phone_book = {}


def format_name(name):
    formatted_name = ' '.join(word.capitalize() for word in name)
    return formatted_name

def format_number(number):
    if number[0] == '8':
        number = number.replace('8', '+7', 1)
    return number

def display_contacts(phone_book):
    for index, (name, number) in enumerate(phone_book.items(), start=1):
        print(f"{index}. {name}: {number}")


def add_contact(phone_book):
    while True:
        full_name = input('Введите имя и фамилию в формате *Имя Фамилия*: ').split()
        if len(full_name) == 2 and all(word.isalpha() for word in full_name):
            break
        else:
            print('Неправильно введены данные! Пожалуйста, введите имя и фамилию, содержащие только буквы.')

    phone_number = input('Введите номер телефона пользователя: ')
    while not ((len(phone_number) == 11 and phone_number[0] == '8' and phone_number.isdigit()) or
               (len(phone_number) == 12 and phone_number[0:2] == '+7' and phone_number[1:].isdigit())):
        phone_number = input('Неправильно введен номер! Пожалуйста, введите номер еще раз: ')

    full_name = format_name(full_name)
    phone_number = format_number(phone_number)

    phone_book[full_name] = phone_number
    print('Контакт успешно добавлен!')
    display_menu()

def delete_contact(phone_book):
    display_contacts(phone_book)
    contact_index = input('Введите номер контакта для удаления: ')

    if contact_index.isdigit() and 1 <= int(contact_index) <= len(phone_book):
        contact_to_delete = list(phone_book.keys())[int(contact_index) - 1]
        del phone_book[contact_to_delete]
        print('Контакт успешно удален!')
    else:
        print('Неправильный номер контакта.')

    display_menu()

def view_contacts(phone_book):
    display_contacts(phone_book)
    display_menu()

def modify_contact(phone_book):
    display_contacts(phone_book)
    contact_index = input('Введите номер контакта для изменения: ')

    if contact_index.isdigit() and 1 <= int(contact_index) <= len(phone_book):
        contact_to_modify = list(phone_book.keys())[int(contact_index) - 1]
        new_phone_number = input('Введите новый номер телефона: ')
        while not ((len(new_phone_number) == 11 and new_phone_number[0] == '8' and new_phone_number.isdigit()) or
                   (len(new_phone_number) == 12 and new_phone_number[0:2] == '+7' and new_phone_number[1:].isdigit())):
            new_phone_number = input('Неправильно введен номер! Пожалуйста, введите новый номер еще раз: ')

        new_phone_number = format_number(new_phone_number)

        phone_book[contact_to_modify] = new_phone_number
        print('Номер успешно изменен!')
    else:
        print('Неправильный номер контакта.')

    display_menu()

def display_menu():
    print('\nМеню телефонной книги')
    print('1. Создать контакт')
    print('2. Удалить контакт по имени')
    print('3. Просмотреть контакты')
    print('4. Изменить контакт по имени')
    print('5. Выход')


flag = True
display_menu()

while flag:
    command = input('Введите номер команды: ')
    if command == '1':
        add_contact(phone_book)
    elif command == '2':
        delete_contact(phone_book)
    elif command == '3':
        view_contacts(phone_book)
    elif command == '4':
        modify_contact(phone_book)
    elif command == '5':
        view_contacts(phone_book)
        print('До свидания!')
        flag = False
    elif not command.isdigit() or int(command) not in [1, 2, 3, 4, 5]:
        print('Такой команды нет, попробуйте еще раз!')
        display_menu()
