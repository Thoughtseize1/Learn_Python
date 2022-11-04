from shutil import *


def create_backup(path, file_name, employee_residence):
    with open(path + '/' + file_name, 'wb') as file:
        for key, value in employee_residence.items():
            if not key:
                break
            file.write("".join(key + " " + value + '\n').encode("utf-8"))
    return make_archive('backup_folder', 'zip')


my_dict = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}

create_backup(
    r"C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06", "file_for_13task.bin", my_dict)
