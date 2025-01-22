def get_daily_fire_incidents():
    return r"""
    SELECT 
        DATE_TRUNC('day', fire_discovery_date_time) as discovery_date,
        COUNT(*) as number_of_fires,
        SUM(incident_size) as total_fire_size
    FROM wfigs
    GROUP BY DATE_TRUNC('day', fire_discovery_date_time)
    ORDER BY discovery_date DESC; 
    """
