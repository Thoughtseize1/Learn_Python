import re


def is_integer(s):
    if len(s) == 0:
        return False
    s = s.strip()
    if s.isdigit() or s[1:].isdigit() and s[0] in ('+', '-'):
        return True
    else:
        return False

# Another case with regular expression


def is_integer_reg(s):
    if len(s) == 0:
        return False
    s = s.strip()
    if re.search('[\+|\-|\d]\d+$', s):
        return True
    else:
        return False


# Testing
print(is_integer('+34bbbbbbbbb     '))
print(is_integer('+34    '))
print(is_integer('-34bbbbbbbbb     '))
print(is_integer('   +34 *@bb     '))
print(is_integer('099     '))
# Testing another function
print(is_integer_reg('+34'))
print(is_integer_reg('-34'))
print(is_integer_reg('+3433!'))
print(is_integer_reg('+34GT'))
print(is_integer_reg('+34R%T'))
