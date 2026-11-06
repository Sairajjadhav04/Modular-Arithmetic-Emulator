def modulo (a, n):
    return a % n

def add_modulo(a, b, n):
    return (a + b) % n

def subtract_modulo(a, b, n):
    return (a - b) % n

def multiply_modulo(a, b, n):
    return (a * b) % n

def divide_modulo(a, b, n):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    # Find the modular inverse of b modulo n
    b_inv = pow(b, -1, n)
    return (a * b_inv) % n

def power_modulo(a, b, n):
    return pow(a, b, n)

def gcd(a, b):
    while b!= 0:
        a, b = b, a % b
    return a