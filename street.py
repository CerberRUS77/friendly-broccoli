while True:

    x = int(input('Введите число: '))
    y = int(input('Введите второе число: '))
    c = int(input('Что делаем 2/3/5 ? '))
    if c == 2:
        print('Ответ', x * y)
    elif c == 3:
        print('Ответ', x + y)
    else:
        c == 5
        print('Закончили)')
        break


