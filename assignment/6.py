#wap to accept any interger from the user and calculate and display below
#1.factorial 2.accept another value (ex: b) and calculate and display a^b

import math

# Accept an integer from the user
num = int(input("Enter an integer: "))

# Calculate and display the factorial
print(f"The factorial of {num} is: {math.factorial(num)}")

# Accept another value 'b' from the user
b = int(input("Enter another integer 'b' for power calculation: "))

# Calculate and display the power operation (a^b)
print(f"{num} raised to the power {b} is: {num ** b}")
