class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        user_dict = {
            "id": self.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        self.contacts.append(user_dict)
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if contact['id'] == id:
                return contact
        return None

    def remove_contacts(self, id):
        self.contacts.remove(list(
            filter(lambda contact: contact.get("id") == id, self.contacts)))


book_1 = Contacts()
book_1.add_contacts('Nikita', '001', 'nick@ukr.net', True)
book_1.add_contacts('Katya', '001', 'nick@ukr.net', True)
book_1.add_contacts('BRO', '001', 'nick@ukr.net', False)
book_1.add_contacts('Stas', '001', 'nick@ukr.net', True)

book_2 = Contacts()
book_2.add_contacts('Book2', '001', 'nick@ukr.net', True)
book_2.add_contacts('Book2', '001', 'nick@ukr.net', True)
book_2.add_contacts('Book2', '001', 'nick@ukr.net', False)
book_2.add_contacts('Book2', '001', 'nick@ukr.net', True)
book_1.add_contacts('Kiril', '001', 'nick@ukr.net', True)
book_2.add_contacts('SBook2', '001', 'nick@ukr.net', True)
book_1.add_contacts('Katya', '001', 'nick@ukr.net', True)
book_1.add_contacts('BRO', '001', 'nick@ukr.net', False)

# print(book_1.list_contacts())
# print('---------------')
# print(book_2.list_contacts())
print(book_1.get_contact_by_id(9))
