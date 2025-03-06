CREATE TABLE IF NOT EXISTS emergency_calls (
    created_at TIMESTAMP,
    location GEO_POINT,
    phone_number TEXT,
    transcription_record TEXT INDEX USING fulltext
); 