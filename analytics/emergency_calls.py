def get_calls_by_topic():
    """This query categorizes emergency calls based on common keywords
    to understand the distribution of different types of emergencies."""
    return """
    SELECT 
        CASE 
            WHEN transcription_record LIKE ANY (['%fire%', '%smoke%', '%burning%', '%wildfire%']) THEN 'Fire Related'
            WHEN transcription_record LIKE ANY (['%accident%', '%crash%', '%collision%', '%car%']) THEN 'Traffic Accident'
            WHEN transcription_record LIKE ANY (['%medical%', '%injury%', '%hurt%', '%pain%']) THEN 'Medical Emergency'
            WHEN transcription_record LIKE ANY (['%tree%', '%branch%', '%fallen%']) THEN 'Tree Related'
            WHEN transcription_record LIKE ANY (['%crime%', '%theft%', '%robbery%', '%suspicious%']) THEN 'Crime Related'
            ELSE 'Other'
        END as emergency_type,
        COUNT(*) as call_count,
        ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) as percentage
    FROM emergency_calls
    GROUP BY emergency_type
    ORDER BY call_count DESC;
    """

def search_emergency_calls(search_terms: str):
    """Search emergency calls based on provided search terms in the transcription."""
    
    # convert search terms into a format suitable for CrateDB MATCH statement in case we have more than 1 search word
    match_terms = ' OR '.join(f'"{term.strip()}"' for term in search_terms.split())
    
    return f"""
    SELECT
        ec.created_at,
        ec.phone_number,
        ec.transcription_record,
        ec.location,
        _score
    FROM emergency_calls ec
    WHERE match(transcription_record, '{match_terms}')
    ORDER BY _score DESC, ec.created_at DESC;
    """

def get_calls_near_fires():
    """This query finds emergency calls that occurred within 10km of wildfire locations."""
    return """
    SELECT 
        w.incident_name,
        w.fire_discovery_date_time,
        w.incident_size,
        ec.created_at as emergency_call_time,
        ec.transcription_record,
        distance(wg.geometry, ec.location) as distance_meters
    FROM wfigs w
    JOIN wfigs_geo wg ON w.object_id = wg.object_id
    JOIN emergency_calls ec ON distance(wg.geometry, ec.location) <= 10000
    ORDER BY distance_meters ASC;
    """

def get_emergency_response_times():
    """This query calculates average response times between call receipt
    and incident discovery for fire-related emergencies."""
    return """
    SELECT 
        DATE_TRUNC('day', ec.created_at) as date,
        AVG(
            EXTRACT(epoch FROM (w.fire_discovery_date_time - ec.created_at))/60
        ) as avg_response_time_minutes,
        COUNT(*) as number_of_incidents
    FROM emergency_calls ec
    JOIN wfigs w ON 
        DATE_TRUNC('day', ec.created_at) = DATE_TRUNC('day', w.fire_discovery_date_time)
        AND transcription_record LIKE ANY (['%fire%', '%smoke%', '%burning%'])
    GROUP BY DATE_TRUNC('day', ec.created_at)
    ORDER BY date DESC;
    """

def get_hourly_patterns():
    """This query analyzes emergency call patterns by hour of day,
    helping identify peak emergency hours."""
    return """
    SELECT 
        DATE_TRUNC('hour', created_at) as hour_of_day,
        COUNT(*) as total_calls,
        COUNT(CASE 
            WHEN transcription_record LIKE ANY (['%fire%', '%smoke%', '%burning%']) 
            THEN 1 
        END) as fire_related_calls
    FROM emergency_calls
    GROUP BY hour_of_day
    ORDER BY hour_of_day;
    """

def get_all_emergency_calls():
    """Get all emergency calls with basic information."""
    return """
    SELECT
        created_at,
        phone_number,
        location,
        transcription_record
    FROM emergency_calls
    ORDER BY created_at DESC;
    """ 