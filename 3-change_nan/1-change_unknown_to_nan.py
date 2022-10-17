from os import wait
import pandas as pd
import numpy as np


df_cases: pd.DataFrame = pd.read_csv('../data/cleaned_csv/cases.csv', sep=',')
df_food : pd.DataFrame = pd.read_csv('../data/cleaned_csv/cases.csv', sep=',')

df_cases.replace('unknown', np.NaN)
print(df_)
