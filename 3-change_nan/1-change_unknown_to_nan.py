from os import wait
import pandas as pd
import numpy as np

df_cases: pd.DataFrame = pd.read_csv('../data/cleaned_csv/cases.csv', sep=',')
df_food : pd.DataFrame = pd.read_csv('../data/cleaned_csv/food.csv', sep=',')

# Question 3.1.
# If the file has no NaN values create some rows with some NaN values.
# ===================================
df_cases.replace('unknown', np.NaN)
df_food.replace('unknown', np.NaN)


# Question 3.2.a
# 2. Now, apply one of these two operations and justify the reason:
# a) Replace the NaN value of a column with another value. (child feature)
# ===================================
df_food['status'].replace(np.NaN, 'unknown')
