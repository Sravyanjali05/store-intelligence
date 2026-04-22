# Simple centroid tracker (no external libs)

import math

class SimpleTracker:
    def __init__(self):
        self.next_id = 0
        self.objects = {}

    def update(self, detections):
        new_objects = {}

        for det in detections:
            x1, y1, x2, y2, conf = det
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            matched_id = None

            for obj_id, (ox, oy) in self.objects.items():
                dist = math.hypot(cx - ox, cy - oy)
                if dist < 50:  # threshold
                    matched_id = obj_id
                    break

            if matched_id is None:
                matched_id = self.next_id
                self.next_id += 1

            new_objects[matched_id] = (cx, cy)

        self.objects = new_objects

        tracks = []
        for obj_id, (cx, cy) in self.objects.items():
            tracks.append((cx, cy, obj_id))

        return tracks


tracker = SimpleTracker()

def track(detections):
    return tracker.update(detections)