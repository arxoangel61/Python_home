a = int(input("enter начало: "))
b = int(input("enter конец: "))
score = 1
c = a / 100 * 10
print(score,"-й день:",a, sep='')
while True:
    if a < b:
        a = a + c
        c = a / 100 * 10
        score = score + 1
        print(score,"-й день:","%.2f" % a, sep='')
        continue
    if a > b:
        print("на ", score,"-й день спортсмен достиг результата - не менее ",b," км", sep='')
        break
