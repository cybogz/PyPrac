def greetUser(firstName, lastName):
    """Returning a full name"""
    fullName = firstName + ' ' + lastName
    return fullName.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' to quit at any time)")

    fName = input("First Name: ")
    if fName.lower() == "q":
        break
    
    lName = input("Last Name: ")
    if lName == "q":
        break

    usersFullName = greetUser(fName, lName)
    print("\nHello " + usersFullName)
