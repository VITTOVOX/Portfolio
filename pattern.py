#Row of stars of max of five in the middle
row = 5

#Put in for loop and if an else statements
for i in range(1, row * 2):
    if i <= row:
        print("*" * i) #increase the pattern 
    else:
        print("*" * (2 * row - i)) #and decrease pattern 