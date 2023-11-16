import math
def birthday(people):
    def calc(people):
        comb = math.comb(people, 2)
        prob = 1 - math.exp(-comb / 365.0)
        return prob
    return calc(people) * 100
people = int(input("Введите количество людей в группе: "))
iterations = int(input("Введите количество итераций: "))
result = 0
for _ in range(iterations):
    result += birthday(people)
avg = result / iterations
print(f"Средняя вероятность совпадения дней рождения для группы из {people} человек: {avg:.2f}%")

import random
gamer = int(input('Введите колличество итераций: '))

def montyhall(gamer):
    i = 0
    guestugadal = 0
    guestneugadal = 0
    while i<gamer:
        have = random.randrange(1,4)
        guest = random.randrange(1,4)
        if have==guest:
            guestugadal+=1
        else:
            guestneugadal+=1
        i+=1
    return f'Вероятность того, что игрок обнаружит приз согласившись на изменение двери - {str((guestneugadal/gamer)*100)}%\nВероятность того, что игрок обнаружит приз не согласившись на изменение двери - {str((guestugadal/gamer)*100)}%'
print (montyhall(gamer))
