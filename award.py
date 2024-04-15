swimming = float(input("Please input total time taken for swimming")) # This asks the user to input total time taken for swimming
cycling = float(input("Please input total time taken for cycling")) # This asks the user to input total time taken for cycling
running = float(input("Please input total time taken for running")) # This asks the user to input total time taken for running
triathlon = (swimming + cycling + running) # This calculates the triathlon time

print("Total time taken to complete Triathlon is " + str(triathlon) + " minutes.") # This prints out the triathlon time for the user

if triathlon >= 111: 
    print("No award won") # If the triathlon time is >=111 the user will recieve a message 'No award won'
elif (triathlon <= 110) and (triathlon >= 106):
    print("Award won is Provinical Scroll") # If the triathlon time is <=110 & >=106 the user will recieve a message 'Award won is provincial scroll'
elif (triathlon <= 105) and (triathlon >= 101): 
    print("Award won is Provincial Half Colours") # If the triathlon time is <=105 & >=101 the user will recieve a message 'Award won is Provincial Half Colours'
else: 
    print("Award won is Provincial Colours") # If the triathlon time anything else the user will recieve a message 'Award won is Provincial Colours'
    

