import cv2
import json
import numpy as np
from ultralytics import YOLO

# Load YOLO model (better accuracy)
model = YOLO("yolov8n.pt")

# Load parking slot coordinates
with open("data/slots.json", "r") as f:
    slots = json.load(f)

# Load video
cap = cv2.VideoCapture("data/parking.mp4")

if not cap.isOpened():
    print("❌ Error: Video not found.")
    exit()

# Vehicle classes from COCO
vehicle_classes = ["car", "truck", "bus", "motorbike"]

def point_in_polygon(point, polygon):
    return cv2.pointPolygonTest(np.array(polygon, np.int32), point, False) >= 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("✅ Video finished.")
        break

    # Resize for better detection
    frame = cv2.resize(frame, (1280, 720))

    # Run YOLO
    results = model(frame, conf=0.5)

    detected_vehicles = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label in vehicle_classes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)

                detected_vehicles.append((cx, cy))

                # Draw vehicle box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.circle(frame, (cx, cy), 4, (0, 255, 255), -1)

    # Check each parking slot
    for slot_name, polygon in slots.items():
        polygon_np = np.array(polygon, np.int32)
        occupied = False

        for vehicle_center in detected_vehicles:
            if point_in_polygon(vehicle_center, polygon):
                occupied = True
                break

        color = (0, 0, 255) if occupied else (0, 255, 0)

        cv2.polylines(frame, [polygon_np], True, color, 2)

        status = "OCCUPIED" if occupied else "FREE"
        cv2.putText(frame, status,
                    tuple(polygon[0]),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, color, 2)

    cv2.imshow("Smart Parking System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()