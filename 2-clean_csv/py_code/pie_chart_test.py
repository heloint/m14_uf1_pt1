'''
Verifies the percentages of NA values for each columns in the table dataset.
Used for determine the how informative a column's data is and does it worth to
keep it.
'''
import pandas as pd
import matplotlib.pyplot as plt

def count_na_percentage(df: pd.DataFrame) -> pd.DataFrame:
    "Calculates what percentage of NA each column has."

    total_rows: int = len(df)

    na_percentages_result: dict[str, float] = {}

    for column in df.columns:

        column_na_sum: int = df[column].isna().sum()  # type:ignore
        column_na_percentage: float = round(((column_na_sum / total_rows) * 100), 2)

        na_percentages_result[column] = column_na_percentage

    return pd.DataFrame(
        data={
            "columns": list(na_percentages_result.keys()),
            "na_percentages": list(na_percentages_result.values()),
        }
    )


def plot_na_percentages(path: str, delimiter: str) -> None:
    "Plots the D.F. of the calculated results as a lineplot."

    pd.set_option('display.max_columns', None)

    df_outbreaks:   pd.DataFrame = pd.read_csv(path, sep=delimiter) #type:ignore
    na_percentages: pd.DataFrame = count_na_percentage(df_outbreaks)
    na_percentages = na_percentages.set_index('columns')
    na_percentages.plot(
        kind="pie",
        title="Percentages of NA per column",
        # x="columns",
        y="na_percentages",
        # xlabel="Columns",
    )
    plt.legend( bbox_to_anchor=(1,0), loc="lower right", 
                              bbox_transform=plt.gcf().transFigure)

    # plt.xticks(range(0, len(na_percentages)), na_percentages['columns'])
    plt.gcf().set_size_inches(8, 8) #type:ignore
    plt.show()


if __name__ == '__main__':
    plot_na_percentages("../../data/outbreaks.csv", ',') 
