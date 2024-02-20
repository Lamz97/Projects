import math

#Below is the information provided to the user to make a decision on the type of calculation they would like to make
print("Investment - To calculate the amount of interest you'll earn on your investment")
print("Bond - To calculate the amount you'll have to pay on a home loan")

#Below is to ask the user to make a selection on the type of calculation based on the information given above to them
selection = str.casefold(input("Please enter which calculation you would like to do, either 'investment' or 'bond': "))

#This if statement is to allow the user to input the values for both investment & bond calculations which will be used to calculate  
if selection == "investment":
    amount = float(input("Please enter how much you are depositing: "))
    interest_rate = float(input("Please enter the interest rate: "))
    amount_of_years = int(input("please enter the number of years you plan to invest: "))
    calculation_type = str.casefold(input("Please enter if you would like 'simple' or 'compound' interest: "))
elif selection == "bond":
    house_value = float(input("Please enter the present value of the house: "))
    interest_rate = float(input("Please enter the interest rate: "))
    amount_of_months = int(input("please enter the number of months you plan to take to repay the bond: "))
    print("You will have to repay £" + str(round((((interest_rate/100)/12) * house_value)/(1 - (1 + ((interest_rate/100)/12))**(-amount_of_months)), 2)) + " each month.")
else: 
    print ("Incorrect selection entered.")

#This if statement is for the users that selected investment as their form of calculation and it calculates simple or compound interest based on their selection
if selection == "investment" and calculation_type == "simple": 
    print("Your investment of £" + str(amount) + " at a simple interest calculation" + " over " + str(amount_of_years) + " years will give you a revenue of £" + str(round(amount * (1 + (interest_rate/100) * amount_of_years), 2)))
elif selection == "investment" and calculation_type == "compound":
    print("Your investment of £" + str(amount) + " at a compound interest calculation" + " over " + str(amount_of_years) + " years will give you a revenue of £" + str(round(amount * math.pow((1 + (interest_rate/100)), amount_of_years), 2)))
elif selection == "bond":
    print(" ")
else:
    print ("Incorrect interest entered.")


