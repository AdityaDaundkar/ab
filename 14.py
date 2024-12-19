from area_module import area_of_triangle, area_of_square, area_of_rectangle, area_of_circle

print("Choose an option:")
print("1. Area of Triangle\n2. Area of Square\n3. Area of Rectangle\n4. Area of Circle")
choice = int(input("Enter your choice: "))

if choice == 1:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print(f"Area of Triangle: {area_of_triangle(base, height)}")
elif choice == 2:
    side = float(input("Enter side: "))
    print(f"Area of Square: {area_of_square(side)}")
elif choice == 3:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print(f"Area of Rectangle: {area_of_rectangle(length, width)}")
elif choice == 4:
    radius = float(input("Enter radius: "))
    print(f"Area of Circle: {area_of_circle(radius)}")
else:
    print("Invalid choice!")
