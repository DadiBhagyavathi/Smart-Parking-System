from collections import deque
from utils.config import HISTORY

class SlotTracker:
    def __init__(self, slot_ids):
        self.history = {sid: deque(maxlen=HISTORY) for sid in slot_ids}

    def update(self, sid, occupied):
        self.history[sid].append(occupied)

    def stable_state(self, sid):
        h = self.history[sid]
        if len(h) == 0:
            return "empty"
        if sum(h) == len(h):
            return "occupied"
        if sum(h) == 0:
            return "empty"
        return "transition"
