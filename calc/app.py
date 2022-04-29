from ast import operator
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)


@app.route('/add')
def p_add():
    """Add a and B"""
    a = request.args['a']
    b = request.args['b']
    return f"<h1>Adding gives us: {add(int(a), int(b))} </h1>"


@app.route('/sub')
def p_sub():
    """Subtract a and B"""
    a = request.args['a']
    b = request.args['b']
    return f"<h1>Subtracting gives us: {sub(int(a), int(b))} </h1>"


@app.route('/mult')
def p_mult():
    """Multiply a and B"""
    a = request.args['a']
    b = request.args['b']
    return f"<h1>Multiplying gives us: {mult(int(a), int(b))} </h1>"


@app.route('/div')
def p_div():
    """Divide a and B"""
    a = request.args['a']
    b = request.args['b']
    return f"<h1>Dividing gives us: {div(int(a), int(b))} </h1>"

# Part 2


operators = {
    "add": add,
    "sub": sub,
    "div": div,
    "mult": mult
}


@app.route("/math/<oper>")
def p_math(oper):
    """Do math on a and b"""
    a = request.args.get('a')
    b = request.args.get('b')
    return f"<h1>Dividing gives us: {operators[oper](int(a), int(b))} </h1>"
