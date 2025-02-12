#We are making a program for a courier company 

# Get user input for distance
distance = float(input("Enter the delivery distance in km: "))

# Get user choice for freight type
freight = input("Choose freight type (Air/Land): ").strip().lower()
if freight == "air":
    freight_cost = 0.36 * distance
elif freight == "land":
    freight_cost = 0.25 * distance
else:
    print("Invalid freight option selected.")
    freight_cost = 0

# Get user choice for insurance
insurance_type = input("Choose insurance type (Full/Limited): ").strip().lower()
if insurance_type == "full":
    insurance_cost = 50.00
elif insurance_type == "limited":
    insurance_cost = 25.00
else:
    print("Invalid insurance option selected.")
    insurance_cost = 0

# Get user choice for gift cover
gift_cover = input("Do you want gift cover? (Yes/No): ").strip().lower()
if gift_cover == "yes":
    gift_cost = 15.00
elif gift_cover == "no":
    gift_cost = 0.00
else:
    print("Invalid gift option selected.")
    gift_cost = 0

# Get user choice for delivery priority
priority = input("Choose delivery priority (Priority/Standard): ").strip().lower()
if priority == "priority":
    priority_cost = 100.00
elif priority == "standard":
    priority_cost = 20.00
else:
    print("Invalid priority option selected.")
    priority_cost = 0

# Get user choice for parcel type
parcel_type = input("Choose parcel type (Sleeve/Box): ").strip().lower()
if parcel_type == "sleeve":
    parcel_cost = 100.00
elif parcel_type == "box":
    parcel_cost = 150.00
else:
    print("Invalid parcel option selected.")
    parcel_cost = 0

# Calculate total cost
total_cost = freight_cost + insurance_cost + gift_cost + priority_cost + parcel_cost

# Display the total cost
print(f"\nThe total cost of sending the parcel is: R{total_cost:.2f}")