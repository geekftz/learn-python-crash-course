
filename = '/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.2/programming.txt'
print(filename)

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
