"""
Simple web UI for Story Grader
Allows users to upload .txt or .pdf stories and tune art vs commerce weighting.
"""
from flask import Flask, request, render_template_string
from story_grader import grade_story
from PyPDF2 import PdfReader

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Story Grader</title>
<h1>Upload a Story</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=file required><br><br>
  <label>Art ↔ Commerce Weight:</label><br>
  <input type=range name=art_weight min=0 max=1 step=0.05 value=0.5>
  <span>(0 = commerce, 1 = art)</span><br><br>
  <input type=submit value=Grade>
</form>
{% if scores %}
<h2>Results</h2>
<ul>
{% for k, v in scores.items() %}
  <li><strong>{{k}}</strong>: {{v}}</li>
{% endfor %}
</ul>
{% endif %}
"""


def extract_text(file):
    if file.filename.lower().endswith('.txt'):
        return file.read().decode('utf-8')
    if file.filename.lower().endswith('.pdf'):
        reader = PdfReader(file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    return ""


@app.route('/', methods=['GET', 'POST'])
def upload():
    scores = None
    if request.method == 'POST':
        file = request.files.get('file')
        art_weight = float(request.form.get('art_weight', 0.5))
        if file:
            story = extract_text(file)
            scores = grade_story(story, art_weight=art_weight)
    return render_template_string(HTML, scores=scores)


if __name__ == '__main__':
    app.run(debug=True)
