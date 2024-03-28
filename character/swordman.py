import random
from init import GameCharacter

class SwordMan(GameCharacter):
    def __init__(self, name, **game_init ):
        super().__init__(name)
        self.jobName = "劍士"
        self.weapon = "單手劍"
        self.skill1 = "爆裂斬"
        self.skill2 = "極光衝刺"

        self.__dict__.update(game_init)

        #職業特有加成
        self.strength += 20
        self.agi += 15
        self.int += 5
        self.dex += 10
        self.luk += 3
        
    
    def attack(self, mode):
        attack_power = self.attackRate() * 1.1
        attack_power = int(attack_power)
        magic_power = self.magicDmg()
        magic_power = int(magic_power)
        max_DMGPower1 = int(attack_power * 1.2)
        max_DMGPower2 = int(attack_power * 1.5)

        if mode == 1:
            print(f"{self.name} 使用 {self.weapon} 進行普通攻擊!")
            damage = random.randint(attack_power, max_DMGPower1)
            attack_accuracy = 0.8
            attackType = "physicalDmg"
            self.mp += 5
        elif mode == 2:
            print(f"{self.name} 使用 {self.weapon} 進行<{self.skill1}>!，產生了{hit_times}火花一同爆炸")
            hit_times = random.randint(1, 5)
            damage = sum(random.randint(attack_power, max_DMGPower2) for _ in range(hit_times))
            attackType = "physicalDmg"
            self.mp -= 15

        elif mode ==3 and self.lvl >= 5:
            hit_times = random.randint(3, 5)
            print(f"{self.name} 使用 {self.weapon} 進行「極光衝刺」攻擊!產生了{hit_times}星星一同墜入敵人身上！")
            damage = magic_power + random.randint(int(magic_power * 1.5), int(magic_power* 2.5))
            attackType = "magicDmg"
            self.mp -= 35
            
        attack_accuracy = super().accuracy() if attackType == "physicalDmg" else 100
        return damage, attack_accuracy, attackType
        
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
        