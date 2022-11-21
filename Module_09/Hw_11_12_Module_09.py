from functools import reduce

numbers = [5, 6, 7]
sum_nums = reduce(lambda x, y: x+y, numbers, 2)

print(sum_nums)

# HW_ 12 ____
payments = [100, -3, 400, 35, -100]


def amount_payment(payment):
    return reduce(lambda x, y: x+y, payment, 0)


print(amount_payment(payments))
