sandwichOrders = ["ham", "pastrami","turkey", "blt", "pastrami"]
finishedSandwiches = []

while "pastrami" in sandwichOrders:
    sandwichOrders.remove("pastrami")

while sandwichOrders:
    userSandwich = sandwichOrders.pop()
    print("I made your " + userSandwich)
    finishedSandwiches.append(userSandwich)

print("\nThese are your finished sandwiches")

for finished in finishedSandwiches:
    print(finished)