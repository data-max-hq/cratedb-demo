SELECT 
    ec.created_at,
    ec.phone_number,
    ec.transcription_record,
    ec.location
FROM emergency_calls ec
WHERE MATCH(transcription_record, 'fire OR smoke OR burning OR wildfire')
ORDER BY _score DESC, ec.created_at DESC; 