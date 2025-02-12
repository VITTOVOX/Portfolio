#Make a menu 
# PRINT "----- MENU -----"
# PRINT "1. Say Hello"
# PRINT "2. Show Current Date"
# PRINT "3. Exit"
# PRINT "Please enter your choice (1-3):
# Read users choice
# Print users choice      
# I asked My friend for help with this one
while True:
    print("----- MENU -----")
    print("1. Say Hello")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")