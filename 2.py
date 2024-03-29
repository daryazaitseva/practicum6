a, b = map(int, input('Введите параметры прямоугольного отверстия: ').split('x'))
c, d, e = map(int, input('Введите параметры кирпича: ').split('x'))
if min(c, d, e)*((c + d + e) - max(c, d, e) - min(c, d, e)) < a*b:
    print('да')
else:
    print('нет')