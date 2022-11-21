# HW - 09
for i in filter(lambda x: x % 2, range(1, 10 + 1)):
    print(i, end='')
print()

some_str = 'Nikita, Ostap, Katya'
for i in filter(lambda x: x.islower(), some_str):
    print(i, end='')


def positive_values(list_payment):
    return list(filter(lambda x: x > 0, list_payment))


print('\n----------------')

### HW - 10


def get_favorites(contacts):
    return list(filter(lambda star: star.get('favorite'), contacts))


contacts_list = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@urk.net",
    "phone": "(992) 914-3792",
    "favorite": True},
    {
        "name": "Allen Raymond",
        "email": "NUtella@co.uk",
        "phone": "(992) 914-3792",
        "favorite": True},
    {
        "name": "Allen Raymond",
        "email": "Snickers@com",
        "phone": "(992) 914-3792",
        "favorite": False}
]

print(get_favorites(contacts_list))
