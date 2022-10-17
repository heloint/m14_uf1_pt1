import pandas as pd
import numpy as np

df_cases: pd.DataFrame = pd.read_csv('../data/cleaned_csv/2-question/cases.csv', sep=',')
df_food : pd.DataFrame = pd.read_csv('../data/cleaned_csv/2-question/food.csv', sep=',')

# Question 3.1.
# If the file has no NaN values create some rows with some NaN values.
# ===================================
df_cases.replace('unknown', np.NaN)
df_food.replace('unknown', np.NaN)


# Question 3.2.a
# 2. Now, apply one of these two operations and justify the reason:
# a) Replace the NaN value of a column with another value. (child feature)
# ===================================
df_cases['status'].replace(np.NaN, 'unknown')


# Save modified dataframes.
# ===============================
df_cases.to_csv('../data/cleaned_csv/3-question/cases.csv', index=False)
df_food.to_csv('../data/cleaned_csv/3-question/food.csv', index=False)
