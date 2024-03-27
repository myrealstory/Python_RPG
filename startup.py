# This file is used to start the game and get the player's name and weapon choice. It also creates the monsters and the amount of monsters the player will face.
# The function startup() is used to get the player's name and weapon choice. It also creates the monsters and the amount of monsters the player will face.
# The function create_monster() is used to create the monsters and the amount of monsters the player will face.
# The function main() is used to start the game and display the amount of monsters the player will face.
# The function play_game() is used to start the game and display the amount of monsters the player will face. It also allows the player to attack the monsters and the monsters to attack the player. It also displays the result of the game.
# The function get_non_empty_input() is used to get the player's name and weapon choice. It also allows the player to attack the monsters and the monsters to attack the player. It also displays the result of the game.
# The class Monster is used to create the monsters and the amount of monsters the player will face.

from MainSystem.getNonEmptyInput import get_non_empty_input
from character.swordman import SwordMan
from init import GameCharacter



def startup():

    player_name = get_non_empty_input("請問你叫什麼名字? ")

    player = GameCharacter(player_name, gold = 2000)
    refresh_choice = get_non_empty_input("是否要消費 200 金幣重新隨機屬性？ (y/n)")

    while refresh_choice.lower() == "y":

        success = player.refresh_attributes()

        if not success:
            break # 如果金幣不足，則跳出迴圈
        print(f"{player_name} 的屬性已經刷新！ 剩餘金幣： {player.gold}")
        print(f"力量 是 {player.strength}")
        print(f"敏捷 是 {player.agi}")
        print(f"智力 是 {player.int}")
        print(f"運氣 是 {player.luk}")
        print(f"HP 是 {player.hp}")
        print(f"MP 是 {player.mp}")
        print(f"總屬性點數 是 {player.totalAll}")
        print(f"剩下金幣 是 {player.gold}")
        refresh_choice = input("是否要繼續消費 200 金幣重新隨機屬性？ (y/n)")

    
    weapon_choice = get_non_empty_input("你是勇敢的戰士，請問你要使用什麼武器? 1.單手劍 2.雙手劍 ")
    while weapon_choice not in ["1", "2"]:
        weapon_choice = input("你是勇敢的戰士，請問你要使用什麼武器? 1.單手劍 2.雙手劍 ")
    weapon_choice = int(weapon_choice)

    character_attr = {
        "strength": player.strength,
        "agi": player.agi,
        "int": player.int,
        "dex": player.dex,
        "luk": player.luk,
        "hp": player.hp,
        "mp": player.mp,
        "gold": player.gold,
    }

    jobPlayer = SwordMan(player_name, weapon_choice, **character_attr)

    return jobPlayer