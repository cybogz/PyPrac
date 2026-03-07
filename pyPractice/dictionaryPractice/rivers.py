rivers = {'nile': 'egypt',
          'mississippi': 'usa',
          'amazon': 'brazil'}

for keys, value in rivers.items():
    print("The " + keys.title() + " runs through " + value.title())

for river in rivers.keys():
    print(river)

print("\n")

for country in rivers.values():
    print(country) 