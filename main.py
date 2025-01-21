from dotenv import load_dotenv

from ingestion.ingest_csv import ingest_csv
from services.client import create_cratedb_client
from infrastructure.create_database_objects import create_database_objects
from ingestion.ingest_geojson import ingest_geojson

load_dotenv()

# Create CrateDB client
cratedb_client = create_cratedb_client()

# Create infrastructure

# create_database_objects(cratedb_client, "sql/wfigs.sql")
# create_database_objects(cratedb_client, "sql/wfigs-geo.sql")
create_database_objects(cratedb_client, "sql/emergency-calls.sql")

# Data ingestion
# ingest_csv(cratedb_client, "data/wfigs-partial.csv", table_name="wfigs")
# ingest_geojson(cratedb_client, "data/wfigs.geojson")
ingest_csv(cratedb_client, "data/emergency_calls.csv", delimiter=";", table_name="emergency_calls")
