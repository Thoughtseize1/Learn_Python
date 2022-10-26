students_info = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]


def save_applicant_data(source, output=None):
    my_dict = []
    for data in source:
        string = ''
        for key, value in data.items():
            string += str(value) + ','
        my_dict.append(string[:-1]+'\n')
    with open(output, 'w') as file_to_write:
        file_to_write.writelines(my_dict)


save_applicant_data(
    students_info, r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\text_to_write_task8.txt')
