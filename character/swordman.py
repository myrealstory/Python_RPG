import random
from init import GameCharacter

class SwordMan(GameCharacter):
    def __init__(self, name, weapon_choice, strength, agi, int, dex, luk, lvl, hp=500, mp=50, experience=0):
        super().__init__(name, hp, strength, agi, int, dex, luk, lvl, experience, hp, mp)
        self.weapon = weapon_choice
        self.weapon_name = "單手劍" if weapon_choice == 1 else "雙手劍"

        #職業特有加成
        self.strength += 20
        self.agi += 15
        self.int += 5
        self.dex += 10
        self.luk += 3
        

    def attack(self):

        base_attack = super().attackRate()

        if self.weapon == 1: # 單手劍
            return base_attack * 1.1 
        else: # 雙手劍
            return base_attack * 1.3 
        
    def single_sword_attack(self, mode):
        attack_power = self.attack()
        magic_power = self.magicDmg()

        if mode == 1:
            print(f"{self.name} 使用 {self.weapon_name} 進行普通攻擊!")
            damage = random.randint(int(attack_power), int(attack_power* 1.2))
            attack_accuracy = 0.8
            attackType = "physicalDmg"
            self.mp += 5
        elif mode == 2:
            print(f"{self.name} 使用 {self.weapon_name} 進行多重斬擊!")
            hit_times = random.randint(1, 5)
            damage = sum(random.randint(int(attack_power), int(attack_power* 1.5)) for _ in range(hit_times))
            attackType = "physicalDmg"
            self.mp -= 15

        elif mode ==3 and self.lvl >= 5:
            hit_times = random.randint(3, 5)
            print(f"{self.name} 使用 {self.weapon_name} 進行「極光衝刺」攻擊!產生了{hit_times}星星一同墜入敵人身上！")
            damage = magic_power + random.randint(int(magic_power * 1.5), int(magic_power* 2.5))
            attackType = "magicDmg"
            self.mp -= 35
            
        attack_accuracy = super().accuracy() if attackType == "physicalDmg" else 100
        return damage, attack_accuracy, attackType
        
    def double_sword_attack(self, mode):
        attack_power = self.attack()

        if mode == 1:
            print(f"{self.name} 使用 {self.weapon_name} 進行普通攻擊!")
            damage = random.randint(int(attack_power * 0.9), int(attack_power* 1.8))
            attackType = "physicalDmg"
            self.mp += 5

        elif mode == 2:
            print(f"{self.name} 使用 {self.weapon_name} 進行「十字審判」攻擊!")
            damage = random.randint(int(attack_power * 1.5), int(attack_power* 2.5)) *2
            attackType = "physicalDmg"
            self.mp -= 25

        elif mode ==3 and self.lvl >= 5:
            print(f"{self.name} 使用 {self.weapon_name} 進行「大地衝擊」攻擊!")
            damage = random.randint(int(attack_power * 3), int(attack_power* 4))
            attackType = "magicDmg"
            self.mp -= 35
        
        attack_accuracy = super().accuracy()
        return damage, attack_accuracy,attackType
        
    def dodge(self):
        dodge_chance = super().AGI()

        if random.random() < dodge_chance:
            return True
        else:
            return False
        
    def defense(self):
        # 簡化的防禦邏輯，可以根據需要調整
        defense_value = super().defense()  # 假设单手剑防御值为30，双手剑为50
        print(f"{self.name} 進行防禦，減少了{defense_value}點傷害。")
        return defense_value
        