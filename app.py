import argparse
from email import parser
from unittest import result
from flask import Flask, request

app = Flask(__name__)
app.debug = True

# creating application routes
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user/<name>")
def printName(name):
    return "<h1>Hello, {}!</h1>".format(name)

# add info
@app.route("/add")
def addNumbers():
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = {
        "a": a,
        "b": b,
        "total": (a+b)
    }

    return result

# subtract info
@app.route("/subtract")
def subtractNumbers():
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = {
        "a": a,
        "b": b,
        "difference": (a-b)
    }

    return result

# multiply info
@app.route("/multiply")
def multiplyNumbers():
    # There is a problem here please, fix and test.
    # Fix and test this.
    a = int(request.args["a"])
    b = (request.args["b"])

    result = {
        "a": a,
        "b": b,
        "product": (a*b)
    }

    return result

# divide info
@app.route("/divide")
def divideNumbers():
    a = int(request.args["a"])
    b = (request.args["b"])

    result = {
        "a": a,
        "b": b,
        # There is a problem here please, fix and test.
        # Fix and test this.
        "factor": (a/0) 
    }

    return result

if __name__ == "___main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", action="store", default="5000")
    args=parser.parse_args()
    app.run(host="0.0.0.0", port=int(args.port))