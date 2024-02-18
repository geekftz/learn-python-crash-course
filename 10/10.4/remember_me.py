# import json


# username = input("what is your username")

# filename = "/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.4/username.json"

# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print("we have a username called " + username)

# 合并现有逻辑

# import json

# filename = "/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.4/username.json"

# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input("what is your username")
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print("we have a username called " + username)
# else:
#     print("welcome back " + username)

# 重构
import json

filename = "/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.4/username.json"


def get_stored_username():
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("what is your username")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("we have a new username called " + username)


def greet_user():
    username = get_stored_username()
    if username is None:
        get_new_username()
    else:
        print("welcome back, " + username)


greet_user()
