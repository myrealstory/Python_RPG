import random

class GameCharacter:
    def __init__(self, name, experience=0,lvl=1,gold=1000):
        self.name = name
        self.experience = experience
        self.lvl = lvl
        self.gold = gold
        
    def refresh_attributes(self):
        if self.gold < 0:
            self.gold = 0
            print("你的金幣不足!")
            return False
        
        self.strength = random.randint(1, 10)
        self.agi = random.randint(1, 10)
        self.int = random.randint(1, 10)
        self.dex = random.randint(1, 10)
        self.luk = random.randint(1, 10)
        self.hp = 100 + self.strength * 10
        self.mp = 50 + self.int * 5
        self.gold -= 200
        self.totalAll = self.strength + self.agi + self.int + self.dex + self.luk
        return True

    
    def attackRate(self):
        strength = self.strength + self.agi * 0.5 + self.luk * 0.05
        return random.randit(strength, strength + 10)

    def AGI(self):
        evade = self.agi + self.strength * 0.1 + self.luk * 0.2
        return (evade / self.totalAll) * 100
    
    def accuracy(self):
        dex = self.dex + self.agi * 0.5 + self.luk * 0.1 + self.strength * 0.1
        return (dex / self.totalAll) * 100
    
    def defense(self):
        return self.strength + self.agi * 0.5 + self.luk * 0.1 + self.dex * 0.1
    
    def criticalRate(self):
        critical = self.luk + self.dex * 0.3 + self.agi * 0.1
        happenCritical = random.randint(40, 100)
        return (critical / self.totalAll) * 100 > happenCritical 

    def criticalDmg(self):
        return self.attackRate() + self.attackRate() * (self.luk * 0.2)

    def magicDmg(self):
        return random.randint(self.int * 1.2, self.int * 1.6 ) 
    
    def magicDef(self):
        return (self.int * 0.5)
    