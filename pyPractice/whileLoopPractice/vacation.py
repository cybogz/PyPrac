userInformation = {}
whileLoopFlag = True

while whileLoopFlag:
    userName = input("Hi what is your name? ")
    userResponse = input("If you could visit one place in the world, where would you go? ")

    userInformation[userName] = userResponse

    repeat = input("Would you like another person to respond? yes/no ")
    if repeat == "no":
        whileLoopFlag = False

for userName, userResponse in userInformation.items():
    print(userName + " would really like to visit " + userResponse)