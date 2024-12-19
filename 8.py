subjects = int(input("Enter the number of subjects: "))
total_marks = 0

for i in range(subjects):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    total_marks += marks

percentage = (total_marks / (subjects * 100)) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
