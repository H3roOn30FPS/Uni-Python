#Geometrical calculator that calculates both area and circumference (or perimeter) 
# for squares, circles, trapezoids, and right triangles (in this order)
import math

def square():
    side = float(input("Enter side (a): "))
    area = side ** 2
    perimeter = 4 * side
    print(f"Square area (S): {area:.2f}")
    print(f"Square perimeter (P): {perimeter:.2f}\n")

def circle():
    radius = float(input("Enter the radius (r): "))
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    print(f"Circle area (S): {area:.2f}")
    print(f"Circle circumference (C): {circumference:.2f}\n")

def trapezoid():
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    h = float(input("Enter the height (h): "))
    side1 = float(input("Enter side c: "))
    side2 = float(input("Enter side d: "))
    area = ((a + b) / 2) * h
    perimeter = a + b + side1 + side2
    print(f"Trapezoid area(S): {area:.2f}")
    print(f"Trapezoid perimeter (P): {perimeter:.2f}\n")

def right_triangle():
    base = float(input("Enter side a: "))
    height = float(input("Enter side b: "))
    hypotenuse = math.sqrt(base**2 + height**2)
    area = 0.5 * base * height
    perimeter = base + height + hypotenuse
    print(f"Right triangle area (S): {area:.2f}")
    print(f"Right triangle perimeter (P): {perimeter:.2f}\n")

print(
"\n---    Geometrical calculator   ---\n"
"---  for finding area and perimeter of set shapes ---\n\n"
"Please enter a corespoding number: \n"
"1 - Operations with Squares;\n" 
"2 - Operations with Circles;\n" 
"3 - Operations with Trapezoids;\n" 
"4 - Operations with Right Triangles;\n" 
"0 - Exit.\n")

while True:
        user_input_option = input("Pick a number: ")
        if user_input_option in ["0", "1", "2", "3", "4"]:
            break
        else:
            print("Invalid input.")

if user_input_option == "1":
    square()
elif user_input_option == "2":
    circle()
elif user_input_option == "3":
    trapezoid()
elif user_input_option == "4":
        right_triangle()
elif user_input_option == "0":
    print("Bye!")