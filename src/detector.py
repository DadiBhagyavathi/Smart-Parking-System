from ultralytics import YOLO
from utils.config import MODEL_PATH, VEHICLE_CLASSES, CONFIDENCE

class VehicleDetector:
    def __init__(self):
        self.model = YOLO(MODEL_PATH)

    def detect(self, frame):
        results = self.model(frame, conf=CONFIDENCE)[0]
        boxes = []
        for box in results.boxes:
            cls = int(box.cls[0])
            if cls in VEHICLE_CLASSES:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                boxes.append((x1, y1, x2, y2))
        return boxes
