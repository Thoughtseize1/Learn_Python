from pathlib import Path
from os import makedirs, getcwd
# Testing module Path
print(getcwd())
my_file = open(
    r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\test_file.txt', mode='r')

# Readind per 100 bytes our file. If data
# while True:
#     data = my_file.read(100)
#     print(data)
#     if not data:
#         break

# "Стрим" можно итерировать с по "строкам безопасно это делать с помощью with -менеджер контекста.
# With делает это безопасно"
with open("test_file.txt", mode="r") as file:
    for line in file:
        print(line)
