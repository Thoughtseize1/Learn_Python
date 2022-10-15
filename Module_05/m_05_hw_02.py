articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key, letter_case=False):
    updated_list = []
    for title in articles_dict:
        for content in title.items():
            if not letter_case and str(content[1]).lower().find(key.lower()) != -1:
                updated_list.append(title)
            elif str(content[1]).find(key) != -1:
                updated_list.append(title)
    return updated_list

print(find_articles('That NEW'))
print("Testing new commit")