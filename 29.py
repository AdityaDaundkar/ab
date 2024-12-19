try:
    num = int(input("Enter a number: "))
    print("Square of the number:", num ** 2)
except ValueError:
    print("Invalid input! Please enter an integer.")
