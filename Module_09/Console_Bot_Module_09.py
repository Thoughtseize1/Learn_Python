USERS = {}


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
    USERS[name] = phone
    return f'User {name} added with phone {phone}'


@input_error
def change_phone(args):
    name, phone = args
    old_phone = USERS[name]
    USERS[name] = phone
    return f'User {name} have a new phone number. Old number was {old_phone}'


@input_error
def show_number(args):
    if not USERS:
        return 'Your adress book is empty'
    user = args[0]
    phone = USERS[user]
    return f'{user} : {phone}'


@input_error
def delete_user(args):
    name = args[0]
    del USERS[name]
    return f"User with name {name} was deleted"


def show_all(_):
    result = ''
    if not USERS:
        return 'Your adress book is empty'
    for name, phone in USERS.items():
        result += f"{name}: {phone} \n"
    return result


def hello(_):
    return "Can I help you? Write something to me:) You can see the avaliable commands by 'help' command"


def exit(_):
    print("Good Bye!!!")
    return 'exit'


def avaliable_comands(_):
    return 'Use "add" to add new user \nUse "change" to change user\'s number\nUse "show" or "show all" to see all adress book. \nUse "exit" or "q" to exit from bot'


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
    'delete': delete_user
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
