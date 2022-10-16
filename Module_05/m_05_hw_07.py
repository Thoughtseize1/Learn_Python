# txt = "the sun"
# my_table = txt.maketrans("nus", "nos", "eh ")
# print(txt.translate(my_table))  # son

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r",
               "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def translate(name):
    return name.translate(TRANS)


print(translate("Дмитро Короб"))  # Dmitro Korob
print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk
