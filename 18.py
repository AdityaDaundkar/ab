list1 = list(map(int, input("Enter numbers for List 1 (space-separated): ").split()))
list2 = list(map(int, input("Enter numbers for List 2 (space-separated): ").split()))

merged_list = list1 + list2
merged_list.sort()

print("Merged and sorted list:", merged_list)
