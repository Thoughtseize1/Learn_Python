import re


def generator_numbers(string=""):
    numbers = re.findall('\d+', string)
    numbers = [int(i) for i in numbers]
    for num in numbers:
        yield num


def sum_profit(string):
    sum = 0
    numbers = generator_numbers(string)
    while True:
        try:
            sum += next(numbers)
        except StopIteration:
            break
    return sum


a = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
print(sum_profit(a))

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
