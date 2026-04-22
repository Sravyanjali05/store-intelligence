import uuid
import datetime

def create_event(track_id, confidence):
    return {
        "event_id": str(uuid.uuid4()),
        "store_id": "STORE_BLR_002",
        "camera_id": "CAM_ENTRY_01",
        "visitor_id": f"VIS_{track_id}",
        "event_type": "ZONE_DWELL",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "zone_id": "FLOOR",
        "dwell_ms": 1000,
        "confidence": confidence
    }