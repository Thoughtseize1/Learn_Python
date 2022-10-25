def get_recipe(path, search_id) -> dict:
    ingredients_list = {
        'id': "",
        'name': "",
        'ingredients': []
    }
    with open(path, 'r') as file:
        for line in file:
            line_list = line.split(',')
            if line_list[0] == search_id:
                ingredients_list['id'] = line_list.pop(0)
                ingredients_list['name'] = line_list.pop(0)
                for ingredient in line_list:
                    ingredients_list['ingredients'].append(
                        ingredient.replace('\n', ''))
    return ingredients_list if ingredients_list['id'] else None


print(get_recipe(
    r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\file_for_6task.txt', '60b90c3b13067a15887e1ae4'))
