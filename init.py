import random

class GameCharacter:
    def __init__(self, name,lvl=1,gold=None):
        self.name = name
        self.lvl = lvl
        self.gold = gold
        
    def refresh_attributes(self):
        if self.gold < 200:
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
        self.totalAll = f"{self.strength + self.agi + self.int + self.dex + self.luk + self.hp + self.mp} / {10 * 5 + 200 + 250}"
        return True

    
    def attackRate(self):
        strength = round(self.strength + self.agi * 0.5 + self.luk * 0.05)
        maxDmg = strength + 10
        return random.randint(strength, maxDmg)

    def AGI(self):
        evade = round(self.agi + self.strength * 0.1 + self.luk * 0.2)
        totalAll = 255 + 255 # agi max - 255 , luk max - 255
        return (evade / totalAll) * 100
    
    def accuracy(self):
        dex = round(self.dex + self.agi * 0.5 + self.luk * 0.1 + self.strength * 0.1)
        totalAll = 255 + 255 # dex max - 255 , luk max - 255
        return (dex / totalAll) * 100
    
    def defense(self):
        return round(self.strength + self.agi * 0.5 + self.luk * 0.1 + self.dex * 0.1)
    
    def criticalRate(self):
        critical = round(self.luk + self.dex * 0.3 + self.agi * 0.1)
        happenCritical = random.randint(40, 100)
        totalAll = 255 + 255 # luk max - 255 , agi max - 255
        return (critical / self.totalAll) * 100 > happenCritical 

    def criticalDmg(self):
        return round(self.attackRate() + self.attackRate() * (self.luk * 0.2))

    def magicDmg(self):
        min_magicAttack = round(self.int * 1.2)
        max_magicAttack = round(self.int * 1.6)
        return random.randint(min_magicAttack, max_magicAttack) 
    
    def magicDef(self):
        return round(self.int * 0.5)
    
    def lvling_Attributes(self):
        # 定義選項 和 對應的屬性名
        statusOptions = {
            "1": "力量",
            "2": "敏捷",
            "3": "智力",
            "4": "準確度",
            "5": "幸運",
            "6": "HP",
            "7": "MP",
        }

        statusChoose = input(f"請問想要升級哪種屬性? 1. 力量 2. 敏捷 3. 智力 4. 準確度 5. 幸運 6.HP 7.MP 8. 離開")

        if statusChoose in statusOptions:
            attr_name = {
                "1": "strength",
                "2": "agi",
                "3": "int",
                "4": "dex",
                "5": "luk",
                "6": "hp",
                "7": "mp",
            }.get(statusChoose)

            increament = random.randint(2, 8)

            if statusChoose in ["6","7"]:
                if statusChoose == "6":
                    increament *= 5  # HP 的增加值是 5 的倍數
                else:
                    increament *= 3  # MP 的增加值是 3 的倍數
            
            setattr(self, attr_name, getattr(self, attr_name) + increament)
            print(f"{statusOptions[statusChoose]} 提升了 {increament}點！")
            print(f"{self.name} 的金幣剩下 {self.gold}")

        elif statusChoose == "8":
            return
        else:
            print("請輸入正確的數字!")
            self.lvling_Attributes()

    