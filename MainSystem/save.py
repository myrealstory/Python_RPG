from character.weapon import weaponName
def save(player):
    # 假設player對象有name，weapon，hp等屬性
    save_data = f"player: {player.name}\n"
    save_data += f"weapon_choice: {player.weapon} {weaponName(player.weapon)}\n"
    save_data += f"hp: {player.hp}\n"
    save_data += f"mp: {player.mp}\n"
    save_data += f"experience: {player.experience}\n"

    with open(f"player_save_file.txt", "w", encoding="utf-8") as file:
        file.write(save_data)
        print(f"{player.name} 的遊戲數據已經保存！")
# Path: MainSystem/load.py