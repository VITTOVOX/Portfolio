# BMI Calculator 
#Step 1 we get the users input 

weight = float(input("Weight Please (kg): "))
height = float(input("Height Please (m): "))

#step 2 we insert  the formula to calulate the user BMI

bmi = weight / (height * height) 
print(bmi)

#step 3 next we insert if,else,elif statements

if bmi > 30:
    print("OBESE")
elif 25 <= bmi <29:
    print("OVERWEIGHT")
elif bmi > 18.5:
    print("NORMAL")
elif bmi < 18.5:
    print("UNDERWEIGHT")



