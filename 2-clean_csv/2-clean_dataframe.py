"""
Clean DataFrame from:
    - Uninformative columns.
    - Completely / Partially rows.
    - Split columns to different DataFrames.
"""
import re
import pandas as pd
from pathlib import Path


def drop_uninformative_columns(df: pd.DataFrame) -> pd.DataFrame:
    "Drops unnecessary columns, because they are uninformative.."

    # Lowercase all column names
    df.columns = df.columns.str.lower()

    # Drop columns
    df.drop(["ingredient", "serotype/genotype"], inplace=True, axis=1)  # type:ignore

    # Drop uninformative rows.
    # If it has <= 5 columns, gets dropped.
    df.dropna(thresh=5, inplace=True)  # type: ignore

    return df


def split_df(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    "Split the dataframe into 'df_cases' and 'df_food'."

    # Add primary keys for each cases
    df.insert(0, "case_id", df.index + 1)

    # - Create dataframe for the food column. [case_id,  food].
    df_food: pd.DataFrame = pd.DataFrame(df.loc[:, ["case_id", "food"]])

    # - Create "cases" dataframe (all columns, except food..).
    df_cases: pd.DataFrame = pd.DataFrame(df.loc[:, df.columns != "food"])

    df_food.reset_index(inplace=True)
    cleaned_df_food: dict[str, list[int | str]] = {"case_id": [], "food": []}

    for _, row in df_food.iterrows():

        split_food = map(str.strip, re.split(r",|;", str(row["food"])))

        for food in split_food:
            food = food.replace("unspecified", "unknown")
            if food == "nan":
                food = "unknown"

            food = food.lower()

            cleaned_df_food["case_id"] += row["case_id"],  # type: ignore
            cleaned_df_food["food"]    += food,

    return df_cases, pd.DataFrame(cleaned_df_food)  # type:ignore


def write_dataframe_to_csv(path: str, df: pd.DataFrame) -> None:
    "Writes out the given DF to a csv file."

    filepath = Path(path)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(filepath, index=False)


if __name__ == "__main__":
    df_outbreaks: pd.DataFrame = pd.read_csv("../data/outbreaks.csv", sep=",")  # type:ignore

    trimmed_df_outbreaks: pd.DataFrame = drop_uninformative_columns(df_outbreaks)

    df_cases, df_food = split_df(trimmed_df_outbreaks)

    write_dataframe_to_csv("../data/cleaned_csv/cases.csv", df_cases)
    write_dataframe_to_csv("../data/cleaned_csv/food.csv", df_food)
