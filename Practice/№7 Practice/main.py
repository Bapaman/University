import csv

# Задание 1: Функция для выбора книг по параметру из файла CSV
def get_books(search_parameter):
    books = []
    with open('books.txt', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        # Пропускаем заголовок
        next(reader)
        for row in reader:
            # Обрабатываем данные в строке
            row_data = [data.strip() for data in row]
            title = row_data[1].lower()
            if search_parameter.lower() in title:
                isbn = row_data[0]
                author_quantity_price = row_data[2:]
                author_quantity_price[1] = int(author_quantity_price[1])  # преобразуем количество в целое число
                author_quantity_price[2] = float(author_quantity_price[2]) # преобразуем цену в число с плавающей точкой
                books.append([isbn] + [title] + author_quantity_price)
    return books

# Задание 2: Функция для вычисления суммарной стоимости каждой книги
def get_totals(books_list):
    totals = []
    for book in books_list:
        isbn, title, author, quantity, price = book
        total_price = quantity * price
        totals.append((isbn, total_price))
    return totals

# Задание 3: Функция для добавления фиксированного значения к сумме, если она ниже определенного числа
def augment_totals(totals_list, threshold, increment):
    adjusted_totals = []
    for isbn, total in totals_list:
        adjusted_total = total if total >= threshold else total + increment
        adjusted_totals.append((isbn, adjusted_total))
    return adjusted_totals

# Пример использования функций
search_param = 'python'
books_filtered = get_books(search_param)
totals = get_totals(books_filtered)
augmented_totals = augment_totals(totals, 500, 100)

# Печатаем результаты
print("Filtered books:")
for book in books_filtered:
    print(book)
print("\nTotals:")
for total in totals:
    print(total)
print("\nAugmented Totals (<500 augmented by 100):")
for augmented_total in augmented_totals:
    print(augmented_total)
