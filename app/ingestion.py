def ingest_events(db, events):
    db.extend(events)
    return {"ingested": len(events)}