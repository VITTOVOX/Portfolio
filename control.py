#Age verfication with elif statement 

# Step 1: Take the user's age and convert it to an integer
age = int(input("Please enter your age: "))

# Step 2: Check if the user is old enough using if, elif, and else statements
if age < 16:
    print("Sorry, you are not old enough to enter.")
elif 16 <= age < 18:
    print("You are almost there.")
elif age == 18:
    print("You are old enough.")
else:
    print("You are allowed to enter.")