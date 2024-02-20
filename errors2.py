# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #SyntaxError as the varibale is not defined correctly, missing ""
animal_type = "cub"
number_of_teeth = int("16") #SyntaxError as the varibale is not converted into an int

full_spec = "This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" #SyntaxError and LogicalError as the variable have not been put in the correct logical order for the sentence to make sense

print("This is a " + animal + ". It is a " + animal_type + " and it has " + str(number_of_teeth) + " teeth.") #SyntaxError and LogicalError as the print function is missing the brackets and print function was used to print full spec variable 

