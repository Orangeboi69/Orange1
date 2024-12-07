import sys,os,time,random,json
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

Banned_Name = [' ', 'nigga','hurensohn','wichser',
                'null','none','true','false','no','in',
                'yes','null',"'",""
                ]
Level_to_xp = {
    "1":25,
    "2":40,
    "3":50,
    "4":75,
    "5":100,
    "6":125,
    "7":150,
    "8":200,
    "9":250,
    "10":300
}

def GamePrint(txt):
    for char in txt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.035)
    print("")
    time.sleep(0.5)

def YN():
    GamePrint("Type" + color.GREEN + color.BOLD + ' Y ' + color.END + "for yes.")
    GamePrint("Type" + color.RED + color.BOLD + ' N ' + color.END + "for No.")

def EnterYN():
    GamePrint("Please enter " + color.GREEN + "'y'" + color.END + ' or ' + color.RED + "'n'"+ color.END + ".")


class Weapon(object):
    def __init__(self, name, amount, multiplier):
        self.name = name
        self.amount = amount
        self.multiplier = multiplier

class Armor(object):
    def __init__(self,name,amount,multiplier):
        self.name = name
        self.amount = amount
        self.multiplier = multiplier

class Monster(object):
    def __init__(self,name,lvl,atk,hp,xp,weapon):
        self.name = name
        self.lvl = lvl
        self.atk = atk
        self.hp = hp
        self.xp = xp
        self.weapon = weapon

class Player(object):
    class Stats(object):
        def __init__(self,ATK,HP,MAXHP,MP,MAXMP,DEF,NAME,LVL,XP):
            self.atk = ATK
            self.hp = HP
            self.maxH = MAXHP
            self.mp = MP
            self.maxM = MAXMP
            self.df = DEF
            self.names = NAME
            self.lvl = LVL
            self.XP = XP
            if XP >= Level_to_xp[str(LVL)]:
                LVL += 1
                XP -= Level_to_xp[str(LVL)]
    class Skill(object):
        def __init__(self,name,useMPstat,multi,MPcost):
            self.name = name
            self.useMP = useMPstat
            self.multiplier = multi
            self.cost = MPcost
    class Inventory:
        class Equip(object):
            def __init__(self,Weapon,Armor):
                self.Weapon = Weapon
                self.Armor = Armor
        class Food(object):
            def __init__(self,name,amount,healHP,healMP):
                self.name = name
                self.amount = amount
                self.healHP = healHP
                self.healMP = healMP
#Weapon-data
Leather_Cloth = Armor("Cloth",1,1)
Basic_Armor = Armor("Basic Armor",0,1.5)
dev_Armor = Armor("Debug Armor",0,10)

fist = Weapon("hand", amount=1,multiplier=1)
wooden_sword = Weapon("wooden sword",amount=0,multiplier=2)
iron_sword = Weapon("iron sword",amount=0,multiplier=3.5)
reinforged_sword = Weapon("reinforged sword",amount=0,multiplier=5)
dev_sword = Weapon(color.DARKCYAN + "Debug Sword" + color.END,amount=0, multiplier=10)

#Skill
Fire = Player.Skill("fire",True,2,5)
Ice = Player.Skill("ice",True,2,3)
#start
P_Stats = Player.Stats(15,100,100,25,25,15,"",1,0)
P_Inv = Player.Inventory.Equip(wooden_sword,Leather_Cloth)
#def
#Fight Stats:
#   Damage = ATK (+Skill) * lvlmulti * SwordMulti
#   EnemyDMG = (EATK * weapon multiplier) * 100 - (P_DEF / 100)
def choose(Q,ifyes_Say,ifno_Say,Value):
    GamePrint(Q)
    YN()
    Ans = input()
    while True:
        if Ans == "y":
            GamePrint(ifyes_Say)
            Value = True
            break
        elif Ans == "n":
            GamePrint(ifno_Say)
            Value = False
            break
        elif 1 != len(Ans) or Ans != 'y' or Ans != 'n':
            EnterYN()
            continue
    return Value

