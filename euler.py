import math
# Step 1: Calculate Euler's Totient Function
def euler_totient(n):
    if n <= 0:
        raise ValueError("n must be positive")
    coprime_numbers = []
    for i in range(1, n + 1):
        if math.gcd(i, n) == 1:
            coprime_numbers.append(i)
    return len(coprime_numbers), coprime_numbers
# Step 2: Apply Euler's Theorem
def euler_theorem(a, n):
    if n <= 1:
        raise ValueError("n must be greater than 1")
    gcd_value = math.gcd(a, n)
    if gcd_value != 1:
        raise ValueError("a and n must be coprime")
    # Calculate Euler Totient
    phi, coprimes = euler_totient(n)
    # Calculate modular exponentiation
    result = pow(a, phi, n)
    # Calculate actual power for smaller examples
    power_value = a ** phi if phi <= 1000 and abs(a) <= 1000 else None
    # Store step-by-step solution
    steps = [
        f"Given: a = {a}, n = {n}",
        f"Step 1: Calculate GCD({a}, {n}) = {gcd_value}",
        "Step 2: Since GCD is 1, Euler's theorem is applicable.",
        f"Step 3: Calculate Euler's Totient Function φ({n}) = {phi}",
        f"Numbers relatively prime to {n}: {', '.join(map(str, coprimes))}",
        f"Step 4: Apply Euler's theorem: {a}^φ({n}) ≡ 1 (mod {n})",
        f"Step 5: Substitute values: {a}^{phi} mod {n}"
    ]
    if power_value is not None:
        steps.append(f"Calculate: {a}^{phi} = {power_value}")
        steps.append(f"Remainder: {power_value} mod {n} = {result}")
    else:
        steps.append(f"Using modular exponentiation, the remainder is {result}")
    steps.append(f"Final Answer: {result}")
    return {
        "a": a,
        "n": n,
        "gcd": gcd_value,
        "phi": phi,
        "coprimes": coprimes,
        "exponent": phi,
        "power_value": power_value,
        "result": result,
        "steps": steps
    }
