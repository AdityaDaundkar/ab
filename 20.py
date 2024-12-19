my_dict = {}
n = int(input("Enter number of key-value pairs: "))

for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    my_dict[key] = value

total = sum(my_dict.values())

print("Sum of all values in the dictionary:", total)
