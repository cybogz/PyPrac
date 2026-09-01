from city_country import city_country_name

print("press 'q' to quit at any time")

while True:
    city = input("Please enter the city of your choosing: ")
    if city == "q":
        break
    country = input("Please enter the country that the city is in: ")
    if country == "q":
        break
    population = input("Please enter the population of the city or press enter to skip: ")
    if population == "q":
        break

    if population == "":
        print(city_country_name(city, country))
    else:
        print(city_country_name(city, country, population))
