import random
from MainSystem.getNonEmptyInput import get_non_empty_input
from character.swordman import SwordMan
from MainSystem.battle import Battle
from init import GameCharacter



class Monster(GameCharacter):
    def __init__(self, name,hp=300, dodge_rate=0.3):
        super().__init__(name, hp)
        self.dodge_rate = dodge_rate

    def attack(self):
        damage = random.choice([30, 40, 50, 60, 70, 80])
        print(f"{self.name} 使用利爪攻擊，造成了 {damage} 點傷害！")
        return damage

    def dodge(self):
        # 隨機產生一個數字來模擬閃避機制
        return random.random() < self.dodge_rate



def create_monster():
    num_monster = random.randint(1, 3) # 隨機產生 1~3 之間的數字
    monster =  [Monster(f"哥布林{chr(65+i)}") for i in range(num_monster)]
    monster_amount = len(monster)
    return monster, monster_amount

def main():
    player_name = get_non_empty_input("請問你叫什麼名字? ")
    weapon_choice = get_non_empty_input("你是勇敢的戰士，請問你要使用什麼武器? 1.單手劍 2.雙手劍 ")
    while weapon_choice not in ["1", "2"]:
        weapon_choice = input("你是勇敢的戰士，請問你要使用什麼武器? 1.單手劍 2.雙手劍 ")
    weapon_choice = int(weapon_choice)

    player = SwordMan(player_name, weapon_choice)
    monsters, monster_amount = create_monster()
    battle = Battle(player, monsters)
    print(f"戰鬥開始！你遇到了 {monster_amount} 只哥布林！")

    while player.hp > 0 and any(monster.hp > 0 for monster in monsters):
        print("-------------------------")
        # 顯示可攻擊的怪物
        battle.display_monsters()

        #讓玩家選擇攻擊模式
        attack_mode = int(get_non_empty_input("請問你要使用什麼攻擊模式? 1.普通攻擊 2.特殊技能 "))

        if attack_mode == 1:
            # 讓玩家選擇攻擊的目標
            target_index = int(get_non_empty_input("請問你要攻擊哪一隻怪物? "))-1
            battle.attack_single_target(attack_mode, target_index)
        elif attack_mode == 2:
            if not battle.attack_all_targets(attack_mode):
                continue #如果MP不足，或其他原因導致無法攻擊，可能需要跳過本輪

        # 怪物反擊
        battle.monsters_attack()

        if player.hp <= 0:
            print(f"{player.name} 已經死亡, 遊戲結束!")
            break       

        if all(monster.hp <= 0 for monster in monsters):
            print("哥布林全滅，你獲得了勝利！")
            break


if __name__ == "__main__":
    main()


        


