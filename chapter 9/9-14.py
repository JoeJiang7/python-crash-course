from random import randint


class Die():
    def __init__(self,sides = 6):
        Die.sides = sides

    def roll_die(self):
        number = randint(1,Die.sides)
        return number


digits1 = Die(6)
for i in range(1,11):
    print(digits1.roll_die())
print("\n")
digits2 = Die(10)
for i in range(1,11):
    print(digits2.roll_die())
print("\n")
digits3 = Die(20)
for i in range(1,11):
    print(digits2.roll_die())