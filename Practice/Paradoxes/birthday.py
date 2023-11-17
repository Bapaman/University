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
