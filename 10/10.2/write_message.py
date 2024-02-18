
filename = '/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.2/programming.txt'
print(filename)

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")


with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
