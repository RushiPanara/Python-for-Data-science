import pandas as pd

def check_missing_values(df):

    issues = {}

    for column in df.columns:

        missing_count = int(df[column].isnull().sum())

        if missing_count>0:
            issues[column] = missing_count

    return issues


def check_duplicates(df):
    
    duplicate_count = int(df.duplicated().sum())
    
    return duplicate_count


def check_numeric_rules(df,rules):

    issues = []

    for column, column_rules in rules.items():

        if column not in df.columns:
            continue

        for index,Value in df[column].items():

            if pd.isna(Value):
                continue

            if "min" in column_rules:
                if Value<column_rules["min"]:
                    issues.append({
                        "column": column,
                        "row": index,
                        "value": Value,
                        "problem": "below minimum"
                    })

            if "max" in column_rules:
                if Value > column_rules["max"]:
                    issues.append({
                        "column": column,
                        "row": index,
                        "value": Value,
                        "problem": "above maximum"
                    })
    return issues


def check_allowed_values(df, rules):
    issues = []

    for column, column_rules in rules.items():

        if column not in df.columns:
            continue

        if "allowed_values" not in column_rules:
            continue

        allowed_values = column_rules["allowed_values"]

        for index, value in df[column].items():

            if pd.isna(value):
                continue

            if value not in allowed_values:
                issues.append({
                    "column": column,
                    "row": index,
                    "value": value,
                    "problem": "value not allowed"
                })

    return issues