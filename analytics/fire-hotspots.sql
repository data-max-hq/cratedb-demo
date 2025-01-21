SELECT 
    count(*) as fire_count,
    avg(w.incident_size) as avg_fire_size,
    within(wg.geometry, 
        format('POLYGON((%s %s, %s %s, %s %s, %s %s, %s %s))',
            round(longitude-0.1, 3), round(latitude-0.1, 3),
            round(longitude-0.1, 3), round(latitude+0.1, 3),
            round(longitude+0.1, 3), round(latitude+0.1, 3),
            round(longitude+0.1, 3), round(latitude-0.1, 3),
            round(longitude-0.1, 3), round(latitude-0.1, 3)
        )) as area
FROM wfigs w
JOIN wfigs_geo wg ON w.object_id = wg.object_id
GROUP BY longitude, latitude
HAVING count(*) > 1
ORDER BY fire_count DESC; 