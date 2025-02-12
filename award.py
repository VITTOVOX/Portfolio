#Creating a award logical progam for triathlon
#Award brackets 
"""
Qualifying Criteria                               |   Time Range       | Award
Within the qualifying time                        |   0 - 100 minutes  | Provincial colours
5 minutes off from the qualifyong time            |   101 - 105 minutes| Provincial half colours
10 minutes off from the qualifying time           |   106 - 110 minutes| Provincial scroll
More than 10 minutes off from the qualifying time |   111 + minutes    | No award


"""
#Step 1 we get the user input for their time 

swimming =int(input("Swimming time: ")) 

cycling = int(input("Cycling time: "))

running =int(input("Running time: "))

#step 2  we add formula 

total_time = swimming + cycling + running

#Step 3 we now determine there award
if total_time <= 100:
    award = "Provincial colours"
elif total_time >= 101 and total_time <= 105:
    award = "Provincial half colours"
elif total_time >= 106 and total_time <= 110:
    award = "Provincial scroll"
else:
    award = "No award"

# Step 4: Display the result

print(f"Total time: {total_time} minutes")
print(f"Award received: {award}")

