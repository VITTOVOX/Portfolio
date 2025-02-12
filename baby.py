#We are Making a age verification program to check the users age
# If the user is below 18 -  we most get false - above 18 we most get true
# Our below must both print difference Responses 

#STEP 1  import date and time

from datetime import datetime

#STEP 2 put a variable to hold todays date and time

current_year = datetime.now().year

#STEP 3 ask the user for their date of birth.

birth_year = int(input("Please Enter your Date of birth:"))

#STEP 4 now we subtract the current date to the date that was entered

age = current_year - birth_year

#STEP 5 now we put in boolean

verification = age >= 18

#STEP 6 boolean will take effect, now we put in IF and ELSE statements to respond to our boolean

if verification:
    print("Congrats! You are old enough.")
else:
    print("DENIED")