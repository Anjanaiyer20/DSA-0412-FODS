import pandas as pd
from statistics import mode

data = [15, 22, 17, 19, 22, 17, 29, 24, 17, 15]
print("Mean:", sum(data)/len(data))
print("Median:", pd.Series(data).median())
print("Mode:", mode(data))
print("Variance:", pd.Series(data).var())
