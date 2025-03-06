-- This query categorizes emergency calls based on common keywords
-- to understand the distribution of different types of emergencies.

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