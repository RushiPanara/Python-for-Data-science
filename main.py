from src.loader import load_csv
from src.profiler import profiler_dataset , print_profile
from src.validator import (check_missing_values,check_duplicates,check_numeric_rules,check_allowed_values)
from src.rules import VALIDATION_RULES
from src.cleaner import clean_dataframe
from src.exporter import export_cleaning_report,export_data

file_path = "examples/customers.csv"

df = load_csv(file_path)
#print(df)

profile = profiler_dataset(df)

print_profile(profile)


print("\n========== DATA QUALITY ==========")
print("\nMissing Values:")

missing_issues = check_missing_values(df)
for column, count in missing_issues.items():
    print(f"  {column}: {count}")

duplicate_count = check_duplicates(df)
print(f"\nDuplicate Rows: {duplicate_count}")

numeric_issues = check_numeric_rules(df,VALIDATION_RULES)

print("\nNumeric Rule Violations:")

for issue in numeric_issues:
    print(
        f"  {issue['column']} | "
        f"Row {issue['row']} | "
        f"Value: {issue['value']} | "
        f"{issue['problem']}"
    )

categorical_issues = check_allowed_values(df,VALIDATION_RULES)
print("\nAllowed Value Violations:")

for issue in categorical_issues:
    print(
        f"  {issue['column']} | "
        f"Row {issue['row']} | "
        f"Value: {issue['value']} | "
        f"{issue['problem']}"
    )

cleaned_df, report = clean_dataframe(df)

export_data(cleaned_df,"output/cleaned_data.csv")
export_cleaning_report(report,"output/cleaning_report.json")
print("\nCleaning completed.")
print("Cleaned data: output/cleaned_data.csv")
print("Cleaning report: output/cleaning_report.json")

print("\nCleaned Data:")
print(cleaned_df)

print("\nCleaning Report:")
print(report.to_dict())


