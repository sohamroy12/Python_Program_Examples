# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age  # attributes


# def call(self):
#     print('call')
#     # return 'Done'

# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Tom', 20)
cat2 = Cat('Tommy', 10)
cat3 = Cat('Tomtom', 5)

# print(cat1.call())
print(f'\nName of the first cat is \"{cat1.name}\" & Age is : {cat1.age}')
print(f'\nName of the seond cat is \"{cat2.name}\" & Age is : {cat2.age}')
print(f'\nName of the third cat is \"{cat3.name}\" & Age is : {cat3.age}\n')
print(Cat.species)

# 2 Create a function that finds the oldest cat
cat_Age = [cat.age]
print(cat_Age)


def CatMax():
    return print(cat_Age.max())


CatMax()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
