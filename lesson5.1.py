# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

out_f = open("lesson1.txt", "w", encoding='utf-8')
line = input("Enter:"'\n')
while out_f:
    out_f.writelines(line)
    line = input("Enter:"'\n')
    if not line:
        break
out_f.close()

out_f = open("lesson1.txt", "r", encoding='utf-8')
for content in out_f:
    print(content)

out_f.close()
