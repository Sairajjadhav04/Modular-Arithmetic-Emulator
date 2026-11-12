from flask import Flask, render_template, request
from calculations import *
from crt import *
from euler import euler_theorem
from fermat import fermat_little_theorem
from rsa import rsa_solver
app = Flask(__name__)
# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')


# MODULAR ARITHMETIC
@app.route('/calculate', methods=['POST'])
def calculate():
    a = request.form.get('a', '')
    b = request.form.get('b', '')
    m = request.form.get('m', '')
    operation = request.form.get('operation', '')

    try:
        a, b, m = int(a), int(b), int(m)

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
            steps=[],
            a=a,
            b=b,
            m=m,
            operation=operation
        )

    except (ValueError, ZeroDivisionError, KeyError) as error:
        return render_template(
            "index.html",
            error=str(error),
            a=a, b=b, m=m,
            operation=operation
        )


# CHINESE REMAINDER THEOREM
@app.route('/crt', methods=['GET', 'POST'])
def crt_solver():

    if request.method == 'POST':
        remainder_input = request.form.get('remainders', '')
        moduli_input = request.form.get('moduli', '')

        try:
            remainders = [
                int(x.strip())
                for x in remainder_input.split(',')
            ]

            moduli = [
                int(x.strip())
                for x in moduli_input.split(',')
            ]

            solution = chinese_remainder_theorem(
                remainders, moduli
            )

            return render_template(
                'crt.html',
                solution=solution,
                result=solution['result'],
                modulus=solution['modulus'],
                steps=solution['steps'],
                remainder_input=remainder_input,
                moduli_input=moduli_input
            )

        except (ValueError, TypeError, KeyError, ZeroDivisionError) as error:
            return render_template(
                'crt.html',
                error=str(error),
                remainder_input=remainder_input,
                moduli_input=moduli_input
            )

    return render_template('crt.html')


# EULER'S TOTIENT THEOREM
@app.route('/euler', methods=['GET', 'POST'])
def euler_solver():

    if request.method == 'POST':
        a = request.form.get('a', '')
        n = request.form.get('n', '')

        try:
            a, n = int(a), int(n)

            solution = euler_theorem(a, n)

            return render_template(
                'euler.html',
                solution=solution,
                result=solution['result'],
                steps=solution['steps'],
                a=a,
                n=n
            )

        except (ValueError, TypeError, KeyError, ZeroDivisionError) as error:
            return render_template(
                'euler.html',
                error=str(error),
                a=a,
                n=n
            )

    return render_template('euler.html')


# FERMAT'S LITTLE THEOREM
@app.route('/fermat', methods=['GET', 'POST'])
def fermat_solver():

    if request.method == 'POST':
        a = request.form.get('a', '')
        p = request.form.get('p', '')

        try:
            a, p = int(a), int(p)

            solution = fermat_little_theorem(a, p)

            return render_template(
                'fermat.html',
                solution=solution,
                result=solution['result'],
                steps=solution['steps'],
                a=a,
                p=p
            )

        except (ValueError, TypeError, KeyError, ZeroDivisionError) as error:
            return render_template(
                'fermat.html',
                error=str(error),
                a=a,
                p=p
            )
    return render_template('fermat.html')  
#RSA Algorithm
@app.route("/rsa", methods=["GET", "POST"])
def rsa():
    result = None
    error = None
    if request.method == "POST":
        try:
            p = int(request.form["p"])
            q = int(request.form["q"])
            e = int(request.form["e"])
            message = int(request.form["message"])
            result = rsa_solver(p, q, e, message)
        except ValueError as ex:
            error = str(ex)
    return render_template(
        "rsa.html",
        result=result,
        error=error
    ) 
if __name__ == '__main__':
    app.run(debug=True)
