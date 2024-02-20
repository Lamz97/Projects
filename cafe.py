menu = ['cinnamon bun', 'coffee', 'cookie', 'cake'] #List of items in the menu
stock = {'cinnamon bun': 5, 'coffee': 4, 'cookie': 7, 'cake': 2} #dictionary showing amount of each item in the menu
price = {'cinnamon bun': 1.50, 'coffee': 3, 'cookie': 1.50, 'cake': 2} #dictionary showing the price of each item in the menu

item_value1 = int(stock['cinnamon bun']) * float(price['cinnamon bun']) #calculates the total stock value for cinnamon buns
item_value2 = int(stock['coffee']) * float(price['coffee']) #calculates the total stock value for coffee
item_value3 = int(stock['cookie']) * float(price['cookie']) #calculates the total stock value for cookie
item_value4 = int(stock['cake']) * float(price['cake']) #calculates the total stock value for cake

total_stock = item_value1 + item_value2 + item_value3 + item_value4 #calculates the total stock value for all items

print("The total stock value at the cafe is £" + str(total_stock)) #prints the total stock value 
