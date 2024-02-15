#write a program to accept lenght and breath of a rectangle and calculate and display area and perimentre of rectangle

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print(f"Area: {area}, Perimeter: {perimeter}")