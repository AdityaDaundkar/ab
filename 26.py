source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

with open(source_file, "r") as source:
    content = source.read()

with open(destination_file, "a") as destination:
    destination.write(content)

print("Content appended successfully!")
