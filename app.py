from flask import Flask, request, render_template
import stories

app = Flask(__name__)


@app.route('/madlib')
def madlib():
    return render_template("madlib.html", prompts=stories.story.prompts)

@app.route('/story')
def story():
  answers = request.args
  text = stories.story.generate(answers)
  return render_template("story.html", story=text)