from die import Die
import pygal

die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_numsides = die2.num_sides + die1.num_sides
for value in range(2, max_numsides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
values = [value for value in range(2,13)]
hist.x_labels = values
hist.y_title = "Frequency of result"
hist.x_title = "Result"

hist.add('D6+D6', frequencies)
hist.render_to_file('die_visual.svg')


