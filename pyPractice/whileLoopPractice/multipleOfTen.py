numberInput = input("Please enter a number and i will tell you if it is a multiple of 10: ")
numberInput = int(numberInput)

if numberInput % 10 == 0:
    print("This number is a multiple of 10")
else:
    print("This is not a multiple of 10")