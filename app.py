""" A simple Python script to run various endpoints based on a url to perform basic calculations"""
import argparse
from math import log

from flask import Flask, request


app = Flask(__name__)
app.debug = True


# creating application routes
@app.route("/")
def hello_world():
    """A simple function that prints Hello,World!"""
    return "<p>Hello, World!</p>"


@app.route("/user/<name>")
def print_name(name):
    """A simple function that prints the Hello, <args-given>"""
    return f"<h1>Hello, {name}!</h1>"


# add info
@app.route("/add")
def add_numbers():
    """A simple function to add 2 numbers"""
    input_1 = int(request.args["input_1"])
    input_2 = int(request.args["input_2"])

    addition_result = {
        "input_1": input_1,
        "input_2": input_2,
        "total": (input_1 + input_2)
    }

    return addition_result


# subtract info
@app.route("/subtract")
def subtract_numbers():
    """A simple function to subtract 2 numbers"""
    input_1 = int(request.args["input_1"])
    input_2 = int(request.args["input_2"])

    subtraction_result = {
        "input_1": input_1,
        "input_2": input_2,
        "difference": (input_1 - input_2)
    }

    return subtraction_result


# multiply info
@app.route("/multiply")
def multiply_numbers():
    """A function to multiply 2 numbers"""
    input_1 = int(request.args["input_1"])
    input_2 = int(request.args["input_2"])

    multiplication_result = {
        "input_1": input_1,
        "input_2": input_2,
        "product": (input_1 * input_2)
    }

    return multiplication_result


# divide info
@app.route("/divide")
def divide_numbers():
    """A function to divide 2 numbers"""
    input_1 = int(request.args["input_1"])
    input_2 = int(request.args["input_2"])

    division_result = {
        "input_1": input_1,
        "input_2": input_2,
        "factor": (input_1 / input_2)
        if input_2 != 0
        else "Not divisible by zero!"  # fixed the divisible by zero
    }

    return division_result


# modulo info
@app.route("/modulo")
def modulo_of_numbers():
    """A function to find the modulo given 2 numbers"""
    input_1 = int(request.args["input_1"])
    input_2 = int(request.args["input_2"])

    modulo_result = {
        "input_1": input_1,
        "input_2": input_2,
        "modulo": (input_1 % input_2)
    }

    return modulo_result


# math_exponent info
@app.route("/math_exponent")
def math_exponent():
    """A function to find the exponent given 2 numbers"""
    input_1 = int(request.args["input_1"])
    input_2 = int(request.args["input_2"])

    exponent_result = {
        "input_1": input_1,
        "input_2": input_2,
        "math_exponent": (input_1 ** input_2)
    }

    return exponent_result


# natural_log info
@app.route("/natural_log")
def natural_log():
    """A function to find the logarithm of a number, given the number and the base"""
    input_1 = int(request.args["input_1"])
    base = int(request.args["base"])

    natural_log_result = {
        "input_1": input_1,
        "base": base,
        "natural_log_result": log(input_1, base)
    }

    return natural_log_result


if __name__ == "___main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", action="store", default="5000")
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=int(args.port))
