import pandas as pd
import json

def ingest_geojson(cratedb_client, json_file_path: str) -> None:

    columns = ['OBJECTID', 'geometry']
    data = []

    with open(json_file_path, 'r') as f:
        geojson = json.load(f)
        for feature in geojson['features']:
            properties = feature['properties']
            geometry = feature['geometry']['coordinates']
            lst = [properties['OBJECTID'], geometry]
            data.append(lst)
    df = pd.DataFrame(data=data, columns=columns)

    df = df.rename(columns={'OBJECTID': 'object_id'})  

    columns_str = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(columns))
    sql_query = f"INSERT INTO wfigs_geo ({columns_str}) VALUES ({placeholders})"

    cursor = cratedb_client.cursor()
    total_records = len(df)
    for index, row in df.iterrows():
        values = tuple(row)

        debug_query = sql_query
        for value in values:
            # if isinstance(value, str):
            #     value = value.replace("'", "")
            debug_query = debug_query.replace("%s", repr(value), 1)
        cursor.execute(debug_query)
        
        if (index + 1) % 50 == 0:
            print(f"Progress: {index + 1}/{total_records} records ingested ({((index + 1)/total_records)*100:.2f}%)")

    print(f"Completed: {total_records}/{total_records} records ingested successfully!")
    