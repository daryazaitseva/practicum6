n, m = map(int, input('Введите количество оцепляемых кварталов: ').split('x'))
k = int(input('Введите количество возможно оцепляемых кварталов: '))
if k % 2 != 0 or k > n * m:
    print('неосуществимо')
else:
    print('успешно')
