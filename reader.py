from argparse import Namespace
import argparse
import pandas as pd
from glob import glob
from os import sep

# reads command prompt arguments
# returns these arguments
def read_args():
    parser = argparse.ArgumentParser(description="Arguments and their features",
                                            usage='%(prog)s [-h] [-f FILE] [-t TEAM] [-rc RELATEDCOL] [-c COLS]',
                                            epilog="Use -h or --help to see more about arguments")
    parser.add_argument(
        '-f', '--file', help='Give filename (extension is optionnal)', type=str, required=True)

    parser.add_argument(
        '-t', '--team', help='Type a team name', type=str, required=False)

    parser.add_argument(
        '-rc', '--relatedCol', help='Type column name related to team', type=str, required=False)

    parser.add_argument(
        '-c', '--cols', help='Type columns name', nargs="+", required=False)

    return parser.parse_args()

class Reader:

    def __init__(self, args: Namespace) -> None:
        self.args = args
        self.files = dict()
        self.reader = None

    def fetch_files(self, dirname: str, extension: str) -> None:
        dir = glob(f'{dirname}{sep}*.{extension}')
        names = [file[file.index(sep) + 1:file.index('.')] for file in dir]
        self.files = dict(zip(names, dir))

    def read(self) -> None:
        file = self.args.file
        if file.find('.') != -1:
            file = file[:file.index(".")]
        if file not in list(self.files.keys()):
            return None
        self.reader = pd.read_csv(self.files[file], encoding='utf-8')

    # gets all data related to value in column
    def get_rows(self):
        return self.reader.loc[self.reader[self.args.relatedCol] == self.args.team]

    def get_cols(self, df: pd.DataFrame):
        return df.loc[:, self.args.cols].values.tolist()

# tested with: 
# python3 -u reader.py --file="France" --team="Nantes" --relatedCol="HomeTeam" --cols 'FTHG' (v1)
# python3 -u reader.py -f="France" -t="Nantes" -rc="HomeTeam" -c 'FTHG' (v2)
if __name__ == '__main__':
    rdr = Reader(read_args())
    rdr.fetch_files('data', 'csv')
    rdr.read()
    if rdr.reader is not None:
        rows = rdr.get_rows()
        cols = rdr.get_cols(rows)
        print(cols)