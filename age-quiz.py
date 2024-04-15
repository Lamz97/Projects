age = int(input("Please input your age")) # This asks this user to input their age

if age > 100:
    print("Sorry, you're dead.") # If the user is over the age of 100 it will print out this message
elif age >= 65:
    print("Enjoy your retirement!") # If the user is 65 or older it will print out this message
elif age >= 40:
    print("You're over the hill.") # If the user is 40 or older it will print out this message
elif age == 21:
    print("Congrats on your 21st!") # If the user is 21 it will print out this message
elif age < 13:
    print("You qualify for the kiddie discount.") # If the user is younger than 13 it will print out this message
else:
    print("Age is but a number.") # If user inputs any other age not in range it will print out this message