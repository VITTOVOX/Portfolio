# We are making a simple calculator 
# We ask the user for 3 integers 
#Then we make the code do 4 things with those 3 integers
# We are going to Sum , Minus , Multiply and Devide 

#Users input 
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

#Sum
total_sum = num1 + num2 + num3 
print(f"\nThe sum of {num1}, {num2}, and {num3} is {total_sum}.")

#Minus
result = num1 - num2
print(f"\n Minus {num1}, {num2}  is {result}.")

#Multiply
multiply = num3 * num1 
print(f"\n The multplication of {num3}, {num1}  is {multiply}.")

#Division 
division = num1 + num2 + num3 / num3
print(f"\nThe division of {num1}, {num2}, and {num3} , divided by {num3} is {division}.")