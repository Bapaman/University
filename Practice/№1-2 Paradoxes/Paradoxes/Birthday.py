import random
import re

def DNIROJD(num_people, num_repeats):

    num_collisions = 0  # количество групп с повторяющимися днями рождения
    for _ in range(num_repeats):
        unique_days = set()
        for _ in range(num_people):
            unique_days.add(random.randint(1, 365))

        if len(unique_days) != num_people:
            num_collisions += 1

    collision_percentage = (num_collisions / num_repeats) * 100
    return (f'Количество групп с как минимум двумя человеками с одинаковыми днями рождения:'f' {num_collisions}'
            f'\nПроцент групп с как минимум двумя человеками с одинаковыми днями рождения: {format(collision_percentage, ".2f")}%')

if __name__ == '__main__':
    num_people = int(re.sub("[^0-9]", "", input('Введите количество людей в группе: ')))
    num_repeats = int(re.sub("[^0-9]", "", input('Введите количество повторений: ')))
    print(DNIROJD(num_people, num_repeats))
