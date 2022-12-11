"""
Next Palindromic Number.
"""


def next_pal(val):
    # your code here
    next_palindrime = 0
    while True:
        val += 1
        if str(val) == str(val)[::-1]:
            next_palindrime = val
            break
    return next_palindrime

# best Practice


def next_pal_best(val):
    val += 1
    while str(val) != str(val)[::-1]:
        val += 1
    return val


print(next_pal(11))
print(next_pal(188))
print(next_pal(191))
print(next_pal(2541))

""" Do I get a bonus?"""


def bonus_time(salary, bonus):
    return f'${salary*10}' if bonus else f'${salary}'


print(bonus_time(10000, True), '$100000')
print(bonus_time(25000, True), '$250000')
print(bonus_time(10000, False), '$10000')
print(bonus_time(60000, False), '$60000')
print(bonus_time(2, True), '$20')
print(bonus_time(78, False), '$78')
print(bonus_time(67890, True), '$678900')

"""Sorting Dictionaries"""


def sort_dict(d):
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
    a = dict(reversed(sorted_dict.items()))
    return list(a.items())

# best Practice


def sort_dict_best(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)


print(sort_dict({3: 1, 2: 2, 1: 3}), [(1, 3), (2, 2), (3, 1)])
print(sort_dict({1: 2, 2: 4, 3: 6}), [(3, 6), (2, 4), (1, 2)])
print(sort_dict({1: 5, 3: 10, 2: 2, 6: 3, 8: 8}),
      [(3, 10), (8, 8), (1, 5), (6, 3), (2, 2)])

x = 3.1234567
x = float('{:.2f}'.format(x))
print(x)
