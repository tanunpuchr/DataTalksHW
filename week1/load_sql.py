import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://<user>:<pwd>@localhost:5432/ny_taxi")

tables = ["green_tripdata", "taxi_zone_lookup"]
files = [
    "green_tripdata_2019-09.csv",
    "taxi+_zone_lookup.csv",
]

for table, file_data in zip(tables, files):
    df = pd.read_csv(file_data)
    df.to_sql(name=table, con=engine, if_exists="replace")
