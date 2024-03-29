import turtle as tr

x1, y1 = map(int, input('Введите координаты верхней левой вершины 1 прямоугольника: ').split(' '))
x2, y2 = map(int, input('Введите координаты нижней правой вершины 1 прямоугольника: ').split(' '))
x3, y3 = map(int, input('Введите координаты верхней левой вершины 2 прямоугольника: ').split(' '))
x4, y4 = map(int, input('Введите координаты нижней правой вершины 1 прямоугольника: ').split(' '))

tr.color('black')
tr.penup()
tr.goto(x1, y1)
tr.right(90)
tr.pendown()
tr.forward(abs(x1 - x2))
tr.right(90)
tr.forward(abs(y1 - y2))
tr.right(90)
tr.forward(abs(x1 - x2))
tr.right(90)
tr.forward(abs(y1 - y2))
tr.penup()

tr.goto(x3, x4)
tr.right(90)
tr.pendown()
tr.forward(abs(x3 - x4))
tr.right(90)
tr.forward(abs(y3 - y4))
tr.right(90)
tr.forward(abs(x3 - x4))
tr.right(90)
tr.forward(abs(y3 - y4))
tr.penup()

tr.goto(100, 100)
if (abs(x1 - x2) > abs(x1 - x3)) and (abs(y1 - y2) > abs(y1 - y3)):
    tr.write('Прямоугольники лежат вне друг друга, не касаясь')
elif (abs(x1 - x2) == abs(x1 - x3)) or (abs(y1 - y2) == abs(y1 - y3)):
    tr.write('Прямоугольники имеют касание')
elif (abs(x1 - x2) < abs(x1 - x3)) or (abs(y1 - y2) < abs(y1 - y3)):
    tr.write('Прямоугольники имеют касание')
elif (abs(x1 - x2) < abs(x1 - x3)) and (abs(y1 - y2) == abs(y1 - y3)):
    tr.write('Один прямоугольник лежит внутри другого, не касаясь')