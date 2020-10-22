# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

f_obj = open("text_5.txt", 'w+', encoding='utf-8')

content = input("Введите четные числа через пробел и нажмите Enter для записи: ")

f_obj.write(content)  # сохраняем в созданный .txt

f_obj.close()


def sum_1():
    live = []
    global f_obj
    try:
        f_obj = open("text_5.txt", 'r', encoding='utf-8')
        for line in f_obj:
            live += line.split()

            return live
    except IOError:
        print("Произошла ошибка ввода-вывода!")
    finally:
        f_obj.close()


# print(sum_1())

c = 0
for box in sum_1():
    # print(int(box))
    c = c + int(box)
print("Общая сумма всех записанных чисел: ", c)
