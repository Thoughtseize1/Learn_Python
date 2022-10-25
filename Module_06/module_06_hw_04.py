def add_employee_to_file(record: str, path):
    my_file = open(path, 'a')
    try:
        my_file.write(record+'\n')
    finally:
        my_file.close()


add_employee_to_file('Nikita Mikelsson, 2022',
                     r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\file_for_4task.txt')
