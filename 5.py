a = input('Введите первый ход коня: ')
b = input('Введите второй ход коня: ')
let_a = 0
let_b = 0
if a[0] == 'a':
    let_a = 1
elif a[0] == 'b':
    let_a = 2
elif a[0] == 'c':
    let_a = 3
elif a[0] == 'd':
    let_a = 4
elif a[0] == 'e':
    let_a = 5
elif a[0] == 'f':
    let_a = 6
elif a[0] == 'g':
    let_a = 7
elif a[0] == 'h':
    let_a = 8

if b[0] == 'a':
    let_b = 1
elif b[0] == 'b':
    let_b = 2
elif b[0] == 'c':
    let_b = 3
elif b[0] == 'd':
    let_b = 4
elif b[0] == 'e':
    let_b = 5
elif b[0] == 'f':
    let_b = 6
elif b[0] == 'g':
    let_b = 7
elif b[0] == 'h':
    let_b = 8

if (((max(let_a, let_b) - min(let_a, let_b) == 2) and (max(int(a[1]), int(b[1])) - min(int(a[1]), int(b[1])) == 1))
        or ((max(let_a, let_b) - min(let_a, let_b) == 1)
            and (max(int(a[1]), int(b[1])) - min(int(a[1]), int(b[1])) == 2))):
    print('верно')
else:
    print('ошибка')


