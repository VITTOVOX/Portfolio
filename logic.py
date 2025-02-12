# This program should calculate the average of three numbers, but it has a logical error.

num1 = 10
num2 = 20
num3 = 30

# Logical error: It should divide by 3, but it divides by 2 instead
average = (num1 + num2 + num3) / 2  

print(f"The average of the numbers is: {average}")
# Suppose we want to calculate the area of a rectangle
width = 5
height = 10

# Logical error: It should be width * height, but we mistakenly add them!
area = width + height  

print(f"The area of the rectangle is: {area}")

# This program should print numbers from 1 to 5, but there's an error
for i in range(1, 5):  # Logical error: range(1, 5) only goes up to 4
    print(i)