from books import *


def show():
    format_data = (data('books.csv'))
    for i in format_data:
        print(i)
    while True:
        a = input('\n\nЧто вы хотите сделать?\n1. Найти книгу по слову\n2. Узнать стоимость\n3. Выход\n')
        if a == '1':
            arr = get_books(format_data, input('Введите ключевое слово: ').strip())
            if len(arr) == 0:
                print('Таких книг нет')
            else:
                print(arr)
        elif a == '2':
            try:
                print(get_totals(format_data, int(input('Введите число: '))))
            except ValueError:
                print('Это не число!')
        else:
            exit()
