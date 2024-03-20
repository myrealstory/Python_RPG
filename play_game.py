from MainSystem.getNonEmptyInput import get_non_empty_input
from character.weapon import weaponName
from MainSystem.save import save

def play_game(battle ,player, monsters):
    while player.hp > 0 and any(monster.hp > 0 for monster in monsters):
        print("-------------------------")
        # 顯示可攻擊的怪物
        battle.display_monsters()

        #讓玩家選擇攻擊模式
        weapon_name = weaponName("swordman",player.weapon)
        attack_mode = int(get_non_empty_input(f"請問你要使用 {weapon_name} 進行? 1.普通攻擊 2.特殊技能 "))

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

            # 計算從妹子怪物獲得的經驗值綜合
            total_exp_gain = sum(monster.initial_hp * 0.5 for monster in monsters)
            player.experience += total_exp_gain
            print(f"你获得了 {total_exp_gain} 点经验值。总经验值现在是 {player.experience}。")
            # 保存遊戲數據
            save(battle.player)
            break