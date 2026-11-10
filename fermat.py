import math
# Step 1: Check whether number is prime
def is_prime(p):
    if p <= 1:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True
# Step 2: Apply Fermat's Little Theorem
def fermat_little_theorem(a, p):
    if not is_prime(p):
        raise ValueError("p must be a prime number")
    if a % p == 0:
        raise ValueError("a must not be divisible by p")
    exponent = p - 1
    result = pow(a, exponent, p)
    power_value = a ** exponent if abs(a) <= 1000 and exponent <= 1000 else None
    steps = [
        f"Given: a = {a}, p = {p}",
        f"Step 1: Check whether {p} is prime.",
        f"Step 2: {p} is a prime number.",
        f"Step 3: Check divisibility: {a} mod {p} = {a % p}",
        "Step 4: Apply Fermat's Little Theorem:",
        f"{a}^(p-1) ≡ 1 (mod {p})",
        f"Step 5: Substitute values: {a}^{exponent} mod {p}"
    ]
    if power_value is not None:
        steps.append(f"Calculate: {a}^{exponent} = {power_value}")
        steps.append(f"Remainder: {power_value} mod {p} = {result}")
    else:
        steps.append(f"Using modular exponentiation, remainder = {result}")
    steps.append(f"Final Answer: {result}")
    return {
        "a": a,
        "p": p,
        "exponent": exponent,
        "result": result,
        "steps": steps
    }