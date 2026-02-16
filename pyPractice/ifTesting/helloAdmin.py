usernames = []

if usernames:
    for users in usernames:
        if users == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + users.title() + " thank you for logging in again")
else:
    print("We need to find some users")

