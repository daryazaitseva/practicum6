import turtle as tr

x1, y1 = map(int, input('Введите центр первой окружности: ').split(' '))
x2, y2 = map(int, input('Введите центр второй окружности: ').split(' '))
r1 = int(input('Введите радиус первой окружности: '))
r2 = int(input('Введите радиус второй окружности: '))

d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

tr.color('black')
tr.penup()
tr.goto(x1, y1)
tr.forward(r1)
tr.left(90)
tr.pendown()
tr.circle(r1)

tr.penup()
tr.goto(x2, y2)
tr.forward(r2)
tr.left(90)
tr.pendown()
tr.circle(r2)

tr.penup()
tr.goto(100, 100)
if d > r1 + r2:
    tr.write('Окружности лежат одна вне другой, не касаясь')
elif d == r1 + r2:
    tr.write('Окружности имеют внешнее касание')
elif abs(r1 - r2) < d < r1 + r2:
    tr.write('Окружности пересекаются')
elif 0 < d < abs(r1 - r2):
    tr.write('Одна окружность лежит внутри другой, не касаясь')
elif d == abs(r1 - r2):
    tr.write('Окружности имеют внутреннее касание')

