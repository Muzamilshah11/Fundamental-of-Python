# Set:-- app ka sath buhat sari sequence of data kha. Aur uss ma jo Unique Value hoti kha. Woo utta ka muji Return karta kha.
# syntax: {'a','b','c','d','a','e','a'}
checkset = {'a','b','c','d','a','e','a'}
print(type(checkset))
check = {} # set or dictionary
print(type(check)) # Empty Dictionary not a set

# Creating a simple program 
db = [];# Creating empty list
while True:
    print("Press 'X' for Exit ")
    name =  input("Enter your name:-- ");
    fname = input("Enter your Father name:-- ");
    r={} # Creating Dictionary
    if name !='x' or fname !='x':
        r['name'] = name
        r['fname'] = fname
        db.append(r)
    else:
        print(db);
        break