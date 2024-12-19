numbers = []
for i in range(10):
    n = float(input(f"Enter number {i+1}: "))
    numbers.append(n)

total_sum = sum(numbers)
print(f"Sum of the numbers: {total_sum}")
