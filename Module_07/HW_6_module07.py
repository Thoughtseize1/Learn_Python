'''Реалізуйте функцію solve_riddle(riddle, word_length, start_letter, reverse=False) для знаходження слова, що шукається в рядку ребуса.

Параметри функції:

riddle - рядок із зашифрованим словом.
word_length – довжина зашифрованого слова.
start_letter - літера, з якої починається слово (мається на увазі, що до початку слова літера не зустрічається в рядку).
reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому. Для значення True слово зашифроване у зворотньому порядку, наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.
Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.'''


def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse:
        riddle = riddle[::-1]
    index_of_start_word = riddle.find(start_letter)
    if index_of_start_word == -1:
        return ''
    return riddle[index_of_start_word:word_length+index_of_start_word]


'''
Функція solve_riddle повертає неправильний результат: 'r'. Очікувалося, що функція solve_riddle при отриманні параметра ('mi1powperet', 3, 'r', True) поверне наступну строку 'rep'
'''
print(solve_riddle('microwave', 4, 'w', False))
