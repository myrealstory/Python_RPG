from MainSystem.getNonEmptyInput import get_non_empty_input

# display_monsters()：显示所有可攻击的怪物。
# attack_single_target()：对单一目标执行攻击。
# attack_all_targets()：执行全体攻击，并考虑MP消耗。
# monsters_attack()：处理怪物的反击。
# apply_damage()：应用伤害到目标上，并处理闪避逻辑。
# player_defense()：处理玩家的防御或闪避选择。

class Battle:
    def __init__(self, player, monsters):
        self.player = player
        self.monsters = monsters

    def display_monsters(self):
        alive_monsters = [monster for monster in self.monsters if monster.hp > 0]
        print("可攻擊的魔物有: ")
        for i, monster in enumerate(alive_monsters):
            if monster.hp > 0:
                print(f"{i+1}. {monster.name} (血量: {monster.hp})")

    def attack_single_target(self, attack_mode, target_index):
        alive_monsters = self.display_monsters()
        target_monster = None

        if len(alive_monsters) == 1:
            target_monster = alive_monsters[0]
            print(f"只有一只怪物，{self.player.name} 對 {target_monster.name} 進行攻擊。")

        else: 
            if target_index < 0 or target_index >= len(alive_monsters):
                print("請選擇一個有效的魔物。")
                return
            target_monster = alive_monsters[target_index]
        
        if target_monster:
            damage, attack_accuracy = self.player.attack(attack_mode)
            self.apply_damage(target_monster, damage, attack_accuracy)

    def attack_all_targets(self, attack_mode,weapon_choice):
        if self.player.mp < 25 and weapon_choice == 2:
            print("MP 不足，無法使用十字審判。")
            return False
        elif self.player.mp < 15 and weapon_choice == 1:
            print("MP 不足，無法使用多重斬擊。")
            return False
        
        for monster in self.monsters:
            if monster.hp > 0:
                damage, attack_accuracy = self.player.attack(attack_mode)
                self.apply_damage(monster, damage, attack_accuracy)
        return True
    
    def monsters_attack(self):
        for monster in self.monsters:
            if monster.hp <= 0:
                continue
            print("-------------------------")
            print(f"{monster.name} 準備反擊。")
            damage = monster.attack()
            self.player_defense(damage)

    def apply_damage(self, target, damage, attack_accuracy):
        #判斷攻擊是否命中
        if attack_accuracy > target.dodge_rate:
            if not target.dodge():
                target.hp -= damage
                print(f"{target.name} 被攻擊並受到了 {damage} 點傷害，剩餘血量為 {target.hp}。")
            else:
                print(f"{target.name} 閃避了 {self.player.name} 的攻擊。")
        else:
            print(f"{self.player.name} 的攻擊沒有命中 {target.name}。")
        if target.hp <= 0:
            print(f"{target.name} 已經死亡。")

    def player_defense(self, damage):
        player_defense_action = int(get_non_empty_input("怪物即將攻擊，你選擇：1.防禦 2.閃躲 "))
        if player_defense_action == 1:
            defense_value = self.player.defense()
            actual_damage = max(0, damage - defense_value)
            self.player.hp -= actual_damage
            self.player.mp += 5
            if actual_damage > 0 :
                print(f"{self.player.name} 在防守後受到了 {actual_damage} 點傷害，剩餘血量為 {self.player.hp}, 剩餘MP為 {self.player.mp}。")
            else:
                print(f"{self.player.name} 完全防禦了攻擊。")
        elif player_defense_action == 2:
            if self.player.dodge():
                print(f"{self.player.name} 閃躲了攻擊。")
            else:
                print(f"{self.player.name} 未能閃躲攻擊。")
                self.player.hp -= damage
                print(f"{self.player.name} 受到了 {damage} 點傷害，剩餘血量為 {self.player.hp}, 剩餘MP為 {self.player.mp}。")