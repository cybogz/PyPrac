def describe_city(city, country = "Japan"):
    print(city + " is in " + country)

describe_city("tokyo")
describe_city("san diego", "usa")
describe_city("tijuana", country = "mexico")