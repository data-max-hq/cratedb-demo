# CrateDB Wildfire Analytics Demo

A demonstration project showcasing CrateDB's capabilities in handling diverse data types, geospatial queries, full-text search, and real-time analytics through a Streamlit interface.

![CrateDB demo gif](/cratedb-demo-gif.gif)

## Overview

This project combines wildfire incident data with emergency call records to demonstrate CrateDB's ability to:
- Handle geospatial data and queries
- Perform full-text search on transcription records
- Process time-series data
- Manage multiple data types efficiently
- Visualize data through an interactive dashboard


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

## Prerequisites
* Access to a CrateDB cluster: Either a local one using docker-compose, or cloud cluster.
* Python 3.10+
* Poetry 2.0+
* Docker (for local Crate cluster)


## Getting the Code
```bash
git clone https://github.com/data-max-hq/cratedb-demo.git
cd cratedb-demo
```

## Install Dependencies

This also sets up a virtual environment if not already running in one.

```bash
poetry install
```

## Getting the CrateDB cluster
To store the data we will need a CrateDB database. Choose between a free hosted instance in the cloud, or run the database locally.

### Cloud option

Create a database in the cloud at [console.cratedb.cloud](https://console.cratedb.cloud/).

Login or create an account, then follow the prompts to create a "CRFREE" database on shared infrastructure in the cloud of your choice (choose from Amazon AWS, Microsoft Azure and Google Cloud). Pick a region close to where you live to minimize latency between your machine running the code and the database that stores the data.

Once you've created your cluster, you'll see a "Download" button. This downloads a text file containing a copy of your database hostname, port, username and password. Make sure to download these as you'll need them later and won't see them again. Your credentials will look something like this example (exact values will vary based on your choice of AWS/Google Cloud/Azure etc):

```bash
Host:              some-host-name.gke1.us-central1.gcp.cratedb.net
Port (PostgreSQL): 5432
Port (HTTPS):      4200
Database:          crate
Username:          admin
Password:          the-password-will-be-here
```
Wait until the cluster status shows a green status icon and "Healthy" status before continuing. Note that it may take a few moments to provision your database.

### Local Option
The best way to run CrateDB locally is by using Docker. We've provided a Docker Compose file for you. Once you've installed Docker Desktop, you can start the database like this:
```bash
docker compose up
```
Once the database is up and running, you can access the console at:

```bash
http://localhost:4200
```
Note that if you have something else running on port 4200 (CrateDB admin UI) or port 5432 (Postgres protocol port) you'll need to stop those other services first, or edit the Docker compose file to expose these ports at different numbers on your local machine.

## Configure environment variables

1. Create a file named ".env".
2. Configure the environment variables depending on local or cloud CrateDB configuration as such:
```bash
CLUSTER_HOST=your_cratedb_host:4200
CLUSTER_USERNAME=your_username
CLUSTER_PASSWORD=your_password
```

## Running the app

Now we have everything needed for our app to run smoothly.

1. Run python script to create tables and ingest data in CrateDB cluster:
```bash
poetry run python main.py
```   
Wait until the ingestion of data on all three tables is finished.

2. Run the Streamlit application:
```bash
poetry run streamlit run streamlit/streamlit_app.py
```
Visit http://localhost:8501/ to access Streamlit and browse through the different pages and dashboards.

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
