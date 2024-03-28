from MainSystem.getNonEmptyInput import get_non_empty_input
from character.weapon import weaponName
from MainSystem.save import save
from init import GameCharacter

def play_game(battle ,player, monsters):
    while player.hp > 0 and any(monster.hp > 0 for monster in monsters):
        print("-------------------------")
        # 顯示可攻擊的怪物
        battle.display_monsters()

        #讓玩家選擇攻擊模式
        weapon_name = weaponName("swordman",player.weapon)
        attack_mode = int(get_non_empty_input(f"請問你要使用 {player.weapon} 進行? 1.普通攻擊 2.特殊技能 "))

        if attack_mode == 1:
            # 讓玩家選擇攻擊的目標
            target_index = int(get_non_empty_input(f"請問你要攻擊哪一隻怪物? "))-1
            battle.attack_single_target(attack_mode, target_index)
        elif attack_mode == 2:
            if not battle.attack_all_targets(attack_mode,player.weapon):
                continue #如果MP不足，或其他原因導致無法攻擊，可能需要跳過本輪

        # 怪物反擊
        battle.monsters_attack()

        if player.hp <= 0:
            print(f"{player.name} 已經死亡, 遊戲結束!")
            break       

        if all(monster.hp <= 0 for monster in monsters):
            print("哥布林全滅，你獲得了勝利！")

            #計算從魔物獲得的金幣綜合
            total_gold_gain = sum(monster.gold for monster in monsters)

            total_gold_gain += total_gold_gain * (player.lvl * 0.1)
            player.gold += total_gold_gain
            print(f"你獲得了 {total_gold_gain} 金幣！ 總金幣現在是 {player.gold}!")
            choice_LVLing = get_non_empty_input("是否要升級屬性? (y/n)")
            if choice_LVLing.lower() == "y":
                GameCharacter.lvling_Attributes()

            # 保存遊戲數據
            save(battle.player)
            
            break