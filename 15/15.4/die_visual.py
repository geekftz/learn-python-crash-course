from die import Die

import pygal

# # create a die
# die = Die()
#
# # roll the die a few times, store results in a list
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
#
#
# print(results)
#
# # analysis results
# frequencies = []
#
# for value in range(1, die.num_sides + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
#
# print(frequencies)
#
#
# # Visualize the results
# hist = pygal.Bar()
#
# hist.title = "Results of rolling one D6 1000 times"
# hist.x_labels = ['1', '2', '3', '4', '5', '6']
# hist.x_title = 'Result'
# hist.y_title = 'Frequency of Result'
#
# hist.add('D6', frequencies)
# hist.render_to_file('die_visual.svg')

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []

max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual1.svg')





















