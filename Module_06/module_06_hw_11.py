
def get_credentials_users(path):
    list_with_users_data = []
    with open(path, 'rb') as file_with_users:
        while True:
            data = file_with_users.readline()
            if not data:
                break
            list_with_users_data.append(data.decode('utf-8').replace('\n', ""))
    print(list_with_users_data)
    return list_with_users_data


get_credentials_users(
    r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\file_to_write_task10.bin')
