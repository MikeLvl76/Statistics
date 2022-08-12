from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from reader import read_args, Reader

class Analyzer:

    def __init__(self, reader: Reader) -> None:
        self.reader = reader
        self.data = []
        self.functions = {
            'unique': lambda x: list(np.unique(x)),
            'median': lambda x: np.median(x),
            'average': lambda x: round(np.average(x), 3),
            'max': lambda x: np.max(x),
            'min': lambda x: np.min(x),
            'standard deviation': lambda x: round(np.std(x), 3),
            'variance': lambda x: np.var(x)
        }

    def prepare_reader(self):
        self.reader.fetch_files('data', 'csv')
        self.reader.read()

    def fetch_data(self):
        if self.reader.reader is not None:
            rows = self.reader.get_rows()
            cols = self.reader.get_cols(rows)

            step = len(cols[0])
            flatten = [item for sub in cols for item in sub]
            data = {i: [] for i in range(step)}

            for k in range(len(flatten)):
                data[k % step].append(flatten[k])

            self.data = [data[key] for key in data.keys()]

    def print_statistics(self) -> str:
        team = self.reader.args.team
        functions = list(self.functions.keys())
        data = self.data
        cols = self.reader.args.cols
        json = {team: {
            col: {
                func: self.functions[func](data[cols.index(col)]) for func in functions
                } for col in cols
            }
        }
        pprint(json, width=70)

    def draw_statistics(self):
        data = self.data
        fig, axs = plt.subplots(2)
        fig.suptitle(f'Goals scored and conceded per match by {self.reader.args.team}')

        axs[0].set_title('Goals scored at home')
        axs[1].set_title('Goals conceded at home')

        for ax in axs:
            ax.set_xticks(np.arange(len(data[0])), np.arange(1, len(data[0]) + 1))
            ax.set_yticks(np.arange(0, max(data[0]) + 1))
            ax.set_xlabel('Match number')
            ax.set_ylabel('Goals scored')
            ax.label_outer()
            ax.grid()
            

        colors = iter(cm.rainbow(np.linspace(0, 1, len(data))))
        cols = self.reader.args.cols

        for k in range(int(len(data) / 2)):
            color = next(colors)
            axs[0].plot(data[k], color=color, linewidth=1.5, label=cols[data.index(data[k])])
            axs[0].legend()
            axs[1].plot(data[k + 2], color=color, linewidth=1.5, label=cols[data.index(data[k + 2])])
            axs[1].legend()

        plt.show()

# new version: python3 -u analyzer.py -f="England" -t="Arsenal" -rc="HomeTeam" -c 'FTHG' 'HTHG' 'FTAG' 'HTAG'
if __name__ == '__main__':
    args = read_args()
    reader = Reader(args)
    analyzer = Analyzer(reader)
    analyzer.prepare_reader()
    analyzer.fetch_data()
    analyzer.print_statistics()
    analyzer.draw_statistics()