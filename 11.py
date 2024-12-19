def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = int(input("Enter the number of Fibonacci terms: "))
print("Fibonacci Series:", [fibonacci_recursive(i) for i in range(n)])
