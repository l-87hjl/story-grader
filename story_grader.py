"""
Story Grader
Grades a story on theme, internal logic, sensory detail, engagement, and marketing appeal.
"""
from datetime import datetime
from typing import Dict
from utils.logging import log_request

def grade_story(story: str) -> Dict[str, float]:
    """Grade a story across multiple artistic and commercial dimensions."""
    log_request(story)

    # Very simple heuristic-based scoring (placeholder for ML / LLM later)
    scores = {
        "theme": min(10.0, max(1.0, len(set(story.split())) / 50)),
        "internal_logic": 7.5,
        "sensory_detail": story.count(" ") / 100,
        "engagement": 6.5,
        "marketing_appeal": 6.0,
    }

    # Normalize
    for k, v in scores.items():
        scores[k] = round(min(10.0, max(1.0, v)), 2)

    scores["overall"] = round(sum(scores.values()) / len(scores), 2)
    scores["graded_at"] = datetime.utcnow().isoformat()
    return scores

if __name__ == "__main__":
    sample = "Once upon a time, a lonely lighthouse keeper listened to the sea whisper secrets."
    print(grade_story(sample))
