"""
Завдання 2
Написати функцію, яка за допомогою регулярних виразів з файлу витягує дані про дату народження,
телефон та електронну адресу. Дані потрібно записати до іншого файлу.
"""


import re
import json


with open('my_text.txt', 'r', encoding='utf8') as file:
    read_text = file.read()


# sample_text = ("Олександр народився 12.04.1985, його телефон: +380501234567, / "
#                "електронна пошта: olex@example.com. Марія народилася 23.11.1990,/"
#                "телефон: +380671234567, пошта: maria@example.com. Сергій має дату народження 05.09.1987,/"
#                "його телефон: +380931234567, пошта: serhiy@example.com")

my_answer = {}

tel_numbers_pattern = r'[+|380]\d+'
all_numbers = re.findall(tel_numbers_pattern, read_text)

numbers = []
for number in all_numbers:
    if len(number) > 4:
        numbers.append(number)

birthdays_pattern = r'(\d{2}\.\d{2}.\d+)|((\d{2}\/\d{2}.\d+))'
my_birthdays = re.findall(birthdays_pattern, read_text)

emails_pattern = r'\w+@\w+.\w{2,3}'
my_emails = re.findall(emails_pattern, read_text)

my_answer['numbers'] = ' ,'.join(numbers)
my_answer['emails'] = ' ,'.join([email for email in my_emails])
my_answer['birthdays'] = ' ,'.join([birthday[0] for birthday in my_birthdays])

with open('data_json.json', 'w') as file:
    json.dump(my_answer, file, indent=2, ensure_ascii=False)


