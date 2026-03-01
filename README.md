🚗 Smart Parking Detection System

An AI-powered Smart Parking System that detects vehicles and determines parking slot availability using YOLOv8 and OpenCV.

This project analyzes video input, detects vehicles in real time, and identifies whether parking slots are FREE or OCCUPIED.

📌 Features

🚘 Real-time vehicle detection using YOLOv8

🅿️ Parking slot occupancy detection

🟢 FREE / 🔴 OCCUPIED status labeling

🎥 Video-based parking monitoring

⚡ Lightweight and efficient model (YOLOv8n)


🛠 Tech Stack

Python

OpenCV

Ultralytics YOLOv8

NumPy

Project Structure
Smart-Parking-System/
│
├── data/               # Input video files
├── models/             # YOLO model files
├── src/                # Source code
│   ├── main.py
│   ├── draw_slots.py
│   └── utils.py
│
├── output/             # Output processed videos
├── screenshots/        # Demo images
│
├── requirements.txt
├── README.md
└── .gitignore


System Workflow

Input Video
     ↓
Frame Extraction (OpenCV)
     ↓
Vehicle Detection (YOLOv8)
     ↓
Parking Slot Mapping
     ↓
Overlap Detection
     ↓
FREE / OCCUPIED Classification
     ↓
Display Output


How It Works

YOLOv8 detects vehicles in each video frame.

Predefined parking slots are mapped using coordinates.

The system checks bounding box overlap.

If overlap exists → slot is marked OCCUPIED.

If no overlap → slot is marked FREE

📜 License

This project is open-source and available under the MIT License.