def get_cats_info(path) -> dict:
    list_with_values = []
    temp_dict = {}
    with open(path, 'r') as file:
        for line in file:
            line = line.split(',')
            temp_dict['id'] = line[0]
            temp_dict['name'] = line[1]
            temp_dict['age'] = line[2].replace('\n', '')
            list_with_values.append(temp_dict.copy())
    return list_with_values


print(get_cats_info(
    r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\file_for_5task_txt'))
