def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

n = int(input("Enter the number of Fibonacci terms: "))
print("Fibonacci Series:", fibonacci(n))
