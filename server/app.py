from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<name>')
def print_string(name):
    print(name)
    return name

@app.route('/count/<number>')
def count(number):
    number = int(number)
    numbers = '\n'.join(str(i) for i in range(number + 1))
    print(numbers)
    return numbers


@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    num1 = float(num1)
    num2 = float(num2)
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return 'Error: Modulo by zero'
    else:
        return 'Error: Invalid operation'

    result_str = str(result)
    print(result_str)
    return f'Result: {result}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
