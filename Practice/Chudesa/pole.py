import random
game = True
record+=1
with open(f'slovar.txt',encoding="utf-8") as f:
   slova = f.read().split()
while game==True:
    while True:
        c = input('Выберите уровень сложности\nЛегкий - 7 жизней: введите 1\nСредний- 5 жизней: введите 2\nСложный - 3 жизни: введите 3\n')
        if c == '1':
            jizn = 7
            break
        elif c == '2':
            jizn = 5
            break
        elif c == '3':
            jizn = 3
            break
        else:
            print ('Ошибка, введите корректное значение!')
    slovo = random.choice(slova)
    x = len(slovo)
    mask = (len(slovo)) * '■'
    ugad = ''
    while jizn != 0 and mask!=slovo:
        vvod = input('Введите букву или слово! ')
        if len(vvod)==1:
            if vvod in slovo:
                for i in range(0, x):
                    if slovo[i] == vvod:
                        ugad = mask[:i] + vvod + mask[i + 1:]
                        mask = ugad
                print ('Вы угадали букву! У вас',jizn,'жизней!')
            else:
                print('Вы не угадали букву!')
                jizn -= 1
                print('Количество ваших жизней =', jizn)
            print (mask)
        else:
            if vvod == slovo:
                print ('Вы угадали слово и выиграли автомобиль!')
                mask = slovo
                record+=1
            else:
                jizn=0
    if jizn == 0:
        print (f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nВы проиграли! Было загадано слово - {slovo}\nК сожалению, вы потеряли возможность выиграть АВТОМОБИЛЬ!(\n\n\n')
    elif mask == slovo:
        print ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nПоздавляю! Вы победили в программе "Поле чудес"! \nВы выиграли автомобиль!\n\n')
    b = input('Сыграть еще раз - 1:\nПрекратить игру - 2: ')
    if b != '1':
        game = False
        if record >= def(reader):
