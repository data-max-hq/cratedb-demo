import os
from crate import client
from dotenv import load_dotenv

load_dotenv()

cluster_connection = client.connect(
    servers=os.getenv("CLUSTER_HOST"),
    username=os.getenv("CLUSTER_USERNAME"),
    password=os.getenv("CLUSTER_PASSWORD"),
)

with cluster_connection:
    cursor = cluster_connection.cursor()
    cursor.execute("SELECT name FROM sys.cluster")
    result = cursor.fetchone()
    print(result)
