from ultralytics import YOLO
import cv2
import json
from emit import create_event

print("DETECT SCRIPT STARTED")

model = YOLO("yolov8n.pt")

def run(video_path):
    print("Processing video:", video_path)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("ERROR: VIDEO NOT OPENING")
        return

    events = []
    frame_id = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Video finished")
            break

        results = model.track(frame, persist=True, verbose=False)

        for r in results:
            if r.boxes is None:
                continue

            for box in r.boxes:
                if int(box.cls[0]) == 0:
                    track_id = int(box.id[0]) if box.id is not None else frame_id
                    confidence = float(box.conf[0])

                    event = create_event(track_id, confidence)
                    events.append(event)

        frame_id += 1

    cap.release()

    with open("events.json", "w") as f:
        json.dump(events, f, indent=2)

    print("DONE —", len(events), "events written")

if __name__ == "__main__":
    run("input.mp4")