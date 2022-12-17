from datetime import datetime
from collections import UserDict


class AdressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def look_book(self):
        if not self.items():
            print("The book is empty")
        else:
            for name, phone in self.data.items():
                print(f"Name: {name}")
                print("Phones: ", end="")
                for customer_phone in phone.phones:
                    if len(phone.phones) > 1:
                        print(f"{customer_phone.value}, ", end="")
                    else:
                        print(f"{customer_phone.value} ")
                print()

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
        birth_date = datetime.strptime(value, '%Y-%m-%d').date()
        if birth_date > today_is:
            raise ValueError(
                "Wrong enter. Up to date")
        self._value = value


class Record():
    def __init__(self, name, *phones, birthday):
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

    def get_days_to_next_birthday(self):
        if not self.birthday:
            raise ValueError("Please, add birthday firstly")
        today = datetime.now().date()
        birthday = datetime.strptime(self.birthday.value, '%Y-%m-%d').date()

        next_birthday_year = today.year

        if today.month >= birthday.month and today.day > birthday.day:
            next_birthday_year += 1

        next_birthday = datetime(
            year=next_birthday_year,
            month=birthday.month,
            day=birthday.day
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
def birthday_func(data):
    name, date = data.strip().split(' ')
    record = MY_BOOK[name]
    record.add_birthday(date)
    return f'For {name} you add Birthday {date}'


@input_error
def next_birthday_func(name):
    name = name.strip()
    record = MY_BOOK[name]
    return f"Days to next {name}'s birthday will be in {record.get_days_to_next_birthday()}."


def show_all(_):
    MY_BOOK.look_book()
    return ""


def hello(_):
    return "Can I help you? Write something to me:) You can see the avaliable commands by 'help' command"


def exit(_):
    print("Good Bye!!!")
    return 'exit'


def avaliable_comands(_):
    return 'Use "add" to add new user \nUse "change" to change user\'s number\nUse "show" or "show all" to see all adress book. \nUse "exit" or "q" to exit from bot\nUse "del" or "delete" to delete user'


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
    'birthday': birthday_func,
    'days to birthday': next_birthday_func
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


def main():
    while True:
        user_input = input(">>>")
        handler, *args = parser_input(user_input)
        result = handler(*args)
        if result == 'exit':
            break
        print(result)


if __name__ == '__main__':
    main()
