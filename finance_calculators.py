#We are making a finance calculator 

#import math and what kind of calculator is needed

import math 
def main_menu():
  while True:
        print("\n--- Financial Calculator ---")
        print("1. Investment")
        print("2. Bond")
        print("3. Exit")

        choice = input("Please enter the number of your choice: ")

        if choice == '1':
            investment()
        elif choice == '2':
            bond()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

#We add investment branch to calulator if the user chooses investment

def investment():
    print("\n--- investment calculator ---")
    principal = float(input("Enter the amount you want to invest: "))
    rate = float(input("Enter annual interest rate (as a percentage): "))
    time = float(input("Enter the number of years you plan to invest: "))
    interest_type = float(input("Do yuou want a simple or compound interest")).lower()
#Add calulations

    if interest_type == 'simple':
        amount = principal * (1 + (rate / 100) * time)
        print(f"Your total investment value with simple interest: {amount:.2f}")
    elif interest_type == 'compound':
        amount = principal * math.pow((1 + (rate / 100)), time)
        print(f"Your total investment value with compound interest: {amount:.2f}")
    else:
        print("Invalid interest type. Please choose 'simple' or 'compound'.")

#We add bond branch to calulator is the user chooses bond 


def bond():
    print("\n--- Bond Repayment Calculator ---")
    house_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
    months = int(input("Enter the number of months to repay the bond: "))

#Add calculations
    monthly_interest = (interest_rate / 100) / 12
    repayment = (monthly_interest * house_value) / (1 - math.pow((1 + monthly_interest), -months))
    
    print(f"Your monthly bond repayment amount: {repayment:.2f}")

main_menu()


