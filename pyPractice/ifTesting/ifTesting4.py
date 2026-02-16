"""
toppings = ["pepperoni", "green peppers", "cheese", "mushrooms"]

for pizzaToppings in toppings:
    if "green peppers" == pizzaToppings:
        print("We are out of green peppers")
    else:
        print("We are adding: " + pizzaToppings)
print("We have finished adding your toppings")
"""

toppings = []

if toppings:
    for pizzaToppings in toppings:
        print("We are adding: " + pizzaToppings)
    print("We are done with your pizza")
else:
    print("Are you sure you want a plain pizza")