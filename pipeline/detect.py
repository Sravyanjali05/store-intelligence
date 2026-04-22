from ultralytics import YOLO
import cv2
import json
import uuid
import datetime
from tracker import track

print("🚀 DETECT SCRIPT STARTED")

model = YOLO("yolov8n.pt")

def run(video_path):
    print("🎥 Processing video:", video_path)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("❌ ERROR: Cannot open video")
        return

    events = []
    frame_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("✅ Video finished")
            break

        # 🔥 YOLO inference (results defined HERE)
        results = model(frame, verbose=False)

        detections = []

        # ✅ MUST be inside loop
        for r in results:
            if r.boxes is None:
                continue

            for box in r.boxes:
                if int(box.cls[0]) == 0:  # person
                    x1, y1, x2, y2 = box.xyxy[0].tolist()
                    conf = float(box.conf[0])
                    detections.append([x1, y1, x2, y2, conf])

        # 🔥 TRACK
        tracks = track(detections)

        for cx, cy, track_id in tracks:
            visitor_id = f"VIS_{track_id}"

            event = {
                "event_id": str(uuid.uuid4()),
                "store_id": "STORE_BLR_002",
                "camera_id": "CAM_ENTRY_01",
                "visitor_id": visitor_id,
                "event_type": "ZONE_DWELL",
                "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
                "zone_id": "FLOOR",
                "dwell_ms": 1000,
                "confidence": 0.9
            }

            events.append(event)

        frame_id += 1

    with open("events.json", "w") as f:
        json.dump(events, f, indent=2)

    print(f"🎯 DONE — {len(events)} events written")

if __name__ == "__main__":
    run("input.mp4")