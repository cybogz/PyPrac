prompt = "Please enter your age\n"
prompt += "Write quit to end\n"

usersAge = ""

while usersAge != "quit":
    usersAge = input(prompt)
    
    if usersAge == "quit":
        break
    
    usersAge = int(usersAge)

    if usersAge < 3:
        print("Your movie ticket is free\n")
    elif usersAge <= 12:
        print("Your movie ticket is $10\n")
    else:
        print("Your movie ticket is $15\n")