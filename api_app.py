"""
API mode for Story Grader
Designed for Substack, Medium, CMS, and other integrations.
"""
from flask import Flask, request, jsonify
from story_grader import grade_story

app = Flask(__name__)


@app.route('/grade', methods=['POST'])
def grade():
    data = request.get_json(force=True)
    story = data.get('story', '')
    art_weight = float(data.get('art_weight', 0.5))
    scores = grade_story(story, art_weight=art_weight)
    return jsonify(scores)


if __name__ == '__main__':
    app.run(port=5001)
