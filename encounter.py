###############################################################################
# Module Encounter.py                                                         #
# written by Thorin Schmidt                                                   #
# 3/17/2015                                                                   #
#   Written for the "CIS Class Project 2015".                                 #
###############################################################################
import MonsterIndex
import random 

class EncounterGroup(object):
    """ base class for the monster(s) that make(s) up an encounter. """
    # Monsters are stored in a dictionary.  A separate keylist is maintained
    # for ease of use. Name is the name of the encounter, while description
    # is a longer, more detailed text. CR is the Challenge Rating, and totalXP
    # is, of course, the XP for the encounter. 
    
    def __init__(self, level, name, listOfMonsters,
                 dictOfMonsters, descr):
        self._level = level  #Level of the encounter as a whole
        self._name = name    #Short Name
        self._number = len(listOfMonsters)
        self._encounterList = listOfMonsters
        self._encounterDict = dictOfMonsters
        self._description = descr
        self._totalXP, self._CR = self._calcXPandCR()

    def __str__(self):
        """ return a string for use in print()"""
        rep = "You are facing: " + self._name + "\n"
        for name in self._keyList:
            rep += name + "\t XP: "+ str(self._encounterDict[name].xp) + "\n"
        rep += "Total XP:  " + str(self._totalXP) + "\n"
        rep += "Total CR:  " + str(self._CR) + "\n"
        return rep 

    def _calcXPandCR(self):
        """Query the monster database to calculate group XP and CR."""
        
        XP_total = 0
        CR_total = 0.0
        for monster in self._keyList:
            XP_total += self._encounterDict[monster].xp
            CR_total += self._encounterDict[monster].cr

        CR_total = int(CR_total)

        return XP_total, CR_total

    
class EncounterGenerator(object):
    """ Class to generate random (and set?) encounters by Challenge Rating"""

    def __init__(self):
        self._theMonsters = MonsterIndex.Monster_List()
        

    def createEncounter(self,CRvalue):
        """ creates a semi-random encounter based on a given CR value."""
        keyList = []
        encounterList = []
        levelOneKeys = self._theMonsters.levelOne.keys()
        levelTwoKeys = self._theMonsters.levelTwo.keys()
        levelThreeKeys = self._theMonsters.levelThree.keys()
        modifier = None
        roll = random.randrange(100)
        if roll in range(10):
            modifier = -1       # Easier encounter
        elif roll in range(90):
            modifier = 0        # Normal encounter
        else:
            modifier = 1        # Harder encounter

        CR = CRvalue + modifier
        #make sure CR never goes lower than 1
        if CR < 1:
            CR = 1
        print(CR)

        while CR > 0:
            candidates = []
            candidatesKeys = []
            for name in levelOneKeys:
                if self._theMonsters.levelOne[name].cr <= CR:
                    candidatesKeys.append(name)
                    candidates.append(self._theMonsters.levelOne[name])
            for name in levelTwoKeys:
                if self._theMonsters.levelTwo[name].cr <= CR:
                    candidatesKeys.append(name)
                    candidates.append(self._theMonsters.levelTwo[name])
            for name in levelThreeKeys:
                if self._theMonsters.levelThree[name].cr <= CR:
                    candidatesKeys.append(name)
                    candidates.append(self._theMonsters.levelThree[name])
            if candidates == []:
                CR = 0
            else:
                
                    
                random.shuffle(candidates)
                member = random.choice(candidates)
                encounterList.append(member)
                keyList.append(member.name)
                CR -= member.cr
                
        print(keyList)

#TestMain
g = EncounterGenerator()

g.createEncounter(2)



