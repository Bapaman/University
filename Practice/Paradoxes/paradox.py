import random
gamer = int(input())
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
print ('Вероятность того, что игрок обнаружит приз согласившись на измнение двери-',str((guestneugadal/gamer)*100),'%')
print ('Вероятность того, что игрок обнаружит приз не согласившись на измнение двери-',str((guestugadal/gamer)*100),'%')
