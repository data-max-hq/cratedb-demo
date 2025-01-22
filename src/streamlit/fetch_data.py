from services.client import create_cratedb_client
from analytics.fire_locations import find_all

def fetch_all_fire():
    cratedb_client = create_cratedb_client()
    # ... rest of your code 