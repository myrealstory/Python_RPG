# This is the main file of the game. It will be the first file to run when the game starts. It will be responsible for the main game loop and the game menu. It will also be responsible for loading the game and saving the game.
from MainSystem.getNonEmptyInput import get_non_empty_input
from MainSystem.battle import Battle
from startup import startup
from play_game import play_game
from character.swordman import SwordMan
from MainSystem.load import load
from map.map import innerMap, create_monster


def main():
    run = True
    while run:
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, PLAY RULES")
        print("4, QUIT GAME")
        choice = get_non_empty_input("輸入您的選擇: ",["1", "2", "3", "4"])

        if choice == "1":
            player = startup()
            innerMap(player,map="map1")
            run = False #假設在遊戲結束後退出主循環
        elif choice == "2":
            hp,mp,experience,name,weapon_choice = load()
            player = SwordMan(name, weapon_choice, hp, mp, experience)
            monsters, monster_amount = create_monster()
            print(f"戰鬥開始！你遇到了 {monster_amount} 只哥布林！")
            battle = Battle(player, monsters)
            play_game(battle, player, monsters)
            run = False

            
        elif choice == "3":
            print("Hey, I'm Gordon, the creator of this game. The game is simple, you are a warrior and you have to fight against the goblins. You can choose to attack the goblins with a normal attack or a special attack. The game will end when you or the goblins die. Good luck!")
            input("Press Enter to continue...")

        elif choice == "4":
            print("Quiting Game... GoodBye!")
            run = False


if __name__ == "__main__":
    main()


        


