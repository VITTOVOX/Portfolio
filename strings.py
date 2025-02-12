# We are testing the strip function 
#Step 1 one make a variable

hero = "$$$SuperMan$$$"

#Step 2 we use the strip function

hero_text = hero.strip("$")

#Step 3 Now print the Stripped text 

print(f"'{hero}' -> '{hero_text}'")
