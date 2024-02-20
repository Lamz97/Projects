swimming = float(input("Please input total time taken for swimming"))
cycling = float(input("Please input total time taken for cycling"))
running = float(input("Please input total time taken for running"))
triathlon = (swimming + cycling + running)

print("Total time taken to complete Triathlon is " + str(triathlon) + " minutes.")

if triathlon >= 111: 
    print("No award won")
elif (triathlon <= 110) and (triathlon >= 106):
    print("Award won is Provinical Scroll")
elif (triathlon <= 105) and (triathlon >= 101): 
    print("Award won is Provincial Half Colours")
else: 
    print("Award won is Provincial Colours")
    

