from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """According to the specified country, return the two letter country code used by Pygal"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # if not find the specified country, return None
    return None


print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))
