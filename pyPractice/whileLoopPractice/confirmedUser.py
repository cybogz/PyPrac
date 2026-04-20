#start with users that need to be varified and an empty list to hold the confirmed users

unconfirmedUsers = ["billy", "tina", "paul", "toby"]
confirmedUsers = []

#verify each user until there are no more unconfirmed users
#move each verified user into the list of confirmed users

while unconfirmedUsers:
    confirmed = unconfirmedUsers.pop()

    print("Veryifying user: " + confirmed.title())
    confirmedUsers.append(confirmed)

#print the confirmed users

print("\nThe following users have been confirmed")

for user in confirmedUsers:
    print(user.title())