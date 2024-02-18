import json


filename = '/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.4/numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
