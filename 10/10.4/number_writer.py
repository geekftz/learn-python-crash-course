import json

numbers = [2, 3, 5, 7, 11, 13]

filename = '/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.4/numbers.json'

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
