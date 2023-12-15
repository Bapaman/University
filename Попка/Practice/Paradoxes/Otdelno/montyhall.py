import random

def montyhall(gamer):
    i = 0
    guest_ugadal = 0
    guest_neugadal = 0

    while i < gamer:
        # Представим, что это тройки дверей (1, 2, 3)
        prize = random.randrange(1, 4)
        guest = random.randrange(1, 4)

        if prize == guest:
            guest_ugadal += 1
        else:
            guest_neugadal += 1
        i += 1

    probability_change = (guest_neugadal / gamer) * 100
    probability_no_change = (guest_ugadal / gamer) * 100

    return f'Вероятность того, что игрок обнаружит приз, согласившись на изменение двери: {probability_change:.2f}%\nВероятность того, что игрок обнаружит приз, не согласившись на изменение двери: {probability_no_change:.2f}%'

if __name__ == "__main__":
    print(montyhall())
