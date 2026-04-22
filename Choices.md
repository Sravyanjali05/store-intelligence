⚙️ Key Technical Choices
1️⃣ YOLOv8 for Object Detection
✅ Why YOLOv8?
Real-time performance

High accuracy for person detection

Easy integration via Ultralytics

Lightweight (yolov8n.pt) suitable for CPU

❌ Alternatives Considered
Faster R-CNN → high accuracy but slow

SSD → faster but less accurate

🎯 Decision
YOLOv8 chosen for balance of speed and accuracy

2️⃣ FastAPI for Backend
✅ Why FastAPI?
High performance (async support)

Automatic API docs (/docs)

Easy JSON handling

Lightweight compared to Django/Flask

❌ Alternatives Considered
Flask → simpler but lacks async & validation

Django → too heavy for this use case

🎯 Decision
FastAPI chosen for modern, scalable API design

3️⃣ Custom Lightweight Tracker
✅ Why Custom Tracker?
No heavy dependencies (avoids Visual Studio issues)

Works on CPU systems

Simple centroid-based tracking

❌ Alternatives Considered
SORT → requires C++ build tools

DeepSORT → complex and GPU-heavy

🎯 Decision
Custom tracker chosen for simplicity and portability

4️⃣ JSON Event-Based Architecture
✅ Why Event-Based Design?
Modular pipeline

Easy debugging

Scalable for future integrations

Compatible with streaming systems

🎯 Example Event
{
  "event_id": "uuid",
  "visitor_id": "VIS_1",
  "event_type": "ZONE_DWELL"
}
5️⃣ SQLite (In-Memory / Simple DB)
✅ Why SQLite?
No setup required

Lightweight

Suitable for prototype/demo

❌ Alternatives
PostgreSQL → production-ready but heavy

MongoDB → unnecessary for structured data

🎯 Summary
Component	Choice	Reason
Detection	YOLOv8	Speed + accuracy
Backend	FastAPI	Performance + simplicity
Tracking	Custom	No dependency issues
Data	JSON Events	Modular
Database	SQLite	Lightweight
🚀 Final Thought
The system prioritizes:

Simplicity

Performance

Scalability

while remaining easy to deploy and demonstrate.
