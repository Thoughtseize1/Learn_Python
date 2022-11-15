from collections import namedtuple

import collections
Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    converted_list = []
    if isinstance(cats[0], tuple):
        for cat in cats:
            converted_list.append(cat._asdict())
    elif isinstance(cats[0], dict):
        Point = collections.namedtuple('Cat', cats[0].keys())
        for elem in cats:
            p = Point._make(elem.values())
            converted_list.append(p)
    else:
        return converted_list


a_1 = [Cat("Mick", 5, "Sara"), Cat(
    "Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
a_2 = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]

# a_3 = {"nickname": "Mick", "age": 5, "owner": "Sara"}
# Cat2 = namedtuple('Cat2', a_3)
# cat_1 = Cat2("Mick", '5', 'Sara')
# print(cat_1)


# dct = {'Physics': 0, 'Chemistry': 0, 'Math': 0, 'English': 0}
# Marks = namedtuple('Marks', dct)
# marks = Marks(90, 85, 95, 100)
# print(marks)

# print(convert_list(a_1))
print(convert_list(a_2))
''' 
Функція convert_list повертає неправильний результат: [<class '__main__.Cat'>, <class '__main__.Cat'>, <class '__main__.Cat'>]. Очікувалося, що функція convert_list поверне наступний результат [Cat(nickname='Mick', age=5, owner='Sara'), Cat(nickname='Barsik', age=7, owner='Olga'), Cat(nickname='Simon', age=3, owner='Yura')]

'''

#############--------------PRACTICE------------------#########

# Person = namedtuple(
#     'Person', ['name', 'last_name', 'age', 'birth_place', 'post_index'])
# person = Person('Mick', 'Nitch', 35, 'Boston', '01146')
# person.name  # 'Mick'
# person.post_index  # '01146'
# person.age  # 35
# person[3]  # 'Boston'

# print(person.birth_place)

# Cats = namedtuple('Cats', 'name color age poroda')
# cat_1 = Cats('Sheldon', 'Red', 10, 'Scotish Fold')
# print(cat_1)

# a = cat_1._asdict()
# print(type(a))
# print('-----------------')
# print(a)
# for i in a:
#     print(i)
# print(a['name'])
