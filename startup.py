# This file is used to start the game and get the player's name and weapon choice. It also creates the monsters and the amount of monsters the player will face.
# The function startup() is used to get the player's name and weapon choice. It also creates the monsters and the amount of monsters the player will face.
# The function create_monster() is used to create the monsters and the amount of monsters the player will face.
# The function main() is used to start the game and display the amount of monsters the player will face.
# The function play_game() is used to start the game and display the amount of monsters the player will face. It also allows the player to attack the monsters and the monsters to attack the player. It also displays the result of the game.
# The function get_non_empty_input() is used to get the player's name and weapon choice. It also allows the player to attack the monsters and the monsters to attack the player. It also displays the result of the game.
# The class Monster is used to create the monsters and the amount of monsters the player will face.

from MainSystem.getNonEmptyInput import get_non_empty_input
from character.swordman import SwordMan
import random
from init import GameCharacter

class Monster(GameCharacter):
    def __init__(self, name,hp=300, dodge_rate=0.3):
        super().__init__(name, hp)
        self.dodge_rate = dodge_rate

    def attack(self):
        damage = random.choice([30, 40, 50, 60, 70, 80])
        print(f"{self.name} 使用利爪攻擊，預估會造成 {damage} 點傷害！")
        return damage

    def dodge(self):
        # 隨機產生一個數字來模擬閃避機制
        return random.random() < self.dodge_rate


def create_monster():
    num_monster = random.randint(1, 3) # 隨機產生 1~3 之間的數字
    monster =  [Monster(f"哥布林{chr(65+i)}") for i in range(num_monster)]
    monster_amount = len(monster)
    return monster, monster_amount

def startup():

    player_name = get_non_empty_input("請問你叫什麼名字? ")
    weapon_choice = get_non_empty_input("你是勇敢的戰士，請問你要使用什麼武器? 1.單手劍 2.雙手劍 ")
    while weapon_choice not in ["1", "2"]:
        weapon_choice = input("你是勇敢的戰士，請問你要使用什麼武器? 1.單手劍 2.雙手劍 ")
    weapon_choice = int(weapon_choice)

    player = SwordMan(player_name, weapon_choice)
    monsters, monster_amount = create_monster()

    return player, monsters, monster_amount