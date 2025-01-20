import os

from crate import client


def create_cratedb_client():
    try:
        return client.connect(
            servers=os.getenv("CLUSTER_HOST"),
            username=os.getenv("CLUSTER_USERNAME"),
            password=os.getenv("CLUSTER_PASSWORD"),
        )
    except client.Error as e:
        raise ConnectionError(f"Failed to connect to CrateDB: {str(e)}")
    except Exception as e:
        raise ConnectionError(f"Unexpected error connecting to CrateDB: {str(e)}")
