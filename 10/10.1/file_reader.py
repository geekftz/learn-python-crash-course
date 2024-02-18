# with open('/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.1/pi_digits.txt', encoding='utf-8') as file_object:
#     contents = file_object.read()
#     print(contents)
#     print(contents.rstrip())

# with open('/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.1/pi_digits.txt', encoding='utf-8') as file_object:
#     for line in file_object:
#         print(line.rstrip())

# with open('/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.1/pi_digits.txt', encoding='utf-8') as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

with open('/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.1/pi_digits.txt', encoding='utf-8') as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
