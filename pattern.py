rows = 5 #number of rows 
for i in range(0, rows): #For statement for the first half of the pattern 
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1): #For statement for the second half of the pattern
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
