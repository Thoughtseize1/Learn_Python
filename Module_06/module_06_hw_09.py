s = b'Hello!'

byte_str = 'some text'.encode()


def is_equal_string(utf8_string, utf16_string):
    utf16_string = utf16_string.decode('utf-16')
    utf8_string = utf8_string.decode('utf-8')

    if utf8_string.casefold() == utf16_string.casefold():
        return True
    else:
        return False
