for i in range(16):
    s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
    print(s)

# width = 5
# for num in range(10):
#     print('{:^10} {:^10} {:^10}'.format(num, num ** 2, num ** 3))

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


def formatted_grades(students):
    formatted_list = []
    number = 1
    for name, grade in students.items():
        temp_string = '{:>4}|{:<10}|{:^5}|{:^5}'.format(
            number, name, grade, grades.get(grade))
        formatted_list.append(temp_string)
        number += 1
    return formatted_list


for el in formatted_grades(students):
    print(el)
