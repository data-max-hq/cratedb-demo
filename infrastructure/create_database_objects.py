def create_database_objects(cratedb_client, ddl_scripts_path: str) -> None:
    cursor = cratedb_client.cursor()

    with open(ddl_scripts_path, "r") as sql_file:
        create_table_sql = sql_file.read()

    cursor.execute(create_table_sql)
    cursor.close()
    print("WFIGS table created successfully!")
