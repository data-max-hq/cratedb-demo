-- This query searches emergency call transcripts for fire-related keywords
-- (fire, smoke, burning, wildfire) and returns call details sorted by
-- relevance score and time. This helps identify potential fire reports
-- from emergency calls.

def search_text(terms:list):
    SELECT
        ec.created_at,
        ec.phone_number,
        ec.transcription_record,
        ec.location
    FROM emergency_calls ec
    WHERE MATCH(transcription_record, 'OR '.join(terms))
    ORDER BY _score DESC, ec.created_at DESC;
