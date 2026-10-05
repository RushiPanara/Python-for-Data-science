# Personal Data Toolkit

A Python-based data quality toolkit for profiling, validating, cleaning, and exporting CSV/JSON datasets.

The project is designed to automate common data-preparation tasks before analysis or machine learning.

---

## Features

### Data Loading
- Load CSV datasets
- Load JSON datasets
- Convert input data into Pandas DataFrames

### Data Profiling
- Dataset dimensions
- Column information
- Data types
- Missing values
- Basic statistical information

### Data Validation
- Validate dataset structure
- Detect missing values
- Check data quality rules
- Identify potential data problems

### Data Cleaning
- Fill missing values
- Remove duplicate rows
- Remove unnecessary whitespace
- Normalize column names
- Convert suitable columns to numeric types
- Convert suitable columns to datetime types

### Cleaning Report
The toolkit generates statistics describing the cleaning process, including:

- Rows before cleaning
- Rows after cleaning
- Duplicate rows removed
- Missing values filled
- Columns renamed
- Numeric conversions
- Datetime conversions

### Export
The toolkit can export:

- Cleaned dataset as CSV
- Cleaning report as JSON

---

## Project Architecture

```text
Personal-Data-Toolkit/
│
├── data/
│   └── customers.csv
│
├── output/
│   ├── cleaned_data.csv
│   └── cleaning_report.json
│
├── src/
│   ├── loader.py
│   ├── profiler.py
│   ├── rules.py
│   ├── validator.py
│   ├── cleaner.py
│   └── exporter.py
│
├── main.py
├── requirements.txt
└── README.md