# 创建和使用类
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 坐下来
    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " is now rolling over")


my_dog = Dog("lili", 10)

# print(my_dog.name)

my_dog.roll_over()
