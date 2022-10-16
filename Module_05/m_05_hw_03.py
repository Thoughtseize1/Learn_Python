def sanitize_phone_number(phone):
    ''' For working with one number'''
    return (phone.replace('(', '')
            .replace(')', '')
            .replace('-', '')
            .replace('+', '')
            .replace(' ', ''))


def sanitize_phone_number_2(phone: str):
    ''' A function from homework!!!'''
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def sanitize_phone_numbers_list(phone):
    '''Another desicion for list with numbers'''
    return [new_number.replace('(', '')
            .replace(')', '')
            .replace('-', '')
            .replace('+', '')
            .replace(' ', '') for new_number in phone]


phones_numbers = ["    +38(050)123-32-34", "     0503451234",
                  "(050)8889900",
                  "38050-111-22-22",
                  "38050 111 22 11   "]

print(sanitize_phone_numbers_list(phones_numbers))
