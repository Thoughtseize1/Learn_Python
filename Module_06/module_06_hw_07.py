def sanitize_file(source, output):
    text_without_numbers = ''
    with open(source, 'r') as file:
        while True:
            data = file.read(1)
            if not data:
                break
            if not data.isdigit():
                text_without_numbers += data
            else:
                continue
    with open(output, 'w') as output_file:
        output_file.write(text_without_numbers)


sanitize_file(r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\text_for_read_task_07.txt',
              r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\text_to_write_task7.txt')
