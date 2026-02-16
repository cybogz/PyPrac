currentUsers = ["cybogz", "chivajavy", "admin", "stevenator", "jermainiamx"]
newUsers = ["gallo", "CYBOGZ", "razor"]

for newUser in newUsers:
    if newUser.lower() in currentUsers:
        print("This username " + newUser.lower() + " has already been used. Please enter a new username")
    else:
        print("You username is available")
