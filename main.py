from dotenv import load_dotenv
from services.client import create_cratedb_client
from infrastructure.create_database_objects import create_database_objects

load_dotenv()

# Create CrateDB client
cratedb_client = create_cratedb_client()

# Create infrastructure
create_database_objects(cratedb_client, "sql/wfigs.sql")

# Data ingestion
