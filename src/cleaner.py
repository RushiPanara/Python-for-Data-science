import pandas as pd
from dataclasses import dataclass,field

def fill_missing_values(df,report):

    df = df.copy()

    for column in df.columns:

        missing_count = df[column].isnull().sum()

        if missing_count == 0:
            continue

        if pd.api.types.is_numeric_dtype(df[column]):
            median_value = df[column].median()
            df[column] = df[column].fillna(median_value)

        else:

            mode = df[column].mode()

            if not mode.empty:
                df[column] = df[column].fillna(mode.iloc[0])

        report.missing_values_filled += missing_count

    return df

def remove_duplicate(df,report):

    df = df.copy()

    count = df.duplicated().sum()

    if count > 0 :
        print(f"Removing {count} duplicated row...")
        df = df.drop_duplicates()
    else:
        print("No duplicated found")

    report.duplicates_removed += count
    return df

def cleaned_text_column(df):

    df = df.copy()

    text = df.select_dtypes(include=["object","string"]).columns

    for column in text:
        df[column] = df[column].str.strip()

    return df

@dataclass
class CleaningReport:
    rows_before:int
    rows_after: int = 0
    duplicates_removed: int = 0
    missing_values_filled: int = 0

    def to_dict(self):
        return {
            "rows_before": int(self.rows_before),
            "rows_after": int(self.rows_after),
            "duplicates_removed": int(self.duplicates_removed),
            "missing_values_filled": int(self.missing_values_filled)
        }

def clean_dataframe(df):

    report = CleaningReport(
        rows_before=len(df)
    )

    cleaned_df = fill_missing_values(df, report)
    cleaned_df = remove_duplicate(cleaned_df, report)
    cleaned_df = cleaned_text_column(cleaned_df)

    report.rows_after = len(cleaned_df)

    return cleaned_df, report