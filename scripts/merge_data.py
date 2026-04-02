import pandas as pd

old = pd.read_parquet("green_tripdata_2021-01.parquet")
new = pd.read_parquet("green_tripdata_2021-02.parquet")

merged = pd.concat([old, new], axis=0)

merged.to_parquet("green_tripdata_v2.parquet")