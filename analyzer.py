import numpy as np
import matplotlib.pyplot as plt
from reader import read_args, Reader

class Analyzer:

    def __init__(self, reader: Reader) -> None:
        self.reader = reader
        self.data = []
        self.functions = {
            'mean': lambda x: np.mean(x),
            'average': lambda x: np.average(x),
            'max': lambda x: np.max(x),
            'min': lambda x: np.min(x),
            'standard deviation': lambda x: np.std(x)
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
            index = 0

            for k in range(len(flatten)):
                if k % step == 0:
                    data[index].append(flatten[k])
                else:
                    data[k % step].append(flatten[k])

            self.data = [data[key] for key in data.keys()]

    def calculate(self, what: str) -> str:
        if what not in list(self.functions.keys()):
            return '0'
        res = f'Pieces of data on {self.reader.args.team} (2021-2022 season):\n'
        for elt in self.data:
            index = self.data.index(elt)
            names = [name for name in self.reader.args.cols]
            res += f'{what} for {names[index]}: {self.functions[what](elt)}\n'
        return res

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
    print(analyzer.calculate('mean'))