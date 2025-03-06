import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from services.client import create_cratedb_client
from analytics.fire_locations import find_all
from analytics.emergency_calls import (
    search_emergency_calls,
    get_calls_by_topic,
    get_all_emergency_calls
)
from analytics.fire_temporal import get_daily_fire_incidents
from analytics.fire_analysis import get_size_distribution, get_fires_in_area

def fetch_all_fire():
    cratedb_client = create_cratedb_client()
    cursor = cratedb_client.cursor()
    
    query = find_all()
    cursor.execute(query)
    
    columns = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    
    return columns, results

def fetch_emergency_calls_search(search_terms: str):
    cratedb_client = create_cratedb_client()
    cursor = cratedb_client.cursor()
    
    query = search_emergency_calls(search_terms)
    cursor.execute(query)
    
    columns = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    
    return columns, results

def fetch_daily_fires():
    cratedb_client = create_cratedb_client()
    cursor = cratedb_client.cursor()
    
    query = get_daily_fire_incidents()
    cursor.execute(query)
    
    columns = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    
    return columns, results

def fetch_calls_by_topic():
    cratedb_client = create_cratedb_client()
    cursor = cratedb_client.cursor()
    
    query = get_calls_by_topic()
    cursor.execute(query)
    
    columns = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    
    return columns, results

def fetch_size_distribution():
    cratedb_client = create_cratedb_client()
    cursor = cratedb_client.cursor()
    
    query = get_size_distribution()
    cursor.execute(query)
    
    columns = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    
    return columns, results

def fetch_fires_in_area():
    cratedb_client = create_cratedb_client()
    cursor = cratedb_client.cursor()
    
    query = get_fires_in_area()
    cursor.execute(query)
    
    columns = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    
    return columns, results

def fetch_all_emergency_calls():
    cratedb_client = create_cratedb_client()
    cursor = cratedb_client.cursor()
    
    query = get_all_emergency_calls()
    cursor.execute(query)
    
    columns = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    
    return columns, results
