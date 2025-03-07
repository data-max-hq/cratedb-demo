CREATE TABLE IF NOT EXISTS wfigs (
    object_id INTEGER,
    source_oid INTEGER,
    created_by_system TEXT,
    incident_size DOUBLE PRECISION,
    discovery_acres DOUBLE PRECISION,
    dispatch_center_id TEXT,
    fire_cause_general TEXT,
    fire_discovery_date_time TIMESTAMP,
    gacc TEXT,
    incident_name TEXT,
    irwin_id TEXT,
    poo_county TEXT,
    poo_state TEXT,
    unique_fire_identifier TEXT,
    created_on_date_time_dt TIMESTAMP,
    source_global_id TEXT,
    global_id TEXT
);