import random
class Game:
    def __init__(self):
        self.barrels = []

        self.barl = ''

        self.name = ""

        self.pl1 = []

        self.ai = []

    """Гененрация бочонков!"""
    def genbarrels(self):
        for i in range(91):
            self.barrels.append(i)

        self.barrels.remove(0)

    """Код одного хода!"""

    def charname(self):
        a = 1
        while a == 1:
            self.name = str(input("Ваш ник:"))
            if self.name == "":
                print("Вы не указали свой ник-нейм")
            else:
                a = a - 1
                print(f"Поздравляю, ваш ник \"{self.name}\"")
    def gencart(self):
        for i in range(3):
            row = random.sample(range(1, 90), 5)
            row.sort()
            for i in range(4):
                row.insert(random.randint(0, len(row)), "")
            self.pl1.append(row)

        for i in range(3):
            row = random.sample(range(1, 90), 5)
            row.sort()
            for i in range(4):
                row.insert(random.randint(0, len(row)), "")
            self.ai.append(row)

    def rungame(self):

        while True:
            self.barl = random.choice(self.barrels)
            self.barrels.remove(self.barl)
            print(f"Новый бочонок: {self.barl} (Осталось:{len(self.barrels)})")




            print("--" * 20)
            print("Ваша карта:")
            a = (f"{self.pl1[0]} \n {self.pl1[1]} \n {self.pl1[2]}")
            print(a)
            print("--" * 20)


            print("Карта компьютера".center(20,"-"))
            a = (f"{self.ai[0]} \n {self.ai[1]} \n {self.ai[2]}")
            print(str(a))
            print("--" * 20)

            if self.barl not in self.ai[0] or self.barl not in self.ai[1] or self.barl not in self.ai[2]:
                pass
            else:
                self.ai.remove(self.barl)

            pl1 = str(input("Зачеркнуть?Y/N"))
            if pl1.lower() == "y":
                if self.barl in self.pl1[0] or self.barl in self.pl1[1] or self.barl in self.pl1[2]:
                    self.pl1.remove(int(self.barl))
                    print("Продолжение..")
                else:
                    print(f"{self.name} проиграл!")
                    return False
            elif pl1.lower() == "n":
                if self.barl not in self.pl1[0] or self.barl not in self.pl1[1] or self.barl not in self.pl1[2]:

                    print("продолжим!")
                else:
                    print(f"{self.name} проиграл!")
                    return False


tom = Game()
tom.charname()
tom.gencart()

tom.genbarrels()

tom.rungame()









