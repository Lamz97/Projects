statement = "Python Program" #original string
length = len(statement) #gets the length of the statement
print(statement) #print original statament

statement2 = " " #empty string

for a in range(0,length,2):
    statement2+=statement[a]
    if a<(length-1):
        statement2+=statement[a+1].upper()

print(statement2) #prints new statement

Statement3 = "this is a python program" #new statement

split = Statement3.split(" ") #splits the string by space
split[1::2] = map(str.upper, split[1::2]) #makes every other word capital
statement4 = " ". join(split) #joins the string back together

print(statement4) #prints new statement 