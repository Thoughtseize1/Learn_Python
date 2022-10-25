def read_employees_from_file(path) -> list:
    my_file = open(path, 'r')
    list_with_employees = []
    try:
        while True:
            data = my_file.readline().replace('\n', '')
            if not data:
                break
            list_with_employees.append(data)
    finally:
        my_file.close()
    return list_with_employees


print(read_employees_from_file(
    r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\file_for_2task.txt'))
