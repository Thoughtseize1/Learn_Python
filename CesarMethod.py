message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if ord(ch)>=65 and ord(ch)<=90:
        pos = ord(ch) - ord("A")
        pos = (pos+offset)%26
        new_char = chr(pos + ord("A"))
        encoded_message += new_char 
        continue
    elif ch != " " and ch!="!":
        pos = ord(ch) - ord("a")
        pos = (pos+offset)%26
        new_char = chr(pos + ord("a"))
    elif ch=="!":
        new_char = ch
    else:
        new_char = " "
    encoded_message = encoded_message+new_char
print(encoded_message)
print("I think that ama cool boy!!")