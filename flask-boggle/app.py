from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify

boggle_game = Boggle()
guessed_words = []
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.debug = True

@app.route('/')
def index():
  """Return boggle game board"""

  boggle_board = boggle_game.make_board()
  session['board'] = boggle_board
  session['high-score'] = 0
  session['times-played'] = 0
  return render_template("index.html", board=boggle_board)

@app.route('/check')
def check():
  """Check if word is valid"""

  word = request.args["word"]
  board = session['board']
  # Make sure we can't make duplicate guesses
  if word not in guessed_words:
    # check_valid_word checks that words are in dictionary and on the board
    response = boggle_game.check_valid_word(board, word)
    guessed_words.append(word)
  else:
    response = "Already guessed word"

  return jsonify({'result': response})

@app.route('/end')
def endGame():
  """Handle game ending"""

  score = request.args["score"]
  high_score = session['high-score']
  if high_score < int(score):
    session['high-score'] = int(score)
  session['times-played'] += 1
  return jsonify({'result': session['times-played']})

@app.route('/reset')
def reset():
  """Create a new boggle board to use"""

  boggle_board = boggle_game.make_board()
  session['board'] = boggle_board
  # Doesn't work
  # return render_template("index.html", board=boggle_board)
  return jsonify({'board': boggle_board})
