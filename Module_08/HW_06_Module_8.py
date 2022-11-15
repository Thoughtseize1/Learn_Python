from decimal import Decimal, getcontext

# print(0.1 + 0.2 == 0.3)  # False
# print(0.1 + 0.2)  # 0.30000000000000004

# getcontext().prec = 6
# print(Decimal(15) / Decimal(7))  # 2.14286


def decimal_average(number_list, signs_count):
    sum_of_values = Decimal(0)
    getcontext().prec = signs_count
    for value in number_list:
        sum_of_values += Decimal(value)
    return sum_of_values/Decimal(len(number_list))


print(decimal_average([3, 5, 77, 23, 0.57], 6))
print(decimal_average([31, 55, 177, 2300, 1.57], 9))

a = [3.2, 5.5, 7.7, 2.3, 0.57]
b = []
for value in a:
    b.append(Decimal(value))


print(type(b[1]))
