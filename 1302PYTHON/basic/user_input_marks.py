a = int(input("enter marks of maths = "))
b = int(input("enter marks of science = "))
c = int(input("enter marks of marathi = "))
d = int(input("enter marks of geometry = "))
e = int(input("enter marks of algebra = "))
f = int(input("enter marks of english = "))

total_marks = 600

obtained_marks = a+b+c+d+e+f

print("the total marks is: ", obtained_marks)

percentage = (obtained_marks/total_marks)*100

print("the percentage is : ", percentage)