# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator  # импортируем переводчик


out_f = open("text_4.txt", "r", encoding='utf-8')
translator = Translator()
content = out_f.read()
result = translator.translate(content, src='en', dest='ru')  # выбираем исходный и на какой нужно перевести язык
# print(result.src)
# print(result.dest)
print(result.text)

out_f.close()

filename = input('\n'"enter name: ")  # пишем имя файла .txt # в нашем случае 404.txt
text = result.text  # сохраняем перевод
file = open(filename, 'w+', encoding='utf-8')
file.write(text)  # сохраняем перевод в новый созданный .txt

file.close()
