"""JSON file persistence for OpenTrack."""

import json
import os


class JsonStorage:
    """Persists issues to a single JSON file."""

    def __init__(self, path):
        self.path = path

    def load(self):
        """Load issues from disk. Returns a dict of id -> issue."""
        if not os.path.exists(self.path):
            return {}
        with open(self.path, "r", encoding="utf-8") as f:
            raw = json.load(f)
        issues = raw.get("issues", {})
        return {int(k): v for k, v in issues.items()}

    def save(self, issues):
        """Write issues to disk."""
        payload = {"issues": {str(k): v for k, v in issues.items()}}
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
