COPY wfigs FROM 'https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/WFIGS_Incident_Locations_YearToDate/FeatureServer/replicafilescache/WFIGS_Incident_Locations_YearToDate_2794279842831865174.csv' 
WITH (
    format = 'csv', 
    header = true,
    skip_errors = true
) 
RETURN SUMMARY;