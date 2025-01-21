SELECT 
    date_trunc('hour', ec.created_at) as time_bucket,
    count(DISTINCT ec.id) as emergency_calls,
    count(DISTINCT w.object_id) as active_fires,
    avg(w.incident_size) as avg_fire_size
FROM emergency_calls ec
LEFT JOIN wfigs w ON date_trunc('hour', ec.created_at) = date_trunc('hour', w.fire_discovery_date_time)
LEFT JOIN wfigs_geo wg ON w.object_id = wg.object_id
WHERE MATCH(ec.transcription_record, 'fire OR smoke OR burning OR wildfire')
GROUP BY time_bucket
ORDER BY time_bucket DESC; 