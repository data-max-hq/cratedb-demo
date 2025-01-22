def find_all():
    return """
    SELECT 
    w.incident_name,
    w.fire_discovery_date_time,
    w.incident_size,
    w.fire_cause_general,
    w.poo_county,
    w.poo_state,
    g.geometry as location
        FROM wfigs w
        JOIN wfigs_geo g ON w.object_id = g.object_id
        ORDER BY w.fire_discovery_date_time DESC; 
    """
