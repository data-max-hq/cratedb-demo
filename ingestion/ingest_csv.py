import pandas as pd
import json

def ingest_csv(cratedb_client, csv_file_path: str, table_name:str, delimiter=",") -> None:

    df = pd.read_csv(csv_file_path, encoding="utf-8-sig", sep=delimiter)
    
    # if 'location' in df.columns:oke
    
    columns = list(df.columns)
    columns_str = f", ".join(columns)
    placeholders = ", ".join(["%s"] * len(columns))

    sql_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"

    cursor = cratedb_client.cursor()
    total_records = len(df)
    for index, row in df.iterrows():
        values = tuple(row)

        debug_query = sql_query
        for value in values:
            if isinstance(value, str):
                if value.startswith('[') and value.endswith(']'):
                    # For array values, don't add quotes around them
                    debug_query = debug_query.replace("%s", value, 1)
                else:
                    # For regular strings, remove single quotes and use repr
                    value = value.replace("'", "")
                    debug_query = debug_query.replace("%s", repr(value), 1)
            else:
                debug_query = debug_query.replace("%s", repr(value), 1)
        cursor.execute(debug_query)
        
        if (index + 1) % 50 == 0:
            print(f"Progress: {index + 1}/{total_records} records ingested ({((index + 1)/total_records)*100:.2f}%)")

    print(f"Completed: {total_records}/{total_records} records ingested successfully!")
