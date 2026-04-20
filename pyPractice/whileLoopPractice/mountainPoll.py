responses = {}

#set a flag to indicate that polling is active
pollingActive = True

while pollingActive:
    #prompt for the person's name and response
    userName = input("What is your name? ")
    userResponse = input("Which mountain would you like to climb someday? ")

    #store the response in the dictionary
    responses[userName] = userResponse

    #find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == "no":
        pollingActive = False

#polling is complete. Show the results.
for userName, userResponse in responses.items():
    print(userName + " would like to climb " + userResponse)