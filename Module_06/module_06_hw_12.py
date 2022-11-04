import base64
'''
У наведеному вище прикладі ми імпортували base64 модуль. Змінну message конвертуємо в байтовий об'єкт, використовуючи рядковий метод 'encode', і зберігаємо його в 'message_bytes'. Потім ми кодуємо message_bytes та зберігаємо результат в base64_bytes, використовуючи base64.b64encode метод. Нарешті, ми отримуємо представлення перетворення Base64 у вигляді рядка, декодуючи змінну base64_bytes. В результаті змінна base64_message зберігатиме наступний рядок YWxhZGRpbjpvcGVuc2VzYW1l
'''
message = "aladdin:opensesame"
message_bytes = message.encode("utf-8")
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode("utf-8")
print(base64_message)  # YWxhZGRpbjpvcGVuc2VzYW1l


def encode_data_to_base64(data):
    new_coded_list = []
    for login_password in data:
        login_password = login_password.encode("utf-8")
        login_password = base64.b64encode(login_password)
        login_password = login_password.decode('utf-8')
        new_coded_list.append(login_password)
    return new_coded_list


login_list = ['andry:uyro18890D', 'steve:oppjM13LL9e']

print(encode_data_to_base64(login_list))
