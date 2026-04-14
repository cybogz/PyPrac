customerMessage = input("Please enter how many people will be in your dinner group: ")
customerMessage = int(customerMessage)

if customerMessage > 8:
    print("Sorry, we do not have an available table for this group size at the moment")
else:
    print("Your table is ready. Follow me to be seated")