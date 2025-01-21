import csv
import pandas as pd
import numpy as np

def ingest_csv(cratedb_client, csv_file_path: str) -> None:

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path, encoding="utf-8-sig")

    # Replace NaN with None for compatibility with CrateDB
    df = df.replace([pd.NA, pd.NaT, float("nan"), np.nan, "NaN", ""], None)
    
    df.columns = [col.lower() for col in df.columns]  # Convert column names to lowercase

    columns = list(df.columns)
    columns_str = ", ".join(columns) 
    placeholders = ", ".join(["%s"] * len(columns))  # Create placeholders for all columns, a feature of the cratedb python client

    # Construct the SQL query
    sql_query = f"INSERT INTO wfigs ({columns_str}) VALUES ({placeholders})"

    # Connect to CrateDB and insert data row by row
    cursor = cratedb_client.cursor()
    for _, row in df.iterrows():
        values = tuple(row)  # Convert the row to a tuple
        print(f"SQL Query: {sql_query}")  # Debugging
        print(f"Values: {values}") 
        cursor.execute(sql_query, values)

    print("WFIGS data ingested successfully!")


# def ingest_csv(cratedb_client, ddl_scripts_path: str) -> None:
#     cursor = cratedb_client.cursor()

#     with open(ddl_scripts_path, "r") as sql_file:
#         ingest_csv_sql = sql_file.read()

#     cursor.execute(ingest_csv_sql)
#     result = cursor.fetchall()
#     print(result)
#     row_count = len(result)
#     cursor.close()
#     print(f"WFIGS data ingested successfully! {row_count} rows affected.")
