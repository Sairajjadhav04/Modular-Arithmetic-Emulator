from flask import Flask, render_template, request 
from calculations import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate',methods=['POST'])
def calculate():
    try :
        a = int(request.form['a'])
        b = int(request.form['b'])
        m = int(request.form['m'])
        operation = request.form['operation']   
        if m <= 0:
            raise ValueError("Modulus must be positive.")
        if operation == "addition":
            result = add_modulo(a, b, m)
        elif operation == "subtraction":
            result = subtract_modulo(a, b, m)
        elif operation == "multiplication":
            result = multiply_modulo(a, b, m)
        elif operation == "division":
            result = divide_modulo(a, b, m)
        elif operation == "modulo":
            result = modulo(a, b)
        elif operation == "gcd":
            result = gcd(a, b)
        else:
            raise ValueError("Invalid operation.")
        return render_template(
            "index.html",
            result=result,
            a=a,
            b=b,
            m=m,
            operation=operation
        )
    except (ValueError, ZeroDivisionError) as error:
        return render_template(
            "index.html",
            error=str(error)
        )
if __name__ == "__main__":
    app.run(debug=True)
