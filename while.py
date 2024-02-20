numbers = []

while True : 
    num = int(input("Please enter a number ")) #while loop to continuously ask the user to enter a number
    if num == -1: 
        break #if number entered = -1 then the program stops asking user for an input
    numbers.append(num)
    if numbers:
        average = str(sum(numbers)/len(numbers)) #this calculates the avergae of the numbers entered so far
        print("Average of the entered numbers: " + average)
    else:
        print("No numbers entered.")