import reader
import re
x = 1
jizn = 0
schet = 0
ispolz = []
choose = (re.sub("[^0-9а-я]", "", (input(f'Выберите уровень сложности:'
              f'\n 1. Легко  - 7 жизней'
              f'\n 2. Средне - 5 жизней'
              f'\n 3. Сложно - 3 жизни\n')).lower()))

while x == 1:
    end = False
    match choose:
        case '1' | 'легко':
            jizn = 7
        case '2' | 'средне':
            jizn = 5
        case '3' | 'сложно':
            jizn = 3
    ispolz.clear()
    word = (reader.word())
    if word == 'exception':
        print(f'Похоже, что вы отгадали все слова! \n0_0\nСтолько очков вам удалось набрать: {schet}')
        break
    print(f'Загаданное слово состоит из {len(word)} букв')
    answer = '\u25a0'*len(word)
    while jizn != 0 and answer != word:
        print('\n\n'+answer)
        lolo = re.sub("[^А-я]", "", (input('Введите одну букву или слово целиком: ')))
        if lolo in(ispolz) and len(lolo)==1:
            print('Вы уже вводили эту букву!')
        elif lolo in(ispolz) and len(lolo)!=1:
            print('Вы уже вводили это слово!')
        else:
            ispolz.append(lolo)
            if lolo not in word and len(lolo)==1:
                jizn -= 1
                print(f'К сожалению, такой буквы в слове нет!\n\nЕще осталось {jizn} жизней')
            elif lolo not in word and len(lolo) != 1:
                jizn = 0
                print(f'К сожалению, загадано не это слово!\n\nВы проиграли!')
            elif lolo == word:
                print(f'Вы угадали слово {word} целиком!\n У вас было в запасе еще столько жизней: {jizn}')
                answer = lolo
            elif lolo in word and len(lolo)==1:
                print(f'Вы угадали букву!\nЖизней в запасе: {jizn}')
                for i in range(0,len(word)):
                    if word[i] == lolo:
                        answer1 = answer[:i]+lolo+answer[i+1:]
                        answer = answer1
        if answer == word:
            schet += 1
            end = True
        elif jizn == 0:
            end = True
        if end == True:
            new_game = re.sub("[^0-9А-я]", "", (input(f'\n\nБыло загадано слово {word}\nСтолько очков вы набрали: {schet}\nХотите сыграть еще?'
                                                       f'\n1.Да'
                                                       f'\n2.Нет\n')).lower())
            match new_game:
                case '1'|'да':
                    game = True
                case _:
                    game = False
if x == False:
    with open(f'best_schet.txt','r') as f:
        record = int(f.read().replace('\n',''))
    if record < schet:
        with open(f'best_schet.txt', 'w') as f:
            f.write(str(schet))
