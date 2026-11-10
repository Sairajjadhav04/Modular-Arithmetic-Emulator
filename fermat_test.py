from fermat import is_prime, fermat_little_theorem
print("Prime Check:", is_prime(5))
answer = fermat_little_theorem(2, 5)
for step in answer["steps"]:
    print(step)