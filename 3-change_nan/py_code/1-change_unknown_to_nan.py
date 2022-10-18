import pandas as pd
import numpy as np
from pathlib import Path

df_cases: pd.DataFrame = pd.read_csv('../data/cleaned_csv/2-question_results/cases.csv', sep=',')
df_food : pd.DataFrame = pd.read_csv('../data/cleaned_csv/2-question_results/food.csv', sep=',')

# Question 3.1.
# If the file has no NaN values create some rows with some NaN values.
# ===================================
df_cases.replace('unknown', np.NaN)
df_food.replace('unknown', np.NaN)


# Question 3.2.a
# 2. Now, apply one of these two operations and justify the reason:
# a) Replace the NaN value of a column with another value. (fillna feature)
# ===================================
df_cases['status'].fillna('unknown')


# Save modified dataframes.
# ===============================
output_path = Path('../data/cleaned_csv/3-question_results')
output_path.mkdir(parents=True, exist_ok=True)
df_cases.to_csv(f'{output_path}/cases.csv', index=False)
df_food.to_csv(f'{output_path}/food.csv', index=False)
