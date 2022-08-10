import pandas as pd
from glob import glob
from os import sep

dir = glob('data/*.csv')
names = [file[file.index(sep) + 1:file.index('.')] for file in dir]
files = dict(zip(names, dir))

reader = pd.read_csv(files['Spain'], encoding='utf-8')
print(reader.head())