def getFormattedName(firstName, lastName, middleName=''):
    if middleName:
        fullName = firstName + " " + middleName + " " + lastName
    else:
        fullName = firstName + " " + lastName
    return fullName.title()

musician = getFormattedName("jimmi", "hendrix")
print(musician)

musician = getFormattedName("lee", "harvey", "oswald")
print(musician)
