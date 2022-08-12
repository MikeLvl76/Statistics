# Some results

## With command
-  `python3 -u analyzer.py -f="France" -t="Nantes" -rc="HomeTeam" -c 'FTHG' 'FTAG' 'HTHG'`

```
{'Nantes': {'FTAG': {'average': 1.053,
                     'max': 3,
                     'median': 1.0,
                     'min': 0,
                     'standard deviation': 0.825,
                     'unique': [0, 1, 2, 3],
                     'variance': 0.6814404432132964},
            'FTHG': {'average': 1.737,
                     'max': 5,
                     'median': 2.0,
                     'min': 0,
                     'standard deviation': 1.408,
                     'unique': [0, 1, 2, 3, 4, 5],
            'HTAG': {'average': 0.526,
                     'max': 2,
                     'median': 0.0,
                     'min': 0,
                     'standard deviation': 0.678,
                     'unique': [0, 1, 2],
                     'variance': 0.45983379501385047},
            'HTHG': {'average': 0.579,
                     'max': 3,
                     'median': 0.0,
                     'min': 0,
                     'standard deviation': 0.748,
                     'unique': [0, 1, 3],
                     'variance': 0.5595567867036011}}}
```

With use of [pprint](https://docs.python.org/3/library/pprint.html) as output function

## By drawing plots

![results](/results/nantes.png)

# Used libraries 

Here is a list of used libraires for this project :

- [pprint](https://docs.python.org/3/library/pprint.html)
- [NumPy](https://numpy.org/doc/stable/)
- [matplotlib](https://matplotlib.org/)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [pandas](https://pandas.pydata.org/)
- [glob](https://docs.python.org/3/library/glob.html)
- [os](https://docs.python.org/3/library/os.html)