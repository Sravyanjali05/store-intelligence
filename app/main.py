from fastapi import FastAPI, Body
from app.ingestion import ingest_events
from app.metrics import get_metrics
from app.health import health_check

app = FastAPI()
DB = []

@app.post("/events/ingest")
def ingest(events: list = Body(...)):
    return ingest_events(DB, events)

@app.get("/stores/{store_id}/metrics")
def metrics(store_id: str):
    return get_metrics(DB, store_id)

@app.get("/health")
def health():
    return health_check()