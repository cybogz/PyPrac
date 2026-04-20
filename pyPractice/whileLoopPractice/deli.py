sandwichOrders = ["ham sandwich", "turkey sandwich", "blt sandwich", "pastrami sandwich"]
finishedSandwiches = []

while sandwichOrders:
    userSandwich = sandwichOrders.pop()
    print("I made your " + userSandwich)
    finishedSandwiches.append(userSandwich)

print("\nThese are your finished sandwiches")

for finished in finishedSandwiches:
    print(finished)