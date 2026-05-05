def buildPerson(firstName, lastName, age = ''):
    person = {'first': firstName, 'last': lastName}
    
    if age:
        person['age'] = age

    return person

newPerson = buildPerson("cyrus", "bogzaran", 33)
print (newPerson)

print(newPerson['first'])
