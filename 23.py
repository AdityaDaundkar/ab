class ListOperations:
    def __init__(self):
        self.my_list = []

    def append_element(self, element):
        self.my_list.append(element)

    def delete_element(self, element):
        if element in self.my_list:
            self.my_list.remove(element)
        else:
            print("Element not found!")

    def display_list(self):
        print("List:", self.my_list)

obj = ListOperations()

while True:
    print("\n1. Append\n2. Delete\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        element = int(input("Enter element to append: "))
        obj.append_element(element)
    elif choice == 2:
        element = int(input("Enter element to delete: "))
        obj.delete_element(element)
    elif choice == 3:
        obj.display_list()
    elif choice == 4:
        break
    else:
        print("Invalid choice! Try again.")
