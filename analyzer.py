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


if __name__ == '__main__':
    rows = get_rows(reader, 'HomeTeam', 'Arsenal')
    col = list(get_one_col(rows, 'FTHG'))
    print(col)