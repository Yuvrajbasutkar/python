##wap to declare list having n elements. accept elements from user n times [all in int] find sum of them
n = int(input("Enter the number of elements: "))
element_list = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]
sum_of_values = sum(element_list)
print("List of elements:", element_list)
print("Sum of all values:", sum_of_values)