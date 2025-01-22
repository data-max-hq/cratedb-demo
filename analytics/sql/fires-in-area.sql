-- This query finds all wildfires within a specific geographic area in Los Angeles County
-- (bounded by coordinates forming roughly a rectangle from Long Beach to the Angeles National Forest).
-- It returns basic fire information including ID, location, name, discovery time, and size.

SELECT 
    w.object_id,
    wg.geometry,
    w.incident_name,
    w.fire_discovery_date_time,
    w.incident_size
FROM wfigs w
JOIN wfigs_geo wg ON w.object_id = wg.object_id
WHERE within(
    wg.geometry,
    'POLYGON((-118.6 33.9, -118.6 34.7, -117.8 34.7, -117.8 33.9, -118.6 33.9))'
); 
-- WORKING