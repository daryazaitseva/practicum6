k = int(input('Введите количество суш: '))
ost = 0
if k % 5 == 0 or k % 7 == 0:
    print('да')
else:
    while k > 0:
        k -= 5
        if k % 5 == 0:
            print('да')
            break
        elif k % 7 == 0:
            print('да')
            break
    if k % 5 != 0 and k % 7 != 0:
        print('нет')