def recover():
    P_Stats.hp = P_Stats.maxH
    GamePrint("Your " + color.RED + "HP" + color.END + " is healed by " + color.BOLD + color.UNDERLINE + str(P_Stats.maxH - P_Stats.hp) + color.END + ".")
    P_Stats.mp = P_Stats.maxM
    GamePrint("Your " + color.BLUE + "MP" + color.END + " is healed by " + color.BOLD + color.UNDERLINE + str(P_Stats.maxM - P_Stats.mp) + color.END + ".")

def addxp(amount):
    P_Stats.XP += amount
    while Level_to_xp[str(P_Stats.lvl)] <= P_Stats.XP:
        P_Stats.lvl += 1
        P_Stats.XP -= Level_to_xp[str(P_Stats.lvl)]
        if P_Stats.lvl < 6:
            GamePrint("You leveled up to " + color.BOLD + str(P_Stats.lvl) + color.END)

def fight(Monster,speicial):
    _run = False
    _surrender = False
    MonsterXP = Monster.xp
    Dummy_End = False
    C_rate = 1
    Monster_Name = Monster.name
    Lvl_Multi = 1 + P_Stats.lvl / 10
    PlayerDamage = P_Stats.atk * Lvl_Multi * P_Inv.Weapon.multiplier
    MonsterDamage = Monster.atk * Monster.weapon.multiplier
    PlayerHP = P_Stats.hp
    MonsterHP = Monster.hp
    PlayerMP = P_Stats.mp
    PlayerDF = P_Stats.df
    PlayerName = P_Stats.names
    MonsterDamage_to_player = MonsterDamage * (1 - (PlayerDF / 100))
    Inf_DMG = PlayerDamage ** 12
    if speicial != "dummy":
        Intro = [color.BOLD + Monster_Name + color.END + " appeared!", "A wild " + color.BOLD + Monster_Name + color.END + " appeared.", "You have encountered a " + color.BOLD + Monster_Name + color.END]
        _x = random.choice(Intro)
        GamePrint(_x)
    while MonsterHP > 0 and PlayerHP > 0 and _run == False:
        GamePrint(color.BOLD + "Options:" + color.END)
        GamePrint(color.RED + color.BOLD + "    1" + color.END + " to fight.")
        GamePrint(color.BLUE + color.BOLD + "    2" + color.END + " to use skill.")
        GamePrint(color.BOLD + "    3" + color.END + " to run away")
        GamePrint(color.BOLD + color.YELLOW + "    4" + color.END + " to surrender.")
        GamePrint(color.BOLD + color.DARKCYAN + "    5" + color.END + " to do nothing.")
        #Player-Action
        while True:
            FoSoR = input()
            if FoSoR == "1":
                GamePrint("You choose to " + color.BOLD + "fight" + color.END + ".")
                Crit = random.randint(C_rate,100)
                if Crit <= 90:
                    MonsterHP -= PlayerDamage
                    GamePrint("You swing you sword and dealt " + color.BOLD + str(PlayerDamage) + color.END + " damage.")
                    C_rate += 1
                    break
                if Crit >= 90:
                    CDMG = PlayerDamage * random.randint(2,4)
                    MonsterHP -= CDMG
                    C_rate = 1
                    GamePrint(color.RED + color.BOLD + "Critical hit!" + color.END + " You give the enemy a heavy hit, you dealt " + color.RED + color.BOLD + str(CDMG) + color.END + " damage.")
                    break
            elif FoSoR == "2":
                GamePrint("You choose to " + color.BOLD + "use a skill" + color.END + ".")
                GamePrint("You have " + color.BOLD + str(len(Skill_List)) + color.END + " skills")
                while True:
                    a = 1
                    for s in Skill_List:
                        GamePrint(str(a) + " - " + color.BOLD + s + color.END)
                        a += 1
                    GamePrint("Type in the number before the skill to use it.")
                    Skill_Choise = input()
                    if int(Skill_Choise) <= len(Skill_List):
                        _Skills = Num_to_Skill[Skill_Choise]
                        SPDMG = PlayerDamage * _Skills.multiplier
                        MonsterHP -= SPDMG
                        if _Skills.useMP == True:
                            PlayerMP -= _Skills.cost
                        GamePrint("You used " + color.BOLD + _Skills.name + color.END + " and dealt " + color.RED + color.BOLD + str(SPDMG) + color.END + " damage.")
                        break
                    else:
                        GamePrint("Please enter a valid number!")
                        continue
                break
            elif FoSoR == "3":
                GamePrint("You choose to " + color.BOLD + "run away" + color.END + ".")
                _run = True
                break
            elif FoSoR == "4":
                if speicial != "tutorial":
                    GamePrint("You choose to " + color.BOLD + "surrender" + color.END + ".")
                    _surrender = True
                    break
                else:
                    GamePrint("This is a tutorial, so you" + color.BOLD + " cannot surrender" + color.END + ".")
                    GamePrint("Please enter" + color.BOLD + " 1,2,3" + color.END + "or" + color.BOLD + " 5" + color.END)
                    continue
            elif FoSoR == "5":
                GamePrint("You choosed to " + color.BOLD + "do nothing." + color.END)
                break
            elif speicial == "dummy" and FoSoR == "end":
                GamePrint(color.BOLD + "ending..." + color.END)
                Dummy_End = True
                break
            else:
                GamePrint("Please enter " + color.BOLD + color.RED + "1,2,3,4" + color.END + " or " + color.BOLD + color.RED + "5" + color.END + ".")
                continue
        #Monster-Action
        if MonsterHP <= 0 or Dummy_End == True:
            Win = True
            break
        if _surrender == True:
            PlayerHP -= Inf_DMG
            GamePrint(color.BOLD + PlayerName + color.END + " did " + color.RED + color.BOLD + str(Inf_DMG) + color.END + " damage.")
            Win = False
            break
        if PlayerHP <= 0:
            if speicial != "tutorial":
                break
            else:
                GamePrint(color.BOLD + "Dying in a tutorial?" + color.END)
                GamePrint(color.BOLD + "Wow you're so 'skilled'!" + color.END)
                GamePrint("Still, this is a tutorial, so you will be " + color.BOLD + "revived." + color.END)
                PlayerHP = P_Stats.maxH
                continue
        if _run == True:
            _sr = random.randint(1,100)
            if _sr >= 10:
                GamePrint(color.BOLD + color.GREEN + "You sucessfully got away." + color.END)
                Win = True
                break
            else:
                GamePrint(color.BOLD + color.RED + "You didn't got away sucessfully." + color.END)
        PlayerHP -= MonsterDamage_to_player
        GamePrint(color.BOLD + Monster_Name + color.END + " did " + color.RED + color.BOLD + str(MonsterDamage_to_player) + color.END + " damage.")
        GamePrint("Now you have " + color.BOLD + color.UNDERLINE + str(PlayerHP) + color.END + " HP out of " + color.BOLD + str(P_Stats.hp) + color.END + " HP and " + color.BOLD + color.UNDERLINE + str(PlayerMP) + color.END + " MP out of " + color.BOLD + str(P_Stats.maxM) + color.END + " MP.")
    if Win == False:
        GamePrint(color.RED + color.BOLD + "You lose!" + color.END)
        P_Stats.hp = 0
    if Win == True:
        if _run != True:
            GamePrint(color.BOLD + color.GREEN + "You win!" + color.END)
            P_Stats.hp = PlayerHP
            P_Stats.mp = PlayerMP
            addxp(MonsterXP)
