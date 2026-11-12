# Modular Arithmetic Emulator

**An Interactive Web-Based Emulator for Discrete Mathematics and Cryptography**

## About the Project

Modular Arithmetic Emulator is a Python and Flask-based educational web application developed to help students understand and solve problems related to Discrete Mathematics and Cryptography.

The application provides interactive mathematical calculators and solvers with step-by-step explanations, helping students understand the logic behind different mathematical operations and cryptographic algorithms.

## Features

The project consists of five major modules:

### 1. Basic Modular Arithmetic
- Modular Addition
- Modular Subtraction
- Modular Multiplication
- Modular Division
- Modulo Operation
- Greatest Common Divisor (GCD)

### 2. Chinese Remainder Theorem (CRT)
- Solve simultaneous congruence equations.
- Calculate modular inverses.
- Display step-by-step mathematical solutions.

### 3. Euler's Theorem
- Calculate modular exponentiation.
- Apply Euler's Totient Function.
- Display mathematical calculations step by step.

### 4. Fermat's Little Theorem
- Solve modular arithmetic problems.
- Apply Fermat's Little Theorem.
- Display step-by-step solutions.

### 5. RSA Algorithm Solver
- Validate prime numbers.
- Calculate RSA modulus (n).
- Calculate Euler's Totient.
- Generate public and private keys.
- Encrypt messages.
- Decrypt messages.
- Display detailed mathematical calculations.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| HTML5 | Webpage structure |
| CSS3 | User interface styling |

## Project Structure

```text
Modular-Arithmetic-Emulator/
│
├── app.py
├── calculations.py
├── crt.py
├── euler.py
├── fermat.py
├── rsa.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── crt.html
│   ├── euler.html
│   ├── fermat.html
│   └── rsa.html
│
└── static/
    └── css/
        └── style.css
```

*Note: The structure above represents the expected project organization. Adjust filenames according to your actual files.*

## Installation and Setup

Follow these steps to run the project on your local machine.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd Modular-Arithmetic-Emulator
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Required Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python app.py
```

### Step 6: Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## How to Use

1. Launch the application.
2. Select the required mathematical module from the navigation bar.
3. Enter the required numerical inputs.
4. Submit the calculation.
5. View the generated results.
6. Understand the mathematical solution through the displayed steps.

## Future Enhancements

- Interactive quizzes and practice exercises.
- Downloadable PDF solutions.
- Improved mathematical equation formatting.
- Additional cryptographic algorithms.
- Responsive user interface improvements.
- More detailed mathematical explanations.

## Security Disclaimer

The RSA implementation is designed for educational and demonstration purposes only. It uses textbook RSA and is not suitable for real-world secure communication. Production RSA requires secure padding such as OAEP and appropriately sized keys.

## Project Information

**Project Name:** Modular Arithmetic Emulator

**Project Domain:** Discrete Mathematics and Cryptography

**Project Type:** Educational Web Application

**Backend:** Python and Flask

**Frontend:** HTML5 and CSS3

---

**Modular Arithmetic Emulator – Simplifying Discrete Mathematics and Cryptography Through Interactive Learning.**