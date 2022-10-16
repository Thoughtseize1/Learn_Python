import re
### Solution was not passed by autocheck ###
# def find_word(text, word):
#     information_dict = {}
#     founded_a_match = word in text
#     information_dict['result'] = founded_a_match
#     is_match = re.search(word, text)
#     if founded_a_match:
#         information_dict['first index'], information_dict['last index'] = is_match.span(
#         )
#     else:
#         information_dict['first index'], information_dict['last index'] = None, None
#     information_dict['search_string'] = word
#     information_dict['string'] = text
#     return information_dict

### Solution passed by autocheck ! ###


def find_word(text, word):
    result = re.search(word, text)
    return {'result': bool(result),
            'first_index': result.span()[0] if result else None,
            'last_index': result.span()[1] if result else None,
            'search_string': word,
            'string': text}


#Test1 (Exist)
# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"))

#Test2 (No_Exist)
# print(find_word(
#     "Guido van Rossum began working on in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as 0.9.0.",
#     "Python"))

# Test3
print(find_word('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.', 'Python'))
