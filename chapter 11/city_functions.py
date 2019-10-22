def citi_functions(country, city, population=''):
    if population:
        full_name = city.title() + ", " + country.title() + ' - population ' + population
    else:
        full_name = city.title() + ", " + country.title()

    return full_name
