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
    'POLYGON((-120 40, -120 41, -119 41, -119 40, -120 40))'
); 