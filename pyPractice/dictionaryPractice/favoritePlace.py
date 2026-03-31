favoritePlaces = {'cyrus' : ['san diego', 'new york'],
                  'john' : ['new york', 'tokyo', 'paris'],
                  'chris' : ['la']}

for name, places in favoritePlaces.items():
    print(name + "'s favorite places are: ")

    for place in places:
        print(place)
    
    print()