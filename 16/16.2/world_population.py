import json

from country_codes import get_country_code

import pygal_maps_world.maps
# from pygal.style import RotateStyle
# from pygal.style import LightColorizedStyle
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

# load data to the list

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Create a dictionary containing population size
cc_populations = {}

# print the population of each country in 2010
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        print(country_name, ": " + str(population))

        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
            print(code + ": " + str(population))
        else:
            print('ERROR - ' + country_name)

# according to the population, divide all countries into three groups
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# wm_style = RotateStyle('#336699')
# wm_style = LightColorizedStyle
# wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm_style = RS('#336699', base_style=LCS)
wm = pygal_maps_world.maps.World(wm=pygal_maps_world.maps.World())

wm.title = 'World Population in 2010, by Country'
# wm.add('2010', cc_populations)

wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population.svg')
