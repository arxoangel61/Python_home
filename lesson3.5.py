# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_func2():
    x = True
    result = 0
    while x == True:
        numbers = input("enter number and q: ").split()
        res_line = 0
        for num in numbers:
            if 'q' in num:
                x = False
                break
            res_line += int(num)
        result += res_line
    return result


print(my_func2())
