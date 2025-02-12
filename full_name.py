#We are now validating the users name. 

#Step 1 ask the user for thier name.
name = input("Enter Name: ").strip()

#Step 2 now we validate if the user did so but if not we display message tell them to enter something .
if len(name) == 0:
    print("You haven’t entered anything. Please enter your full name.")

#Step 3 now one for if the user did so but below 4.

elif len(name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")

#step 4 and now one for above the character limit 25.

elif len(name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

#Step 5 If user entered there full name without error we print a thank you 

else:
    print("Thank you for entering your full name!") 