#Skill-data
Skill_List = [
    "Fire",
    "Ice"
]
Num_to_Skill = {
    "1":Fire,
    "2":Ice
}
#Monster-data
LowRat = Monster("rat",random.randint(1,5),random.randint(5,10),25,15,fist)
XPMonster = Monster("MrXP",100,0,5,1024,fist)
Dummy = Monster("Dummy",100,0,2**16,0,fist)
Creature_1 = Monster("Creature_1",2,10,100,20,wooden_sword)

Monster_List = [
    "LowRat",
    "XPMonster",
    "Dummy",
    "Creature_1"
]
#List
Name_to_Monster = {
    "LowRat":LowRat,
    "XPMonster":XPMonster,
    "Dummy":Dummy,
    "Creature_1":Creature_1
}
#Game
#Ask Name
while True:
    while True:
        GamePrint("What is your name?")
        P_Stats.names = input()
        if P_Stats.names == 'Orange':
            P_Stats.names = color.RED + 'O' + color.YELLOW + 'r' + color.GREEN + 'a' + color.CYAN + 'n' + color.BLUE + 'g' + color.PURPLE + 'e' + color.END
            dev_Armor.amount = 1
            dev_sword.amount = 1
        time.sleep(0.25)
        if P_Stats.names.lower() in Banned_Name:
            GamePrint("Name cannot be " + color.RED + P_Stats.names + color.END)
            GamePrint("Please enter your name again.")
            continue
        else:
            break
    GamePrint("Is " + color.BOLD + P_Stats.names + color.END + " your Name?")
    YN()
    characterNAMEYorN = input()
    characterNAMEYorN = characterNAMEYorN.lower()
    if characterNAMEYorN == "y":
        break
    elif characterNAMEYorN == 'n':
        GamePrint("Please enter your name again.")
        continue
    elif 1 != len(characterNAMEYorN) or characterNAMEYorN != 'y' or characterNAMEYorN != 'n':
        EnterYN()
        continue
