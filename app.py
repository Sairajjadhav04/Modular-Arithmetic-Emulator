from flask import Flask, render_template, request 
from calculations import *
from crt import *
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

@app.route("/crt", methods=["GET", "POST"])
def crt_solver():

    if request.method == "POST":

        try:
            remainder_input = request.form["remainders"]
            moduli_input = request.form["moduli"]

            remainders = [
                int(x.strip())
                for x in remainder_input.split(",")
            ]

            moduli = [
                int(x.strip())
                for x in moduli_input.split(",")
            ]

            solution = chinese_remainder_theorem(
                remainders, moduli
            )

            return render_template(
                "crt.html",
                result=solution["result"],
                modulus=solution["modulus"],
                steps=solution["steps"],
                remainder_input=remainder_input,
                moduli_input=moduli_input
            )

        except (ValueError, TypeError) as error:

            return render_template(
                "crt.html",
                error=str(error),
                remainder_input=request.form.get("remainders", ""),
                moduli_input=request.form.get("moduli", "")
            )
    return render_template("crt.html")
if __name__ == "__main__":
    app.run(debug=True)
