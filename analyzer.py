import pandas as pd
from glob import glob
from os import sep
import numpy as np
import matplotlib.pyplot as plt

dir = glob('data/*.csv')
names = [file[file.index(sep) + 1:file.index('.')] for file in dir]
files = dict(zip(names, dir))

reader = pd.read_csv(files['England'], encoding='utf-8')

# gets all rows and columns containing value
def get_rows(reader, col:str, value: str):
    return reader.loc[reader[col] == value]

# gets DataFrame col by its name
def get_one_col(df, col: str):
    return df[col]

# calculates mean of DataFrame values of col
def get_mean_of(col: list or tuple):
    return round(np.mean(col), 5)

# draw plot using csv cols as values
def draw(title: str, values: list or tuple, xlabel: str = '', ylabel: str = ''):
    plt.title(title)
    plt.xticks(np.arange(len(col)), np.arange(1, len(col)+1))
    plt.yticks(np.arange(0, max(col) + 1))
    if xlabel != '':
        plt.xlabel(xlabel)
    if ylabel != '':
        plt.ylabel(ylabel)
    plt.plot(values, 'r--', linewidth=2.0)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    team = 'Chelsea'
    rows = get_rows(reader, 'HomeTeam', team)
    col = list(get_one_col(rows, 'FTHG'))
    print(col)
    draw(f'Goals scored at home by {team} during first leg of season 2021-2022', col, 'Matches', 'Goals')