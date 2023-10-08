from flask import Flask, request, render_template
import stories
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY']="madlibs3427"
debug = DebugToolbarExtension(app)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/form")
def generate_inputs():
    story_factors = stories.story_words()
    return render_template("questions.html", story_factors=story_factors)

@app.route("/story", methods=["POST"])
def generated_story():
    keys = stories.story_words()
    vals = list()
    answers = dict()
    for ind in range(len(keys)):
        answers[keys[ind-1]] = request.form[keys[ind-1]]
    story_template = stories.story
    final_story = story_template.generate(answers)
    return render_template("story.html", final_story = final_story)

