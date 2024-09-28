"""
Завдання 3
Користувач вводить з клавіатури пропозицію. Написати функцію,
яка друкуватиме на екран останні 3 символи кожного слова.

"""


import re

my_input = 'Користувач вводить з клавіатури пропозицію. Написати функцію,\
            яка друкуватиме на екран останні 3 символи кожного слова.'


def last_3_characters(some_input: str):
    pattern = r'[А-яІіЇі]+'
    usr_input = re.findall(pattern, some_input)
    return [word[len(word)-3:] for word in usr_input]


user_input = input("please provide me the string: ")
for some_word in last_3_characters(user_input):
    print(some_word, end=' ')




