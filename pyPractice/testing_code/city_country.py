def city_country_name(city, country, population=""):
    """Will format a string on city and country of users choosing"""

    if population:
        name = f"{city}, {country} - population {population}"
    else:
        name = f"{city}, {country}"
    return name