#The following program should give your disposable mnonthly income and monthly savings 

net_income = int(input("Please enter how much your monthly income after tax ")) #Asks user to input their income
expenses = int(input("Please enter your total monthly expenses ")) #Asks user to input their expenses
profit = net_income - expenses #formula to work out the users profit
savings = profit * 0.1 #formula to work out the users savings if they save 10% of their profit
disposable_income = profit + savings #formula to workout the disposable income of the user after expenses and savigns have been taken from the income

print("Based on your income you should be saving £" + str(savings)) #displays the users savigns
print("Based on your savigns your disposable income should be £" + str(disposable_income)) #displays the users disposable income

#The LogicalError is that a "+" has been used to calculate the disposable income instead of the "-" so the expected output will be incorrect.