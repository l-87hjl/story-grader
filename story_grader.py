"""
Story Grader
Grades a story on theme, internal logic, sensory detail, engagement, and marketing appeal.
Supports weighted scoring for art vs commerce.
"""
from datetime import datetime
from typing import Dict
from utils.logging import log_request


def grade_story(story: str, art_weight: float = 0.5) -> Dict[str, float]:
    """
    Grade a story across multiple artistic and commercial dimensions.
    art_weight: 0.0 (pure commerce) -> 1.0 (pure art)
    """
    log_request(story)

    artistic = {
        "theme": min(10.0, max(1.0, len(set(story.split())) / 50)),
        "internal_logic": 7.5,
        "sensory_detail": max(1.0, min(10.0, story.count(" ") / 80)),
    }

    commercial = {
        "engagement": 6.5,
        "marketing_appeal": 6.0,
    }

    # Weighted merge
    scores = {}
    for k, v in artistic.items():
        scores[k] = round(v * art_weight + (1 - art_weight) * 5.0, 2)
    for k, v in commercial.items():
        scores[k] = round(v * (1 - art_weight) + art_weight * 5.0, 2)

    scores["overall"] = round(sum(scores.values()) / len(scores), 2)
    scores["graded_at"] = datetime.utcnow().isoformat()
    scores["art_weight"] = art_weight
    return scores
