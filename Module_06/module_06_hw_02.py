def write_employees_to_file(employee_list, path):
    my_file = open(path, 'w')
    try:
        for employee in employee_list:
            if type(employee) is list:
                for person in employee:
                    my_file.write(person + '\n')
            else:
                my_file.write(employee + '\n')
    finally:
        my_file.close()


workers_list = [['Robert Stivenson,28',
                 'Alex Denver,30'], ['Drake Mikelsson,19']]

write_employees_to_file(
    workers_list, r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\file_for_2task.txt')
