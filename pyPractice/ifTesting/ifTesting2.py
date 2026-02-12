age = 17

if age >= 18:
    print("You are old enough to vote")
else:
    print("You are not old enough to vote")
    yearsTillVoting = 18-age
    print("You need " + str(yearsTillVoting) + " years until you can vote")

if age < 4:
    price = 0
elif age < 18:
    price = 10
elif age < 65:
    price = 15
elif age >= 65:
    price = 5
print("Your admission price is: $" + str(price))