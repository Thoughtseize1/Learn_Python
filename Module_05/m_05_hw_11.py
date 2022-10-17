import re

s = "I bought 77 nuts for 6$ and 11 bolts for 3$."

# print(re.findall("(\d){2}", s))  # ['0']
# print(re.findall("[\d]{3}", s))
print('')


def find_all_words(text, word):
    return re.ignorecase.findall("word", text)


def replace_spam_words(text, spam_words):
    for word in spam_words:
        text = re.sub(word, '*'*len(word), text, flags=re.IGNORECASE)
    return text


test_str = replace_spam_words(
    'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', ['began', 'Python'])

print(test_str, '\n')

# print(find_all_words())
