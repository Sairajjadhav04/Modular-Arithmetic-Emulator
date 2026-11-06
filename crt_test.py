from crt import chinese_remainder_theorem
remainders = [2, 3, 2]
moduli = [3, 5, 7]
solution = chinese_remainder_theorem(
    remainders, moduli
)
print("Final Answer:", solution["result"])
print("Total Modulus:", solution["modulus"])
print("\nStep-by-Step Solution:")
for step in solution["steps"]:
    print(step)
