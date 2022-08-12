from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
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

# previously tested with: 
# python3 -u analyzer.py --file="France" --team="Nantes" --relatedCol="HomeTeam" --cols 'FTHG' (v1)
# python3 -u analyzer.py -f="France" -t="Nantes" -rc="HomeTeam" -c 'FTHG' (v2)

# now tested with : python3 -u analyzer.py -f="France" -t="Nantes" -rc="HomeTeam" -c 'FTHG' 'FTAG' 'HTHG'
if __name__ == '__main__':
    args = read_args()
    reader = Reader(args)
    analyzer = Analyzer(reader)
    analyzer.prepare_reader()
    analyzer.fetch_data()
    analyzer.print_statistics()