toppings = ""

while toppings != "quit":
    toppings = input("Please enter your toppings. Write 'quit' to quit: ")
    if toppings == 'quit':
        break
    else:
        print(toppings + " has been added to your toppings")
