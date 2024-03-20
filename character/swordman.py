import random
from init import GameCharacter

class SwordMan(GameCharacter):
    def __init__(self, name , weapon_choice, hp=500, mp=50, experience=0):
        super().__init__(name,hp)
        self.weapon = weapon_choice
        self.weapon_name = "單手劍" if weapon_choice == 1 else "雙手劍"
        self.mp = mp
        self.experience = experience
        

    def attack(self, mode):
        if self.weapon == 1: # 單手劍
            return self.single_sword_attack(mode)
        else: # 雙手劍
            return self.double_sword_attack(mode)
        
    def single_sword_attack(self, mode):
        if mode == 1:
            print(f"{self.name} 使用 {self.weapon_name} 進行普通攻擊!")
            damage = random.randint(50, 100)
            attack_accuracy = 0.8
            return damage, attack_accuracy
        else:
            print(f"{self.name} 使用 {self.weapon_name} 進行多重斬擊!")
            hit_times = random.randint(1, 5)
            total_damage = 0
            while hit_times > 0:
                hit_times -= 1
                total_damage += random.randint(50, 70)
            return total_damage, 1  # 假設這種攻擊模式總是命中
        
    def double_sword_attack(self, mode):
        if mode == 1:
            print(f"{self.name} 使用 {self.weapon_name} 進行普通攻擊!")
            damage = random.randint(70, 120)
            attack_accuracy = 0.7
            return damage, attack_accuracy
        else:
            print(f"{self.name} 使用 {self.weapon_name} 進行「十字審判」攻擊!")
            total_damage = random.randint(100, 150) * 2
            return total_damage, 1  # 假設這種攻擊模式總是命中
        
    def dodge(self):
        if self.weapon == 1:
            dodge_chance = 0.5
        else:
            dodge_chance = 0.3

        if random.random() < dodge_chance:
            return True
        else:
            return False
        
    def defense(self):
        # 簡化的防禦邏輯，可以根據需要調整
        defense_value = 30 if self.weapon == 1 else 50  # 假设单手剑防御值为30，双手剑为50
        print(f"{self.name} 進行防禦，減少了{defense_value}點傷害。")
        return defense_value
        