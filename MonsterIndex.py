# Monster Code
# Zach Golik, Brianna Melius
# April 9, 2015
# A thing for stuff

class Monster(object):
    def __init__(self, name, xp, rangedAtk, rangedDieNum, rangedDieSide,
                 rangedMod, meleeAtk, meleeDieNum, meleeDieSide, meleeMod,
                 strength, dex, con, intelligence, wis, cha, size, CMB, CMD,
                 armorClass, fort, ref, will, speed, hp, cr, sprite):
        self.name = name
        self.xp = xp
        self.rangedAtk = rangedAtk
        self.rangedDieNum = rangedDieNum
        self.rangedDieSide = rangedDieSide
        self.rangedMod = rangedMod
        self.meleeAtk = meleeAtk
        self.meleeDieNum = meleeDieNum
        self.meleeDieSide = meleeDieSide
        self.meleeMod = meleeMod
        self.str = strength
        self.dex = dex
        self.con = con
        self.intelligence = intelligence
        self.wis = wis
        self.cha = cha
        self.size = size
        self.CMB = CMB
        self.CMD = CMD
        self.armorClass = armorClass
        self.fort = fort
        self.ref = ref
        self.will = will
        self.speed = speed
        self.hp = hp
        self.cr = cr
        self.sprite = sprite

    def __str__(self):
        rep = self.name + "\n" + "\tXP: " + str(self.xp) + "\n"
        rep += "\tCR: " + str(self.cr) + "\n"
        return rep

# Dictionaries by level
class Monster_List(object):
    def __init__(self):
        self.levelOne = {}
        self.levelTwo = {}
        self.levelThree = {}
        self.populate()

    # Add level zero - one monsters
    def add_one(self, one):
        self.levelOne[one.name] = one

    # Add level two monsters
    def add_two(self, two):
        self.levelTwo[two.name] = two

    # Add level three monsters
    def add_three(self, three):
        self.levelThree[three.name] = three

    # Print level zero - one monsters
    def print_levelOne(self):
        listOfKeys = self.levelOne.keys()
        for monster in listOfKeys:
            print(self.levelOne[monster])

    # Print level two monsters
    def print_levelTwo(self):
        listOfKeys = self.levelTwo.keys()
        for monster in listOfKeys:
            print(self.levelTwo[monster])

    # Print level three monsters
    def print_levelThree(self):
        listOfKeys = self.levelThree.keys()
        for monster in listOfKeys:
            print(self.levelThree[monster])

    #Populate the dictionaries
    def populate(self):
        Level_One = open('Level 0 - 1 Monsters', 'r')
        for line in Level_One:
            line.strip()
            data = line.split(',')
            monster_data = Monster(data[0], int(data[1]), int(data[2]),
                                   int(data[3]), int(data[4]), int(data[5]),
                                   int(data[6]), int(data[7]), int(data[8]),
                                   int(data[9]), int(data[10]), int(data[11]),
                                   int(data[12]), int(data[13]), int(data[14]),
                                   int(data[15]), int(data[16]), int(data[17]),
                                   int(data[18]), int(data[19]), int(data[20]),
                                   int(data[21]), int(data[22]), int(data[23]),
                                   int(data[24]), float(data[25]), data[26])
            self.add_one(monster_data)
        Level_One.close()

        Level_Two = open('Level Two Monsters', 'r')
        for line in Level_Two:
            line.strip()
            data = line.split(',')
            monster_data = Monster(data[0], int(data[1]), int(data[2]),
                                   int(data[3]), int(data[4]), int(data[5]),
                                   int(data[6]), int(data[7]), int(data[8]),
                                   int(data[9]), int(data[10]), int(data[11]),
                                   int(data[12]), int(data[13]), int(data[14]),
                                   int(data[15]), int(data[16]), int(data[17]),
                                   int(data[18]), int(data[19]), int(data[20]),
                                   int(data[21]), int(data[22]), int(data[23]),
                                   int(data[24]), int(data[25]), data[26])
            self.add_two(monster_data)

        Level_Two.close()

        Level_Three = open('Level Three Monsters', 'r')
        for line in Level_Three:
            line.strip()
            data = line.split(',')
            monster_data = Monster(data[0], int(data[1]), int(data[2]),
                                   int(data[3]), int(data[4]), int(data[5]),
                                   int(data[6]), int(data[7]), int(data[8]),
                                   int(data[9]), int(data[10]), int(data[11]),
                                   int(data[12]), int(data[13]), int(data[14]),
                                   int(data[15]), int(data[16]), int(data[17]),
                                   int(data[18]), int(data[19]), int(data[20]),
                                   int(data[21]), int(data[22]), int(data[23]),
                                   int(data[24]), int(data[25]), data[26])
            self.add_three(monster_data)
        Level_Three.close()

#TestMain
#monsters = Monster_List()
#print("LEVEL ONE\n")
#monsters.print_levelOne()
#print("LEVEL TWO\n")
#monsters.print_levelTwo()
#print("LEVEL THREE\n")
#monsters.print_levelThree()
