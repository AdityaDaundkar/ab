import random

n = int(input("Enter how many random numbers you want: "))
random_numbers = [random.randint(1, 20) for _ in range(n)]

print("Random numbers:", random_numbers)
