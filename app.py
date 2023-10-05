from flask import Flask
from stories import generate
app = Flask(__name__)

@app.route("/story")
def generated_story():
    return 'story'

