"""
Завдання 1
Написати функцію, яка за допомогою регулярних виразів розбиває текст
на окремі слова і знаходить частоту окремих слів.
"""


import re


my_text = "День почався дуже добре. Добре світить сонце, добре йти на прогулянку. \
           Люди радісні, і це добре. Коли все добре, настрій стає ще кращим."


def simple_count(text: str):
    pattern = r'[А-яі]+'

    words = re.findall(pattern, text)

    my_counter = {}
    words = [i.lower() for i in words]

    for word in words:
        my_counter[word] = words.count(word)

    for k, v in my_counter.items():
        print(f'слово "{k}" - count {v} times')


if __name__ == '__main__':
    simple_count(my_text)