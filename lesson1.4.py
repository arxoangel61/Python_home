a = int(input("enter: "))

maxi = a % 10
while True:
    a = a // 10
    if a % 10 > maxi:
        maxi = a % 10
    if a > 9:
        continue
    else:
        print("max number", maxi)
        break


