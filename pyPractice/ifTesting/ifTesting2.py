age = 15

if age >= 18:
    print("You are old enough to vote")
else:
    print("You are not old enough to vote")
    yearsTillVoting = 18-age
    print("You need " + str(yearsTillVoting) + " years until you can vote")