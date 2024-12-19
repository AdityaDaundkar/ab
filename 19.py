my_dict = {}
n = int(input("Enter number of key-value pairs: "))

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

check_key = input("Enter the key to check: ")

if check_key in my_dict:
    print(f"Key '{check_key}' exists with value '{my_dict[check_key]}'.")
else:
    print(f"Key '{check_key}' does not exist.")
