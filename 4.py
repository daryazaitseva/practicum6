cage = input('Введите значение клетки шахматного поля: ')
if cage[0] in 'aceg' and cage[1] in '1357':
    print('черный')
elif cage[0] in 'aceg' and cage[1] in '2468':
    print('белый')
elif cage[0] in 'bdfh' and cage[1] in '1357':
    print('белый')
else:
    print('черный')