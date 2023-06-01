while True:

    x = int(input('Введите число: '))
    y = int(input('Введите второе число: '))
    c = int(input('Что делаем 1/2/4 ? '))
    if c == 1:
        print('Ответ', x * y)
    elif c == 2:
        print('Ответ', x + y)
    else:
        c == 4
        print('Закончили)')
        break

