-- This query analyzes the distribution of fires by size categories,
-- helping understand the prevalence of different fire magnitudes.

SELECT 
    CASE 
        WHEN incident_size < 1 THEN 'Less than 1 acre'
        WHEN incident_size < 10 THEN '1-10 acres'
        WHEN incident_size < 100 THEN '10-100 acres'
        WHEN incident_size < 1000 THEN '100-1000 acres'
        ELSE 'Over 1000 acres'
    END as size_category,
    COUNT(*) as number_of_fires,
    AVG(incident_size) as average_size
FROM wfigs
GROUP BY size_category
ORDER BY MIN(incident_size); 