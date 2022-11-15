'''
Напишіть функцію визначення кількості днів у конкретному місяці. Ваша функція повинна приймати два параметри: month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12 і year - рік, що складається із чотирьох цифр. Перевірте, чи функція коректно обробляє місяць лютий високосного року.
'''
from calendar import monthrange


def get_days_in_month(month, year):
    try:
        return monthrange(year, month)[1]
    except:
        print("Incorrect month")


print(get_days_in_month(2, 2016))
