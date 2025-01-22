-- This query shows the distribution of fires across different counties,
-- helping identify high-risk areas.

SELECT 
    poo_county,
    COUNT(*) as number_of_fires,
    SUM(incident_size) as total_fire_size,
    AVG(incident_size) as average_fire_size
FROM wfigs
GROUP BY poo_county
ORDER BY number_of_fires DESC