import json
from shapely.geometry import Polygon, Point

def load_slots(path):
    with open(path, "r") as f:
        return json.load(f)

def is_occupied(slot_polygon, detections):
    poly = Polygon(slot_polygon)
    for x1, y1, x2, y2 in detections:
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
        if poly.contains(Point(cx, cy)):
            return True
    return False
