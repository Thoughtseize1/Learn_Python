
'''Декоратор повинен додавати для коротких номерів префікс +38, а для повного міжнародного номера (з 12 символом) - тільки знак +. Реалізуйте декоратор format_phone_number для функції sanitize_phone_number з необхідним функціоналом.
Очікувалося, що функція sanitize_phone_number при отриманні параметра ' 0503451234' поверне наступний результат '+380503451234'
'''


def format_phone_number(func):
    def inner(phone):
        temp_phone = func(phone)
        if len(temp_phone) == 12:
            return '+' + temp_phone
        else:
            return '+38' + temp_phone
    return inner


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


tel_1 = sanitize_phone_number(' 0503451234')
print(tel_1)
