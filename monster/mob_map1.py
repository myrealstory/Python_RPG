from init import GameCharacter
import random


class Globin(GameCharacter):
    def __init__(self, name = "哥布林",hp=300, dodge_rate=0.3):
        super().__init__(name, hp)
        self.dodge_rate = dodge_rate

    def attack(self):
        damage = random.choice([30, 40, 50, 60, 70, 80])
        print(f"{self.name} 使用利爪攻擊，預估會造成 {damage} 點傷害！")
        return damage

    def dodge(self):
        # 隨機產生一個數字來模擬閃避機制
        return random.random() < self.dodge_rate
    
class Orc(GameCharacter):
    def __init__(self, name = "食人怪",hp=800, dodge_rate=0.2):
        super().__init__(name, hp)
        self.dodge_rate = dodge_rate

    def attack(self):
        
        if random.random() < 0.3:
            return self.specal_attack()
        else:
            return self.normal_attack()
        
    def normal_attack(self):
        damage = random.choice([30, 40, 50, 60, 70, 80])
        print(f"{self.name} 揮動巨錘，預估會造成 {damage} 點傷害！")
        return damage
    
    def specal_attack(self):
        damage = random.choice([100, 150, 200])
        print(f"{self.name} 使用狂暴攻擊，預估會造成 {damage} 點傷害！")
        return damage
    
    def dodge(self):
        # 隨機產生一個數字來模擬閃避機制
        return random.random() < self.dodge_rate
    
class gaintOrc(GameCharacter):
    def __init__(self, name="變異食人怪", hp=1800, dodge_rate=0.4, ultimate=1):
        super().__init__(name, hp)
        self.dodge_rate = dodge_rate
        self.ultimate = ultimate

    def attack(self):
        if self.hp < 200 and self.ultimate > 0:
            self.ultimate -= 1
            return self.destroyal()
        elif random.random() < 0.4:
            return self.special_attack()
        else:
            return self.normal_attack()
        
    def normal_attack(self):
        damage = random.choice([30, 40, 50, 60, 70, 80])
        print(f"{self.name} 揮動巨錘，預估會造成 {damage} 點傷害！")
        return damage
    
    def special_attack(self):
        damage = random.choice([150, 180, 250])
        print(f"{self.name} 使用萬錘打法，預估會造成 {damage} 點傷害！")
        return damage
    
    def destroyal(self):
        damage = 450
        print(f"{self.name} 感到反胃，吐出萬毒惡氣，預估會造成 {damage} 點傷害！")
        return damage
    
    def dodge(self):
        # 隨機產生一個數字來模擬閃避機制
        return random.random() < self.dodge_rate
    
def monster_type():
    return [Globin(), Orc()]