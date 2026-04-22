🏗️ System Design
🎯 Overview
The Store Intelligence System follows a modular pipeline architecture:

Video → Detection → Tracking → Event Generation → API → Metrics
🧩 Components
1️⃣ Video Processing Layer
Input: input.mp4

Extract frames using OpenCV

Process frame-by-frame

2️⃣ Detection Layer
Model: YOLOv8

Detects persons in each frame

Outputs bounding boxes

3️⃣ Tracking Layer
Assigns consistent IDs across frames

Uses centroid-based tracking

Ensures unique visitor identification

4️⃣ Event Generation Layer
Converts detections into structured events

Example Event:
{
  "event_id": "uuid",
  "visitor_id": "VIS_1",
  "timestamp": "ISO format",
  "zone_id": "FLOOR"
}
5️⃣ API Layer (FastAPI)
Handles:

Event ingestion

Metrics computation

Health checks

Endpoints:
/events/ingest

/stores/{store_id}/metrics

/health

6️⃣ Data Storage
In-memory storage (list / SQLite)

Stores all events

Used for analytics

🔄 Data Flow
Frame → Detection → Tracking → Event → API → Metrics
📊 Metrics Computation
Metrics are derived from events:

Unique visitors → unique(visitor_id)

Dwell activity → event count

Store insights → aggregated data

🧠 Design Principles
✅ Modularity
Each component is independent and replaceable

✅ Scalability
Can be extended to:

Kafka (streaming)

Cloud APIs

Real-time dashboards

✅ Simplicity
Minimal dependencies

Easy setup

Works on local machines

⚠️ Limitations
Basic tracking (not DeepSORT)

CPU-based performance

Single camera support

🚀 Future Improvements
Multi-camera support

Advanced tracking (DeepSORT)

Heatmaps

Real-time dashboard

Cloud deployment

🏁 Conclusion
This system demonstrates a complete AI pipeline:

From raw video

To structured insights

Delivered via scalable APIs

It is designed to be practical, efficient, and extensible.

