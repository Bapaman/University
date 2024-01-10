import random

with open(f'slovar.txt', encoding="utf-8") as f:
   slovar = f.read().split()
def word():
   if len(slovar) != 0:
      choose = random.choice(slovar)
      slovar.remove(choose)
      return(choose)
   else:
      return('exception')

