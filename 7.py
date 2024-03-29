k = int(input('Введите количество суш: '))
ost = 0
ostat = 0
if k != 0 and k % 5 != 0 and k % 7 != 0:
    while k > 0:
        ost = k - 5
        if ost == 7 or ost == 5:
            print('да')
            break
        k -= 5
    if ost != 5 and ost != 7:
        ost = 0
        while k > 0:
            ost = k - 7
            if ost == 7 or ost == 5:
                print('да')
                break
            k -= 7
        if ost != 0 or ost != 5 and ost != 7:
            print('нет')
elif k % 5 == 0 or k % 7 == 0:
    print('да')

