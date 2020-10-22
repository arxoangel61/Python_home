# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


out_f = open("lesson2.txt", "r", encoding='utf-8')
content = out_f.read()
words = content.split()
num_words = len(words)
print(f"В file {out_f} находится {num_words} слов.")
print((len(content)), "Всего букв")
print(out_f.tell(), "Всего байт")
lines = 0

out_f.close()

out_f = open("lesson2.txt", "r", encoding='utf-8')
content2 = out_f.read()
for live in enumerate(content2.splitlines(), 1):
    print(live)

out_f.close()
