import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_csv(path: str, delimiter: str) -> pd.DataFrame:
    '''Reads a csv file and returns it 
       as a pandas DataFrame.
    '''

    return pd.read_csv(path, delimiter)

df_outbreaks: pd.DataFrame = read_csv('../data/outbreaks.csv', ',')


def count_na_percentage(df: pd.DataFrame) -> pd.DataFrame:
    ''' Calculates what percentage of
                        NA each column has.
    '''

    total_rows: int = len(df) 
    
    na_percentages_result: dict[str, float] = {}

    for column in df.columns:
        column_na_sum: int = df[column] \
                                    .isna() \
                                    .sum()

        column_na_percentage: float = round((column_na_sum / total_rows) * 100, 2)

        na_percentages_result.setdefault(column, column_na_percentage)

    return pd.DataFrame({'columns'        : list(na_percentages_result.keys()),
                         'na_percentages' : list(na_percentages_result.values())})

na_percentage: pd.DataFrame = count_na_percentage(df_outbreaks)
na_percentage.plot()
plt.show()
