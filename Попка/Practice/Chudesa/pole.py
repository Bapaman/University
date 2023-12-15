import random
with open(f'slovar.txt',encoding="utf-8") as f:
   slova = f.read().split()
while True:
    slovo = random.choice(slova)
    x = len(slovo)
    mask = (len(slovo)) * '*'
    ugad = ''
    jizn = 6
    while jizn != 0 and mask!=slovo:
        vvod = input('Введите букву! ')
        if vvod in slovo:
            for i in range(0, x):
                if slovo[i] == vvod:
                    ugad = mask[:i] + vvod + mask[i + 1:]
                    mask = ugad
            print ('Вы угадали букву! У вас',jizn,'жизней!')
        else:
            print('Вы не угадали букву!')
            print (slovo)
            jizn -= 1
            print('Количество ваших жизней =', jizn)
        print (mask)
    if jizn == 0:
        print ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nВы проиграли!\n К сожалению, вы оказались в том случае ,когда автомобиль - вы не выиграли!(\n\n\n')
    elif mask == slovo:
        print ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nПоздавляю! Вы победили в программе "Поле чудес"! \nВы выиграли автомобиль!\n\n')
