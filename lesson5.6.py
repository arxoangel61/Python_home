# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_dict = dict()

f_obj = open("text_6.txt", 'r', encoding='utf-8')
# content = f_obj.readlines()
# for line in content:
#     splitted_line = line.split()
#     # print(splitted_line)
#     subject = splitted_line[0]
#     # print(subject)
#     sum_lesson = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
#     # print(sum_lesson)
#     my_dict[subject[:-1]] = sum_lesson
#
# print(my_dict)

import re

my_dict = {}
with open("text_6.txt", "r", encoding="utf-8") as file:
    for line in file:
        num = (int(num) for num in re.findall('(\d+)', line))
        word = line.split()[0]
        my_dict.update({word: sum(num)})

print(my_dict)
