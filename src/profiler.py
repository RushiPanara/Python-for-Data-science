def profiler_dataset(df):
    profile = {}

    profile["rows"] = df.shape[0]
    profile["columns"] = df.shape[1]
    profile["column_name"] = list(df.columns)
    profile["duplicate_rows"] = int(df.duplicated().sum())
    profile["memory_usage_bytes"] = int(df.memory_usage(deep=True).sum())

    column_info = {}

    for column in df.columns:
        info = {
            "data_type" : str(df[column].dtype),
            "missing_value" : int(df[column].isnull().sum()),
            "missing_percentage" : round(df[column].isnull().mean()*100,2),
            "unique_value" : int(df[column].nunique())
        }

        if df[column].dtype in ["int64","float64"]:
            info["mean"] = df[column].mean()
            info["median"] = df[column].median()
            info["minimum"] = df[column].min()
            info["maximum"] = df[column].max()
            info["standard_deviation"] = df[column].std()

        column_info[column] = info


    profile["column_info"] = column_info


    return profile

def print_profile(profile):

    print("\n========== DATABASE PROFILE ==========")

    print(f"\nRows : {profile['rows']}")
    print(f"Columns : {profile['columns']}")
    print(f"Duplicate Rows: {profile['duplicate_rows']}")
    print(f"Memory Usage: {profile['memory_usage_bytes']} bytes")

    print("\n========== Column Information ==========")

    for column,info in profile["column_info"].items():

        print(f"\nColumn: {column}")
        print(f"  Data Type: {info['data_type']}")
        print(f"  Missing Values: {info['missing_value']}")
        print(f"  Missing Percentage: {info['missing_percentage']}%")
        print(f"  Unique Values: {info['unique_value']}")

        if "mean" in info:
            print(f"Mean : {info['mean']:.2f}")
            print(f"  Median: {info['median']:.2f}")
            print(f"  Minimum: {info['minimum']}")
            print(f"  Maximum: {info['maximum']}")
            print(f"  Standard Deviation: {info['standard_deviation']:.2f}")