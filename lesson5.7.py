# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.


import json

firm_dict = {}
profit = []

with open("text_7.txt", "r", encoding='utf-8') as info_f:
    lines = info_f.readlines()
    # print(lines)
    for line in lines:
        name, form, revenue, costs = line.split()  # name - имя компании, form - (ООО-ИП), revenue - выручка, costs - издержки
        prof = int(revenue) - int(costs)
        firm_dict[name] = prof
        if prof > 0:
            profit.append(prof)

profit = sum(profit) / len(profit) #общую сумму / на количество компаний
info = [firm_dict, {'profit': profit}]

with open('text_77.json', 'w') as f_json:
    json.dump(info, f_json)

with open('text_77.json') as f_json:
    print(json.load(f_json))
