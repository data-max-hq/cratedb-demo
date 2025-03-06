def get_daily_fire_incidents():
    """This query aggregates the number of fire incidents discovered per day,
    helping visualize daily fire activity patterns."""
    
    return """
    SELECT 
        DATE_TRUNC('day', fire_discovery_date_time) as discovery_date,
        COUNT(*) as number_of_fires,
        SUM(incident_size) as total_fire_size
    FROM wfigs
    GROUP BY DATE_TRUNC('day', fire_discovery_date_time)
    ORDER BY discovery_date DESC;
    """

def get_temporal_correlation():
    """This query analyzes the temporal relationship between fire-related emergency calls
    and actual wildfires. It groups data by hour and shows how many active fires were
    discovered during hours when fire-related emergency calls were made, along with
    the average fire size. This helps identify potential correlations between
    emergency calls and fire incidents."""
    
    return """
    SELECT 
        date_trunc('hour', ec.created_at) as time_bucket,
        count(DISTINCT w.object_id) as active_fires,
        avg(w.incident_size) as avg_fire_size
    FROM emergency_calls ec
    LEFT JOIN wfigs w ON date_trunc('hour', ec.created_at) = date_trunc('hour', w.fire_discovery_date_time)
    LEFT JOIN wfigs_geo wg ON w.object_id = wg.object_id
    WHERE MATCH(ec.transcription_record, 'fire OR smoke OR burning OR wildfire')
    GROUP BY time_bucket
    ORDER BY time_bucket DESC;
    """ 

def get_size_distribution():
    """This query categorizes fires by size and counts them in each category."""
    return """
    SELECT 
        CASE 
            WHEN incident_size <= 10 THEN 'Small (0-10 acres)'
            WHEN incident_size <= 100 THEN 'Medium (11-100 acres)'
            WHEN incident_size <= 1000 THEN 'Large (101-1000 acres)'
            ELSE 'Very Large (1000+ acres)'
        END as size_category,
        COUNT(*) as fire_count,
        ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) as percentage
    FROM wfigs
    GROUP BY size_category
    ORDER BY 
        CASE size_category
            WHEN 'Small (0-10 acres)' THEN 1
            WHEN 'Medium (11-100 acres)' THEN 2
            WHEN 'Large (101-1000 acres)' THEN 3
            ELSE 4
        END;
    """ 