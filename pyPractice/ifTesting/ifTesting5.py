toppingsAvailable = ["pepperoni", "cheese", "bell pepper", "pinapple"]
toppingsRequested = ["pepperoni", "pinapple", "bacon", "cheese"]

for toppings in toppingsRequested:
    if toppings in toppingsAvailable:
        print(toppings + " has been added")
    else:
        print(toppings + " is not available")
print("\nAll toppings have been added to your pizza")