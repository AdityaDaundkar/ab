class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative number entered!")
    print("You entered:", num)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Invalid input! Please enter an integer.")
