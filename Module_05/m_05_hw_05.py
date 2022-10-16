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


def get_phone_numbers_for_countries(list_phones):
    sorted_dict = {}
    sanitized_list_of_numbers = [
        sanitize_phone_number(number) for number in list_phones]
    for number in sanitized_list_of_numbers:
        if number.startswith("81"):
            sorted_dict["JP"] = sorted_dict["JP"].append(number)
    print(sorted_dict)


phones_numbers = ["+380993672266", '   065-66-2711', '   -813424715']

get_phone_numbers_for_countries(phones_numbers)
