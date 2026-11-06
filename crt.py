from math import prod,gcd
def chinese_remainder_theorem(remainders, moduli):
    if len(moduli) < 2:
        raise ValueError("Enter at least two congruences.")
    if any(m <= 1 for m in moduli):
        raise ValueError("Each modulus must be greater than 1.")
    # Check pairwise coprimality
    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if gcd(moduli[i], moduli[j]) != 1:
                raise ValueError(
                    "Moduli must be pairwise coprime."
                )
    steps = []
    # Calculate product of all moduli
    M = prod(moduli)
    steps.append(f"Step 1: Calculate M = {M}")
    result = 0
    # Calculate individual terms
    for i in range(len(moduli)):
        mi = moduli[i]
        ai = remainders[i]
        Mi = M // mi
        # Modular inverse
        yi = pow(Mi, -1, mi)
        term = ai * Mi * yi
        steps.append(f"Step 2.{i+1}: M{i+1} = {Mi}")
        steps.append(f"Step 2.{i+1}: Inverse of {Mi} mod {mi} = {yi}")
        steps.append(f"Step 2.{i+1}: Term = {ai} * {Mi} * {yi} = {term}")
        result += term
    # Calculate final answer
    x = result % M
    steps.append(f"Step 3: Add all terms = {result}")
    steps.append(f"Step 4: x = {result} mod {M} = {x}")
    # Verification
    steps.append("Step 5: Verification")
    for i in range(len(moduli)):
        check = x % moduli[i]
        steps.append(
            f"{x} mod {moduli[i]} = {check}"
        )
    return {
        "result": x,
        "modulus": M,
        "steps": steps
    }
