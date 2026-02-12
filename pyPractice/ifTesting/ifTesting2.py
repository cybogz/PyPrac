age = 20

if age >= 18:
    print("You are old enough to vote")
else:
    print("You are not old enough to vote")
    yearsTillVoting = 18-age
    print("You need " + str(yearsTillVoting) + " years until you can vote")

if age < 4:
    print("Admission is free")
elif age > 18:
    print("You must pay $10")
else:
    print("You must pay $5")