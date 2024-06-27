#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:text>")
def print_string(text="a string"):
    print(text)
    return f"{text}"

@app.route("/count/<int:number>")
def count(number):
    numbers ='\n'.join(str(i) for i in range(number))
    return f"{numbers}\n"

@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):
       number_1 = int(num1)
       number_2 = int(num2)
       if operation == "+":
        result = number_1 + number_2
       elif operation == "-":
        result = number_1 - number_2
       elif operation == "*":
        result = number_1 * number_2
       elif operation == "div":
        result = number_1 / number_2
       elif operation == "%":
        result = number_1 % number_2
       else:
        return "Invalid operation. Please use one of: +, -, *, div, %"
       
       return f"{result}"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
