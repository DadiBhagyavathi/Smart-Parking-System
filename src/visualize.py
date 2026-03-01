import cv2
import numpy as np

def draw(frame, slots, states):
    for sid, polygon in slots.items():
        pts = np.array(polygon, dtype=np.int32)

        if states[sid] == "occupied":
            color = (0, 0, 255)
        elif states[sid] == "empty":
            color = (0, 255, 0)
        else:
            color = (0, 255, 255)

        cv2.polylines(frame, [pts], True, color, 2)
        x, y = polygon[0]
        cv2.putText(frame, sid, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return frame
