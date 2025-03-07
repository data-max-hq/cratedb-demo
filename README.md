# CrateDB Wildfire Analytics Demo

A demonstration project showcasing CrateDB's capabilities in handling diverse data types, geospatial queries, full-text search, and real-time analytics through a Streamlit interface.

## Overview

This project combines wildfire incident data with emergency call records to demonstrate CrateDB's ability to:
- Handle geospatial data and queries
- Perform full-text search on transcription records
- Process time-series data
- Manage multiple data types efficiently
- Visualize data through an interactive dashboard

## Project Structure

```
├── analytics/
│   ├── emergency_calls.py    # Emergency calls analysis queries
│   ├── fire_analysis.py      # Fire incident analysis
│   ├── fire_locations.py     # Geospatial queries
│   ├── fire_temporal.py      # Time-based analysis
│   └── sql/                  # Raw SQL queries
├── infrastructure/
│   └── create_database_objects.py  # Database setup
├── ingestion/
│   ├── ingest_csv.py        # CSV data ingestion
│   └── ingest_geojson.py    # GeoJSON data ingestion
├── services/
│   └── client.py            # CrateDB connection handling
├── sql/
│   ├── emergency-calls.sql  # Emergency calls table schema
│   ├── wfigs.sql           # Wildfire incidents schema
│   └── wfigs-geo.sql       # Geospatial data schema
├── streamlit/
│   ├── streamlit_app.py    # Main Streamlit application
│   └── fetch_data.py       # Data fetching utilities
```

## Features

### 1. Interactive Dashboards
- Daily fire incidents visualization
- Emergency call type distribution
- Fire size distribution analysis
- Geographic visualization of fires in LA County

### 2. Data Analysis Capabilities
- Temporal correlation between fires and emergency calls
- Geospatial analysis of fire locations
- Full-text search in emergency call transcripts
- Statistical analysis of fire sizes and distributions

### 3. Search Functionality
- State-based wildfire filtering
- Keyword-based emergency call search
- Interactive map visualization

## Technology Stack

- **Database**: CrateDB
- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Language**: Python 3.10+

## Setup

1. Install dependencies:
```bash
poetry install
```

2. Configure environment variables:
```bash
CLUSTER_HOST=your_cratedb_host
CLUSTER_USERNAME=your_username
CLUSTER_PASSWORD=your_password
```

3. Run python app to create tables and ingest data in CrateDB cluster:
```bash
poetry run python main.py
```   

4. Run the Streamlit application:
```bash
poetry run streamlit run streamlit/streamlit_app.py
```

## Data Types Demonstrated

- **Geospatial**: GEO_POINT for fire and emergency locations
- **Temporal**: TIMESTAMP for event timing
- **Numeric**: DOUBLE PRECISION for fire sizes
- **Text**: TEXT with fulltext indexing for search
- **Categorical**: TEXT for classifications

## Key SQL Features Used

- Geospatial functions (within, distance)
- Full-text search (MATCH)
- Time-based aggregations (DATE_TRUNC)
- Complex JOINs
- Window functions
- Case statements
- Group by operations
