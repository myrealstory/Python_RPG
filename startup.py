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

def jobRecommendation(player):
    recommendations = []

    if player.strength >= 7:
        recommendations.append("劍士")
    if player.int >= 7:
        recommendations.append("法師")
    if player.dex >= 7:
        recommendations.append("弓箭手")
    if player.agi >= 7:
        recommendations.append("盜賊")
    
    # 根據推薦結果聲稱提示信息
    if recommendations:
        if len(recommendations) == 1:
            return recommendations[0]
        else:
            return " 或 ".join(recommendations)
    else:
        return "無"


def startup():

    player_name = input("請問你叫什麼名字? ")

    player = GameCharacter(player_name, gold = 2000)
    refresh_choice = get_non_empty_input("是否要消費 200 金幣重新隨機屬性？ (y/n)", ["y", "n"])

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

    jobPickRecommend = jobRecommendation(player)
    if jobPickRecommend != "無":
        jobChoice = get_non_empty_input(f"你是勇敢的勇者，神建議你選 {jobPickRecommend},請問你要選擇什麼職業? 1.劍士 2.法師 3.盜賊 4.弓箭手 ",["1", "2", "3", "4"])
        while jobChoice not in ["1", "2", "3", "4"]:
            jobChoice = input(f"你是勇敢的勇者，神建議你選  <{jobPickRecommend}> ,請問你要選擇什麼職業? 1.劍士 2.法師 3.盜賊 4.弓箭手 ")
        jobChoice = int(jobChoice)
    else:
        jobChoice = get_non_empty_input("你是勇敢的勇者，請問你要選擇什麼職業? 1.劍士 2.法師 3.盜賊 4.弓箭手 ",["1", "2", "3", "4"])
        while jobChoice not in ["1", "2", "3", "4"]:
            jobChoice = input("你是勇敢的勇者，請問你要選擇什麼職業? 1.劍士 2.法師 3.盜賊 4.弓箭手 ")
        jobChoice = int(jobChoice)

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

    if jobChoice == 1:
        jobPlayer = SwordMan(player_name, **character_attr)
    elif jobChoice == 2:
        return "to be continued"
    elif jobChoice == 3:
        return "to be continued"
    elif jobChoice == 4:
        return "to be continued"

    return jobPlayer