sandwichOrders = ["ham", "pastrami", "turkey", "blt", "pastrami"]
finishedSandwiches = []

while sandwichOrders:
    userSandwich = sandwichOrders.pop()
    if userSandwich == "pastrami":
        continue
    print("I made your " + userSandwich)
    finishedSandwiches.append(userSandwich)

print("\nThese are your finished sandwiches")

for finished in finishedSandwiches:
    print(finished)