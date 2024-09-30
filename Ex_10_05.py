"""
Завдання 5
З клавіатури вводиться рядок, в якому є інформація про прізвище, ім'я, дату народження,
електронну адресу та відгук про курси учня. Написати функцію, яка, використовуючи регулярні вирази, витягне дані з
рядка і поверне словник.

"""

import re
import json

my_test_text = """
Іваненко Олександр, 15.03.1992, alex.ivanenko@example.com — "Курси були дуже корисними, багато нової інформації та практичних завдань."
Петренко Марія, 28.07.1990, m.petry@example.com — "Я отримала цінні знання, викладачі професійні, рекомендуватиму іншим."
Сидоренко Андрій, 10.11.1985, sidorenko.andrii@example.com — "Дуже цікаві курси, особливо сподобалися практичні заняття, хотілося б ще більше."
Коваленко Олена, 05.02.1995, olena.kovalenko@example.com — "Задоволена курсами, але іноді не вистачало глибини в поясненнях складних тем."
Мельник Сергій, 19.09.1988, serg.melnik@example.com — "Все чудово, дякую за цікаві матеріали та постійну підтримку від викладачів."
"""


fio_pattern = r'^[А-яЇїІіЄє]+ [А-яЇїІіЄє]+'
birthdays_pattern = r'(\d{2}\.\d{2}.\d+)|((\d{2}\/\d{2}.\d+))'
emails_pattern = r'\w+@\w+.\w{2,3}'
comment = r'\"[А-я\WЇїІіЄє]+$'

my_dict = {}

for input_string in my_test_text.splitlines()[1::]:
    dkk = {}
    name = re.findall(fio_pattern, input_string)
    birthday = re.findall(birthdays_pattern, input_string)
    dkk['name'] = ''.join(name)
    dkk['birthday'] = re.findall(birthdays_pattern, input_string)[0][0]
    dkk['email'] = re.findall(emails_pattern, input_string)[0]
    my_dict[''.join(name)] = dkk

with open('my_answer_05.json', 'w', encoding='utf8') as file:
    json.dump(my_dict, file, indent=2, ensure_ascii=False)
