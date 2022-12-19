from datetime import datetime
from collections import UserDict
import pickle


class AdressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def look_book(self):
        if self.items():
            print("YOUR CONTACTS BOOK:")
            for name, record in self.data.items():
                print(f"Name: {name}")
                print('Phones: ' +
                      ', '.join([phone.value for phone in record.phones]))
                if record.birthday:
                    print('Birthday:', record.birthday.value)
                print()
        else:
            print("The book is empty")

    def remove_record(self, name: str):
        self.data.pop(name)

    def iterator(self, count=5):
        pages = []
        i = 0
        for record in self.data.values():
            pages.append(record)
            i += 1
            if i == count:
                yield pages
                pages = []
                i = 0
            if pages:
                yield pages

    def search(self, value):
        record_result = []
        for record in self.data.values():
            if value in record.name.value:
                record_result.append(record)
                continue
            for phone in record.phones:
                if value in phone.value:
                    record_result.append(record)
        if not record_result:
            raise ValueError('Contact does not exist')
        return record_result

    def save_contacts(self, file):
        with open(file, 'wb') as fh:
            pickle.dump(self.data, fh)

    def load_contacts(self, file):
        try:
            with open(file, 'rb') as fh:
                self.data = pickle.load(fh)
        except FileNotFoundError:
            pass


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    pass


class Phone(Field):
    @Field.value.setter
    def value(self, value):
        if not value.isnumeric():
            raise ValueError('Phones are wrong')
        if len(value) < 10 or len(value) > 12:
            raise ValueError("Phone must have 10 symbols")
        self._value = value


class Birthday(Field):
    @Field.value.setter
    def value(self, value):
        today_is = datetime.now().date()
        birth_date = datetime.strptime(value, '%d-%m-%Y').date()
        if birth_date > today_is:
            raise ValueError(
                "Wrong enter. Up to date")
        self._value = birth_date


class Record():
    def __init__(self, name, *phones, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None
        for phone in phones:
            self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        self.del_phone(old_phone)
        self.add_phone(new_phone)

    def del_phone(self, phone: str):
        for record_phone in self.phones:
            if record_phone.value == phone:
                self.phones.remove(record_phone)

    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def get_info(self):
        phone_number = ''
        birth_info = ''

        for phone in self.phones:
            phone_number += f'{phone.value}, '

        if self.birthday:
            birth_info = f'(Birthday: {self.birthday.value})'

        return f'{self.name.value.title()}: {phone_number[:-2]}; {birth_info}'

    def get_days_to_next_birthday(self):
        if not self.birthday._value:
            raise ValueError("Please, add birthday firstly")
        today = datetime.now().date()
        next_birthday_year = today.year

        if today.month >= self.birthday._value.month and today.day > self.birthday._value.day:
            next_birthday_year += 1

        next_birthday = datetime(
            year=next_birthday_year,
            month=self.birthday._value.month,
            day=self.birthday._value.day
        )
        return (next_birthday.date() - today).days


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact doesnt exist, please try again.'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'This contact cannot be added, it exists already'
        except TypeError:
            return 'Unknown command or parametrs, please try again.'
    return inner


@input_error
def add_user(args):
    name, phone = args
    if name not in MY_BOOK:
        MY_BOOK.add_record(Record(name, phone))
        return f'User {name} added with phone {phone}'
    MY_BOOK[name].add_phone(phone)
    return f'Adding a new tel {phone} for {name}'


@input_error
def change_phone(args):
    name, new_phone, old_phone = args
    old_phone = MY_BOOK.get(name)
    print(old_phone)
    MY_BOOK[name].edit_phone(old_phone, new_phone)
    return f'User {name} have a new phone number. Old number was {old_phone}'


@input_error
def show_number(args):
    user = args[0]
    phone = MY_BOOK[user]
    return f'{user} : {[tel.value for tel in phone.phones]}'


@input_error
def delete_user(args):
    name = args[0]
    MY_BOOK.remove_record(name)
    return f"User with name {name} was deleted"


@input_error
def birthday_func(args):
    name, date = args[0], args[1]
    record = MY_BOOK[name]
    record.add_birthday(date)
    return f'For {name} you added Birthday {date}'


@input_error
def next_birthday_func(name):
    record = MY_BOOK[name[0]]
    return f"Days to next {name[0]}'s birthday will be in {record.get_days_to_next_birthday()} days."


def show_all(_):
    MY_BOOK.look_book()
    return ""


@input_error
def search_record(args):
    records = MY_BOOK.search(args[0].capitalize())
    search_records = " "
    for record in records:
        search_records += f'{record.get_info()}\n'
    return search_records


def hello(_):
    return "Can I help you? Write something to me:) You can see the avaliable commands by 'help' command"


def exit(_):
    print("Good Bye!!!")
    return 'exit'


def save_func(_):
    MY_BOOK.save_contacts(FILE_NAME)
    print("Contacts saved")


def avaliable_comands(_):
    return '''
    Use "add" *name* *phone* to add new user.
    Use "change" *name* *phone* to change user\'s number.
    Use "show" or "show all" to see all adress book. 
    Use "exit" or "q" to exit from bot.
    Use "del" *user* or "delete" to delete user.
    Use "birthday" *user* *birthday* to add birthday to contact in format "DD-MM-YYY".
    Use "next" *user* if you want to know how mane days before birthday.
    Use "save" to save your contacts.
    Use "search" *name* to find user's info.
    '''


HANDLERS = {
    "hello": hello,
    'good bye': exit,
    'close': exit,
    'exit': exit,
    'q': exit,
    'add': add_user,
    'change': change_phone,
    'show': show_all,
    'show all': show_all,
    'phone': show_number,
    'help': avaliable_comands,
    'del': delete_user,
    'delete': delete_user,
    'search': search_record,
    'birthday': birthday_func,
    'next': next_birthday_func,
    'save': save_func
}


def parser_input(user_input):
    cmd, *args = user_input.split()
    try:
        handler = HANDLERS[cmd.lower()]
    except KeyError:
        if args:
            cmd = f'{cmd} {args[0]}'
            args = args[1:]
        else:
            def handler(_): return "Unknown command"
    return handler, args


MY_BOOK = AdressBook()
FILE_NAME = "data_console_bot.bin"


def main():
    try:
        MY_BOOK.load_contacts(FILE_NAME)
    except EOFError:
        print('Your book is empty. Write "Help" to see awaliable commands')

    while True:
        user_input = input(">>>")
        handler, *args = parser_input(user_input)
        result = handler(*args)
        if result == 'exit':
            MY_BOOK.save_contacts(FILE_NAME)
            break
        if result:
            print(result)


if __name__ == '__main__':
    main()
