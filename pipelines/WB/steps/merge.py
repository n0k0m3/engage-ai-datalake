import glob
import pandas as pd
import polars as pl


def merge_files():
    # Merge Country metadata files
    all_files = glob.glob("./data/Metadata_Country_API_*_DS2_en_csv_v2_*.csv")
    df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
    # drop columns with "Unnamed" in the name
    df = df[df.columns.drop(list(df.filter(regex="Unnamed")))]
    pl.DataFrame(df).write_parquet("./data/Metadata_Country.parquet")

    # Merge Indicators metadata files
    first_file = glob.glob("./data/Metadata_Indicator_API_*_DS2_en_csv_v2_*.csv")[0]
    df = df[df.columns.drop(list(df.filter(regex="Unnamed")))]
    pl.DataFrame(pd.read_csv(first_file)).write_parquet("./data/Metadata_Indicator.parquet")

    # Merge Indicators files
    all_files = glob.glob("./data/API_*_DS2_en_csv_v2_*.csv")
    df = pd.concat((pd.read_csv(f, skiprows=4) for f in all_files), ignore_index=True)
    df = df[df.columns.drop(list(df.filter(regex="Unnamed")))]
    pl.DataFrame(df).write_parquet("./data/Indicator.parquet")
