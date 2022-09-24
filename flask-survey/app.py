from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

responses = []

@app.route('/')
def home():
  """Home Page for surveys"""
  return render_template("home.html", title=satisfaction_survey.title, instruc=satisfaction_survey.instructions)

@app.route('/questions', methods=['POST'])
def initialize():
  """Set session responses to an empty list"""
  ls = []
  session["responses"] = ls
  return redirect("/questions/0")

@app.route('/questions/<int:q_id>')
def show_question(q_id):
  """Show question of given id"""

  # Check if user is at the right URL
  if q_id != len(session["responses"]):
    flash("Trying to access invalid question. Redirecting.")
    q_id = len(session["responses"])
  # If user has answered all questions redirect to thank you page
  if len(session["responses"]) == 4:
    return redirect("/thanks")

  return render_template("form.html", question=satisfaction_survey.questions[q_id])

@app.route('/answer', methods=['POST'])
def answers():
  """Collect answers"""
  responses = session["responses"]
  responses.append(request.form["choice"])
  session["responses"] = responses
  if len(responses) < len(satisfaction_survey.questions):
    return redirect("/questions/" + str(len(responses)))
  return redirect("/thanks")

@app.route('/thanks')
def thanks():
  return render_template("thanks.html")