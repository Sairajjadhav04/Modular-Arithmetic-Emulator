import math
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True
def rsa_solver(p, q, e, message):
    steps = []
    # Step 1: Given values
    steps.append({
        "title": "Step 1: Given Values",
        "details": [
            f"p = {p}",
            f"q = {q}",
            f"e = {e}",
            f"Message M = {message}"
        ]
    })
    # Step 2: Prime verification
    if not is_prime(p) or not is_prime(q):
        raise ValueError("p and q must be prime numbers.")

    if p == q:
        raise ValueError("p and q must be different.")

    steps.append({
        "title": "Step 2: Prime Number Verification",
        "details": [
            f"{p} is a prime number.",
            f"{q} is a prime number.",
            "Both numbers are valid."
        ]
    })
    # Step 3: Calculate n
    n = p * q
    steps.append({
        "title": "Step 3: Calculate n",
        "details": [
            "Formula: n = p × q",
            f"n = {p} × {q}",
            f"n = {n}"
        ]
    })
    # Step 4: Calculate phi
    phi = (p - 1) * (q - 1)
    steps.append({
        "title": "Step 4: Calculate Euler's Totient",
        "details": [
            "Formula: φ(n) = (p-1)(q-1)",
            f"φ(n) = ({p}-1)({q}-1)",
            f"φ(n) = {phi}"
        ]
    })
    # Step 5: Verify e
    if e <= 1 or e >= phi:
        raise ValueError("e must satisfy 1 < e < phi(n).")

    if math.gcd(e, phi) != 1:
        raise ValueError("gcd(e, phi) must be 1.")

    steps.append({
        "title": "Step 5: Verify Public Exponent",
        "details": [
            f"e = {e}",
            f"gcd({e}, {phi}) = 1",
            "Therefore, e is valid."
        ]
    })
    # Step 6: Extended Euclidean Algorithm
    old_r, r = phi, e
    old_s, s = 1, 0
    old_t, t = 0, 1
    euclid_steps = []

    while r != 0:
        quotient = old_r // r

        euclid_steps.append(
            f"{old_r} = {quotient} × {r} + {old_r % r}"
        )

        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    d = old_t % phi

    euclid_steps.append(
        f"Therefore, d = {old_t} mod {phi} = {d}"
    )

    steps.append({
        "title": "Step 6: Calculate Private Key",
        "details": [
            "Using Extended Euclidean Algorithm:",
            *euclid_steps,
            f"Private exponent d = {d}"
        ]
    })

    # Step 7: Validate message
    if message < 0 or message >= n:
        raise ValueError("Message must satisfy 0 <= M < n.")

    # Step 8: Encryption
    ciphertext = pow(message, e, n)

    steps.append({
        "title": "Step 7: Encryption",
        "details": [
            "Formula: C = M^e mod n",
            f"C = {message}^{e} mod {n}",
            f"C = {pow(message, e)} mod {n}",
            f"Encrypted message C = {ciphertext}"
        ]
    })

    # Step 9: Decryption with intermediate calculations
    power_steps = []
    base = ciphertext
    exponent = d
    result = 1
    current_power = 0
    power_values = []

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % n

        power_steps.append(
            f"Exponent = {exponent}, base = {base}, result = {result}"
        )

        base = (base * base) % n
        exponent //= 2

    decrypted = result

    steps.append({
        "title": "Step 8: Decryption",
        "details": [
            "Formula: M = C^d mod n",
            f"M = {ciphertext}^{d} mod {n}",
            *power_steps,
            f"Decrypted message = {decrypted}"
        ]
    })

    # Step 10: Final verification
    steps.append({
        "title": "Step 9: Final Verification",
        "details": [
            f"Original Message = {message}",
            f"Decrypted Message = {decrypted}",
            "RSA encryption and decryption successful."
            if message == decrypted
            else "RSA verification failed."
        ]
    })

    return {
        "n": n,
        "phi": phi,
        "public_key": (e, n),
        "private_key": (d, n),
        "ciphertext": ciphertext,
        "decrypted": decrypted,
        "steps": steps
    }
