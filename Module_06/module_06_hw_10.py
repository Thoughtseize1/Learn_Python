info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}


def save_credentials_users(path, users_info):
    with open(path, 'wb') as file_with_users:
        for login, password in users_info.items():
            file_with_users.write(
                "".join(login + ": "+password + "\n").encode())


save_credentials_users(
    r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\file_to_write_task10.bin', info)