#can't use worse sword, only the best
while P_Stats.hp >= 1:
    if dev_sword.amount == 1:
        P_Inv.Weapon = dev_sword
    if dev_Armor.amount == 1:
        P_Inv.Weapon = dev_Armor
    GamePrint(color.BOLD + "Here comes a simple tutorial about the current fighting system;" + color.END)
    fight(LowRat,"tutorial")
    recover()
    fight(XPMonster," ")
    GamePrint("Now you have fighted 2 Monster, you're probably not confused anymore, Here is a " + color.BOLD + "Dummy" + color.END + ", the speicial is that it has almost infinte HP, so feel free to try out your damage.")
    GamePrint("Also, saying " + color.BOLD + color.UNDERLINE + "end" + color.END + " will end the current test with the dummy")
    fight(Dummy,"dummy")
    GamePrint(color.BOLD + "Now let the real game begin!" + color.BOLD)
    P_Stats.XP = 0
    P_Stats.lvl = 1
    GamePrint("Loading" + color.BOLD + color.END + "...")
    for i in range(2):
        GamePrint(" ")
    GamePrint("You woke up.")
    time.sleep(0.25)
    GamePrint("'Why is there no light?', you ask yourself...")
    time.sleep(0.1)
    GamePrint("You light up a torch and walk outside.")
    GamePrint("'Where is the sun?'")
    GamePrint("You have a bad feeling about what's going to happen...")
    GamePrint("I better get inside....")
    time.sleep(1)
    GamePrint("After the moment you closed the door, something or someone slammed on your door and begging for help.")
    Dialog_Save = True
    choose("Help or leave him there?","You decided to help him","You're afraid so you didn't help",Dialog_Save)
    if Dialog_Save == True:
        GamePrint("You opened the door and saw a man and creature chasing him.")
        GamePrint("You open the door and quickly close it, only allowing ??? to pass through.")
        GamePrint("'Thank you.', ??? said.")
    if Dialog_Save == False:
        GamePrint("'Boom!', your door is now longer usable.")
        GamePrint("The man quickly rushed in your house and hid somewhere.")
        GamePrint("'rawr!', the creature screamed and runned toward you.")
        fight(Creature_1," ")
    break
GamePrint(color.YELLOW + color.BOLD + "Thank you for test beta version of game :)" + color.END)