def normal_name(list_name):
    return list(map(lambda x: x.capitalize(), list_name))


def get_emails(list_contacts):
    return map(lambda x: x.get('email'), list_contacts)


list_with_incorrect_names = ["dan", "jane", "steve", "mike", "nikita"]

contacts_list = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@urk.net",
    "phone": "(992) 914-3792",
    "favorite": False},
    {
        "name": "Allen Raymond",
        "email": "NUtella@co.uk",
        "phone": "(992) 914-3792",
        "favorite": False},
    {
        "name": "Allen Raymond",
        "email": "Snickers@com",
        "phone": "(992) 914-3792",
        "favorite": False}
]

print(normal_name(list_with_incorrect_names))
a = get_emails(contacts_list)
print(a)
print(type(a))
a = list(a)
print(a)
print(type(a))
