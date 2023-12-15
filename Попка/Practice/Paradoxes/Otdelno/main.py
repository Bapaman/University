import re
import birthday
import montyhall

choose = str(input(f'Выберите парадокс\n1. Парадокс Монти Холла\n2. Парадокс Дней рождения\n'))
choose = choose.lower()

if choose == '1':
    gamer = int(re.sub("[^0-9]", "", (input('Введите кол-во итераций: '))))
    print(montyhall.montyhall(gamer))
elif choose == '2':
    people = int(re.sub("[^0-9]", "", (input('Введите кол-во человек в группе: '))))
    repeats = int(re.sub("[^0-9]", "", (input('Введите кол-во итераций: '))))
    average_probability = birthday.birthday(people, repeats)
    print(f"Средняя вероятность совпадения дней рождения для группы из {people} человек: {average_probability:.2f}%")
else:
    print('Неправильный выбор, выберите 1 или 2')
