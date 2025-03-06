def get_size_distribution():
    """This query categorizes fires by size and counts them in each category."""
    return """
    SELECT 
        CASE 
            WHEN incident_size <= 10 THEN 'Small (0-10 acres)'
            WHEN incident_size <= 100 THEN 'Medium (11-100 acres)'
            WHEN incident_size <= 1000 THEN 'Large (101-1000 acres)'
            ELSE 'Very Large (1000+ acres)'
        END as size_category,
        COUNT(*) as number_of_fires,
        ROUND(AVG(incident_size), 2) as average_size
    FROM wfigs
    GROUP BY size_category
    ORDER BY 
        CASE size_category
            WHEN 'Small (0-10 acres)' THEN 1
            WHEN 'Medium (11-100 acres)' THEN 2
            WHEN 'Large (101-1000 acres)' THEN 3
            ELSE 4
        END;
    """

def get_fires_by_county():
    """This query shows the distribution of fires across different counties,
    helping identify high-risk areas."""
    return """
    SELECT 
        poo_county,
        COUNT(*) as number_of_fires,
        SUM(incident_size) as total_fire_size,
        AVG(incident_size) as average_fire_size
    FROM wfigs
    GROUP BY poo_county
    ORDER BY number_of_fires DESC;
    """

def get_fires_in_area():
    """This query finds all wildfires within a specific geographic area in Los Angeles County
    (bounded by coordinates forming roughly a rectangle from Long Beach to the Angeles National Forest).
    It returns basic fire information including ID, location, name, discovery time, and size."""
    return """
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
        'POLYGON((-118.6 33.9, -118.6 34.7, -117.8 34.7, -117.8 33.9, -118.6 33.9))');
    """ 