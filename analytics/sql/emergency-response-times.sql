-- This query calculates average response times between call receipt
-- and incident discovery for fire-related emergencies.

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