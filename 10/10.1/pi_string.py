with open('/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.1/pi_digits.txt', encoding='utf-8') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))
