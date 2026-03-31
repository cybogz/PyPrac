cities = {
    'San Diego':{
    'country':'USA',
    'population':'3 million',
    'fact':"it's a beach city"
    },
    'New York City':{
    'country':'USA',
    'population':'8.5 million',
    'fact':'street photography capital of the world'
    },
    'Tokyo':{
    'country':'Japan',
    'population':'36 million',
    'fact':'they have lemon sours here'
    }
}

for name, information in cities.items():
    print("Here is some information about " + name + ": ")

    countryInfo = information['country']
    populationInfo = information['population']
    factInfo = information['fact']

    print("\tCountry: " + countryInfo)
    print("\tPopulation: " + populationInfo)
    print("\tFact about the city: " + factInfo)

    print()
