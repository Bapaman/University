def read(nazv_file):
    try:
        spisok = open(nazv_file, 'r')
        linii = spisok.readlines()
        spisok.close()
        numbers = [int(line.strip()) for line in linii]

        if numbers[0] != len(numbers) - 1:
            raise ValueError("Первое число не совпадает с количеством чисел в файле")
        return numbers
    except FileNotFoundError:
        print(f"Ошибка: Файл {nazv_file} не найден.")
    except ValueError as e:
        print(f"Ошибка: Невозможно преобразовать строку в число. {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
nazv_file = input("Введите имя файла: ")
numbers = read(nazv_file)
if numbers:
    print(f"Список чисел из файла: {numbers}")
