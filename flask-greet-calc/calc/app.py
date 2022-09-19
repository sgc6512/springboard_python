# Put your app in here.
from flask import Flask
from flask import request
import operations
app = Flask(__name__)

@app.route('/add')
def add():
  a = request.args["a"]
  b = request.args["b"]
  return str(operations.add(int(a), int(b)))

@app.route('/sub')
def sub():
  a = request.args["a"]
  b = request.args["b"]
  return str(operations.sub(int(a), int(b)))

@app.route('/mult')
def mult():
  a = request.args["a"]
  b = request.args["b"]
  return str(operations.mult(int(a), int(b)))

@app.route('/div')
def div():
  a = request.args["a"]
  b = request.args["b"]
  return str(operations.div(int(a), int(b)))

  
### PART TWO

operators = {
        "add": operations.add,
        "sub": operations.sub,
        "mult": operations.mult,
        "div": operations.div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)