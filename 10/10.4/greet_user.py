import json

filename = "/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.4/username.json"

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("username: ", username)
