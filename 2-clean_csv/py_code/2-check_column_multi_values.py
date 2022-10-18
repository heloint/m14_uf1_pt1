'''
Check if any of the column of the source dataset
'''

import pandas as pd
from typing import Generator

def check_if_multi_valued(df: pd.DataFrame) -> Generator[str, None, None]:
    ''' Loops through the given data frame and if finds any multi-value field in
        any column, then returns a Generator with the "multi-valued" column names.
    '''
    
    observed: set = set() 
    for column in df.columns:
        for row in df.to_dict('records'):

            if len(str(row[column]).split(';')) > 1 \
                and column not in observed:

                observed.add(column)

                yield column


if __name__ == '__main__':
    df_outbreaks: pd.DataFrame = pd.read_csv("../data/outbreaks.csv", sep=",")  # type:ignore
    print(set(check_if_multi_valued(df_outbreaks)))
