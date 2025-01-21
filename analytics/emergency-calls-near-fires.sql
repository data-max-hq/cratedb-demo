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
WHERE w.incident_status = 'Active'
ORDER BY distance_meters ASC; 