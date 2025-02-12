# We create an empty list to store our data
numbers = []

# Add an input block
while True:
    user_input = input("Please enter a number (enter -1 to end): ")

    # End code if user inputs -1
    if user_input == "-1":
        break

    try:
        # Convert input into float and store in our list
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("INVALID INPUT")

# Ensure we don't divide by zero
if numbers:
    total_sum = sum(numbers)
    average = total_sum / len(numbers)  # Compute the average
    print("\nNumbers entered:", numbers)
    print(f"Total sum: {total_sum:.2f}")
    print(f"Average: {average:.2f}")
else:
    print("No valid numbers entered.")