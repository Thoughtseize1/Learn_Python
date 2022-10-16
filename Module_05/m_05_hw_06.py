import re


def is_spam_words(text, spam_words, space_around=False):
    for word in spam_words:
        if word in spam_words:
            if text[text.find(word)+len(word)] == " " and space_around:
                return False
            else:
                return True


# print(is_spam_words("Молох", ["лох"]))  # True
# print(is_spam_words("Молох", ["лох"], True))  # False

# print(is_spam_words("Ты лох.", ["лох"]))  # True
# print(is_spam_words("Ты лох.", ["лох"], True))  # True
# print(is_spam_words('Молох бог лох ужасен. лох', ['лох']))  # True


# ДОЛЖНО БЫТЬ == False
print(is_spam_words('Молох бог ужасен.', ['лох'], True))
# ДОЛЖНО БЫТЬ == True
print(is_spam_words('Молох бог ужасен.', ['лох']))
