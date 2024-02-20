# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #SyntaxError because print function was missing brackets
print("\n") #SyntaxError because print function is missing brackets and indentation was made where not needed

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" #SynatxError because the variable was not correctly defined "==" instead of "=", "24 years old" instead of "24" and indentation was made where not needed
age = int(age_Str) #SyntaxError because indentation was made where not needed
print("I'm " + str(age)+ " years old.") #SyntaxError because indentation was made where not needed and incorrect variable used and age was not converted back into a string

    # Variables declaring additional years and printing the total years of age
years_from_now = "3.5" #SyntaxError and LogicalError because indentation was made where not needed and variable should be "3.5" to get  the correct answer
total_years = age + float(years_from_now) #SyntaxError because indentation was made where not needed and "years from now" was not converted into a float

print("The total number of years: " + str(total_years)) #SyntaxError because print function was missing brackets and incorrect variable for total years was stated

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 #SyntaxError becuase varibale total_years was not correctly defined 
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") #SyntaxError because print function was missing brackets and variable total_months was  not converted into a str

#HINT, 330 months is the correct answer

