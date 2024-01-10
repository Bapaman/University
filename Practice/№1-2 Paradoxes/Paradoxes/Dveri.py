import random
import re

def DVERI(iterations):

    guest_wins = 0  # Счет побед гостя
    DVERI_wins = 0  # Счет ведущего

    for i in range(0, iterations):
        prize_behind_door = random.randint(1, 3)  # Определение двери, за которой находится приз
        guest_choice = random.randint(1, 3)  # Дверь, которую выбрал гость

        if prize_behind_door == guest_choice:  # Если гость угадал правильную дверь, то открыв ее, он получит приз (1/3)
            guest_wins += 1
        else:
            # Если гость не угадал дверь, то ведущий уберет одну дверь, за которой ничего нет.
            # Останется только дверь с призом и выбранная гостем.
            # Не угадав с первого раза, гость откроет дверь, за которой точно есть приз (2/3)
            DVERI_wins += 1

    return (f'\tЕсли бы гость придерживался своего выбора, то он получил колличество призов равное: {guest_wins} ({format((100/(iterations/guest_wins)), ".2f")}%)'
            f' \n\tИначе, гость бы получил колличество призов равное: {DVERI_wins} ({format((100/(iterations/DVERI_wins)), ".2f")}%)')


if __name__ == '__main__':
    iterations = int(re.sub("[^0-9]", "", (input('Введите количество итераций: '))))
    print(DVERI(iterations))
