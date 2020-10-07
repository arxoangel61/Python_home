#выручка = proceeds
#издержки = costs
#сотрудники = staff
#доход = income
#убыток = lesion
#прибыль = profit

staff = 0
proceeds = float(input("enter proceeds: "))
costs = float(input("enter costs: "))
if proceeds > costs:
    result = "%.2f" % (proceeds - costs)
    print("Фирма работает в плюс:", result)
    staff = int(input("enter staff: "))
    income = "%.2f" % (float(result) / staff)
    print("Каждый сотрудник заработал по:", income, "прибыли")
if proceeds < costs:
    result = "%.2f" % (float(proceeds) - float(costs))
    print("Фирма работает в минус:", "%.2f" % abs(float(result)))
if proceeds == costs:
    print("Фирма работает в Ноль")

