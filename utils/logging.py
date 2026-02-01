"""
Logging utilities for Story Grader
"""
import os
from datetime import datetime

REQUEST_LOG = "logs/requests.log"
CHANGE_LOG = "logs/changes.log"

os.makedirs("logs", exist_ok=True)


def log_request(story: str):
    """Log a user story submission."""
    with open(REQUEST_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.utcnow().isoformat()}] STORY_SUBMITTED length={len(story)}\n")


def log_change(description: str):
    """Log a system or grading logic change."""
    with open(CHANGE_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.utcnow().isoformat()}] CHANGE {description}\n")
