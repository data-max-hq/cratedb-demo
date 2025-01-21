-- This query analyzes emergency call patterns by hour of day,
-- helping identify peak emergency hours.

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