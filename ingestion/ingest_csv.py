def ingest_csv(cratedb_client, ddl_scripts_path: str) -> None:
    cursor = cratedb_client.cursor()

    with open(ddl_scripts_path, "r") as sql_file:
        ingest_csv_sql = sql_file.read()

    cursor.execute(ingest_csv_sql)
    cursor.close()
    print("WFIGS data ingested successfully!")
