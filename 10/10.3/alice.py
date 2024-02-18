# filename = 'alice.txt'

# with open(filename) as f_obj:
#     contents = f_obj.read()


# filename = '/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.3/alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = "Sorry, the file " + filename + " does not exist."
#     print(msg)

filename = '/Users/fangxiang/Documents/GitHub/learn-python-crash-course/10/10.3/alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
