# 🛍️ Store Intelligence System


## 🚀 Overview


The **Store Intelligence System** is an AI-powered video analytics solution that transforms raw CCTV footage into meaningful business insights.

It detects people, tracks movement, generates behavioral events, and exposes real-time analytics through APIs.


---


## 🎯 Key Features


* 👤 **Person Detection** using YOLOv8

* 🔄 **Visitor Tracking** (consistent IDs across frames)

* 📊 **Event Generation Pipeline**

* 🌐 **FastAPI Backend** for real-time analytics

* 📈 **Store Metrics** (visitor count, dwell activity)

* ⚡ **Lightweight & Modular Architecture**


---


## 🧠 How It Works


```text

Video Input → YOLO Detection → Tracking → Event Generation → API → Metrics

```


1. 🎥 Video is processed frame-by-frame

2. 🤖 YOLO detects people

3. 🔍 Tracker assigns unique visitor IDs

4. 📄 Events are generated

5. 🌐 API ingests events

6. 📊 Metrics are computed


---


## 📂 Project Structure


```

store-intelligence/

├── pipeline/ # Detection + Tracking + Event generation

├── app/ # FastAPI backend

├── tests/ # Unit tests

├── data/ # Layout + sample data

├── docs/ # Design & decisions

├── docker-compose.yml

└── README.md

```


---


## ⚙️ Installation


```bash

pip install -r pipeline/requirements.txt

pip install -r app/requirements.txt

```


---


## ▶️ How to Run


### 1️⃣ Run Detection Pipeline


```bash

python pipeline/detect.py

```


### 2️⃣ Start API Server


```bash

uvicorn app.main:app --reload

```


### 3️⃣ Ingest Events


```bash

curl -X POST "http://127.0.0.1:8000/events/ingest" \

-H "Content-Type: application/json" \

--data-binary "@events.json"

```


---


## 📊 API Endpoints


| Endpoint | Description |

| ---------------------------- | ----------------------- |

| `/health` | Check API status |

| `/events/ingest` | Ingest detection events |

| `/stores/{store_id}/metrics` | Get store analytics |


---


## 📈 Sample Output


```json

{

"store_id": "STORE_BLR_002",

"visitors": 197

}

```


---


## 📦 Input Requirements


Place your video file in root directory:


```

input.mp4

```


---


## 🧪 Testing


```bash

pytest

```


---


## 🛠️ Tech Stack


* Python 🐍

* YOLOv8 (Ultralytics)

* OpenCV

* FastAPI

* NumPy


---


## 💡 Use Cases


* Retail store analytics

* Footfall analysis

* Customer behavior tracking

* Smart surveillance systems


---


## ⚠️ Limitations


* Tracking is basic (can be improved with DeepSORT)

* Accuracy depends on video quality


---


## 🚀 Future Enhancements


* 🔥 Heatmaps

* 📊 Funnel analytics

* 🚨 Anomaly detection

* 📱 Dashboard UI


---


## 👨‍💻 Author


**Damodarapatruni Sravyanjali**

B.Tech CSE (Data Science & ML)


---


## ⭐ Final Note


This project demonstrates a **complete real-world AI pipeline** — from video processing to actionable business insights.
