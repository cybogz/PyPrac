userHeight = input("Please enter your height in centimeters: ")

#convert height into an integer
intHeight = int(userHeight)

if intHeight < 152:
    print("You are not tall enough for this ride. Sorry :(")
else:
    print("You can enter this ride")