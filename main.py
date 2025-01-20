from dotenv import load_dotenv
from services.client import create_cratedb_client
from infrastructure.create_database_objects import create_database_objects
from ingestion.ingest_csv import ingest_csv

load_dotenv()

# Create CrateDB client
cratedb_client = create_cratedb_client()

# Create infrastructure
create_database_objects(cratedb_client, "sql/wfigs.sql")

# Data ingestion
ingest_csv(cratedb_client, "sql/wfigs-csv-ingest.sql")

# todo: Sindi - Ingest wfigs.csv data in CrateDB
# todo: Sindi - Create table for /wfigs.geojson (check wfigs-geo.sql)
# todo: Sindi - Ingest /wfigs.geojson data to CrateDB