from flask import Flask,render_template, request, jsonify
from math import log

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def homePage():
    return render_template('index.html')
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route('/math', methods=['POST'])
def math_operation():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    result = ""

    if operation == "add":
        result = f"The sum of {num1} and {num2} is {num1 + num2}"
    elif operation == "subtract":
        result = f"The result of subtracting {num2} from {num1} is {num1 - num2}"
    elif operation == "multiply":
        result = f"The product of {num1} and {num2} is {num1 * num2}"
    elif operation == "divide":
        if num2 != 0:
            result = f"The result of dividing {num1} by {num2} is {num1 / num2}"
        else:
            result = "Cannot divide by zero"
    elif operation == "log":
        if num1 > 0 and num2 > 1:
            result = f"The logarithm of {num2} to the base {num1} is {round(log(num2, num1), 4)}"
        else:
            result = "Invalid input for logarithm operation"

    return render_template('results.html', result=result)
if __name__=="__main__":
    app.run(host="0.0.0.0")
