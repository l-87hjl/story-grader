# Story Grader

Story Grader is a lightweight, extensible tool for evaluating written stories across artistic, narrative, and commercial dimensions.

## What It Does
The grader analyzes a story and produces normalized scores (1–10) for:

- **Theme** – clarity and development of central ideas
- **Internal Logic** – coherence and consistency
- **Sensory Detail** – vividness and descriptive richness
- **Engagement** – reader interest and momentum
- **Marketing Appeal** – hook strength and audience viability

An overall score and timestamp are also returned.

## Project Structure
```
story-grader/
├── story_grader.py        # Core grading logic
├── ui_app.py              # Web UI for uploading and grading stories
├── utils/
│   └── logging.py         # Request & change logging
├── logs/
│   ├── requests.log       # User submissions
│   └── changes.log        # System / grading changes
├── agent.changelog        # Changes implemented by the AI agent
└── README.md
```

## Running the Grader (CLI)
```bash
python story_grader.py
```

## Running the Web UI
The UI allows uploading `.txt` or `.pdf` files for grading.

```bash
pip install flask PyPDF2
python ui_app.py
```
Then open:
```
http://127.0.0.1:5000
```

## Logs
- **requests.log** – records every story submission (timestamp + length)
- **changes.log** – records grading logic or system changes

## Roadmap Ideas
- LLM-based qualitative feedback
- Genre-aware grading profiles
- Marketing conversion prediction
- API mode for integrations

---
This project is designed to evolve from heuristic scoring into a fully explainable, AI-assisted story evaluation system.