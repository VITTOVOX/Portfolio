# We are moking a shopping list with a calculator add to it 
# First we ask user for their input on what they need 

#Step 1 asking user for thier input
product1 = input("Enter the name of the first product: ")
price1 = float(input(f"Enter the price of {product1}: "))

product2 = input("Enter the name of the second product: ")
price2 = float(input(f"Enter the price of {product2}: "))

product3 = input("Enter the name of the third product: ")
price3 = float(input(f"Enter the price of {product3}: "))

#Step 2 Now we sum all of this together 
total_price = price1 + price2 + price3
print(f"\nThe cost of {price1}, {price2}, and {price3} is {total_price}.")

#Step 3 After getting the prices we now round the asnwer 
rounded_price = round( total_price, 2 )
print(f"The rounded price is: R{rounded_price}")