def capital_text(s: str) -> str:
    s = s.capitalize()
    b = s.split(' ')
    print(b)
    index = 0
    while index < len(b):
        if b[index][-1] in ('?', '!', '.') and index+1 < len(b):
            b[index+1] = b[index+1].capitalize()
        index += 1
    return ' '.join(b)


test = 'доброго дня! як справи? в мене норм.'
test_text = 'alert. boss dear you so cool! oh'
print(capital_text(test))
print(capital_text(test_text))
