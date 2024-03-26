
import random
import importlib
from MainSystem.battle import Battle
from play_game import play_game

def create_monster(map):
    num_monsters = random.randint(1, 3)
    monster = []
    monster_module = importlib.import_module(f"monster.mob_{map}")
    available_monsters = monster_module.monster_type()

    for i in range(num_monsters):
        chosen_monster_type = random.choice(available_monsters)
        monster_name = f"{chosen_monster_type.__name__}_ {i + 1}"
        # 實例化怪物，，並添加到怪物列表中
        monster = chosen_monster_type(name =monster_name)
        monster.append(monster)

    monster_amount = len(monster)  
    return monster, monster_amount

def innerMap(player,map):
    while True:
        print("你來到了一片荒涼的土地，這裡有許多怪物，你必須打倒他們才能獲得更多金幣升級。")
        print("1. 你將會遇到怪物：哥布林 or 食人怪")
        print("2. 往前走尋找機會")
        print("3. 地圖3")
        print("4. 離開遊戲")
        map_choice = input("請選擇你的路線：")

        if map_choice == "1":
            monsters, monster_amount = create_monster(map)
            print(f"戰鬥開始！你遇到了 {monster_amount} 只魔物！")
            battle = Battle(player, monsters)
            play_game(battle, player, monsters)
            continue
        elif map_choice == "2":
            break
        elif map_choice == "3":
            break
        elif map_choice == "4":
            print(f"請問{player.name}是否要離開遊戲？")
            break
        else:
            print("請輸入正確的選項！")
            continue
