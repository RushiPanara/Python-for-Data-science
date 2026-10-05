import json
from pathlib import Path
import pandas as pd

def export_data(df,output_path):

    output_path = Path(output_path)

    output_path.parent.mkdir(parents=True,exist_ok=True)

    df.to_csv(output_path,index=False)

    

def export_cleaning_report(report, output_path):

    output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            report.to_dict(),
            file,
            indent=4
        )