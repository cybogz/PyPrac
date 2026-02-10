pizzas = ["pep", "cheese", "meat lovers", "pinapple"]

myFavPizzas = pizzas[:]

myFavPizzas.append("sardines")

print("This is a list of pizzas\n")
for pizzaList in pizzas:
    print(pizzaList)

print("\nThis is my fav list of pizzas\n")
for myListFavPizzas in myFavPizzas:
    print(myListFavPizzas)