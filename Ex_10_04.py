"""
Завдання 4
Напишіть функцію, яка буде аналізувати текст, що надходить до неї,
і виводити тільки унікальні слова на екран, загальну кількість слів і кількість унікальних слів.

"""

import re

my_text = ('День почався дуже добре. Добре світить сонце, добре йти на прогулянку.'
        'Люди радісні, і це добре. Коли все добре, настрій стає ще кращим')


def simple_text_def(text: str):
        my_words_pattern = r'[А-яЇїІіє]+'
        my_find = re.findall(my_words_pattern, text)
        unique_words = []
        for word in my_find:
            if my_find.count(word) == 1:
                unique_words.append(word)
        return (f'Унікальні слова {", ".join(unique_words)} , кількість унікальних слів {len(unique_words)}'
                f' Усього слів: {len(my_find)}')

if __name__ == '__main__':
    print(simple_text_def(my_text))
