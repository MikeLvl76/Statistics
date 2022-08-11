import numpy as np
import matplotlib.pyplot as plt
from reader import read_args, Reader, call_reader

# # calculates mean of DataFrame values of col
# def get_mean_of(col: list or tuple):
#     return round(np.mean(col), 5)

# # draw plot using csv cols as values
# def draw(title: str, values: list or tuple, xlabel: str = '', ylabel: str = ''):
#     plt.title(title)
#     plt.xticks(np.arange(len(col)), np.arange(1, len(col)+1))
#     plt.yticks(np.arange(0, max(col) + 1))
#     if xlabel != '':
#         plt.xlabel(xlabel)
#     if ylabel != '':
#         plt.ylabel(ylabel)
#     plt.plot(values, 'ro', linewidth=2.0)
#     plt.grid()
#     plt.show()

# tested with: 
# python3 -u analyzer.py --file="France" --team="Nantes" --relatedCol="HomeTeam" --cols 'FTHG' (v1)
# python3 -u analyzer.py -f="France" -t="Nantes" -rc="HomeTeam" -c 'FTHG' (v2)
if __name__ == '__main__':
    call_reader()