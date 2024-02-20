names = []
DOB = []
n = 1
m = 1
file = open("DOB.txt", "r") # Reads the data in the file
data = file.readlines() 

for line in data: 
    parts = line.split() # Splits the lines into multiple pieces
    names.append(parts[0] + " " + parts[1]) # Adds first two pieces together, so both first name and last name
    DOB.append(parts[2] + " " + parts[3] + " " + parts[4]) # Adds the last pieces of the line together so the DOB


print("Name") # Prints each name on a seperate line
for i in names: 
    print("\t" + str(n) + ".   " + i)
    n += 1

print("Birthdate") # Prints each DOB on a seperate line
for j in DOB:
    print("\t" + str(m) + ".   " + j)
    m += 1

file.close()