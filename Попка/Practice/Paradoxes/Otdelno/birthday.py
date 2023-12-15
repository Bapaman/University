import math

def birthday(people, iterations):
    def calc(people):
        comb = math.comb(people, 2)
        prob = 1 - math.exp(-comb / 365.0)
        return prob * 100

    result = 0
    for _ in range(iterations):
        result += calc(people)

    avg = result / iterations
    return avg

if __name__ == "__main__":
    people = int(input("Введите количество людей в группе: "))
    iterations = int(input("Введите количество итераций: "))

    average_probability = birthday(people, iterations)

    print(f"Средняя вероятность совпадения дней рождения для группы из {people} человек: {average_probability:.2f}%")
