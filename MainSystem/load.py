from startup import startup

def load():
    try:
        with open(f"player_save_file.txt", "r",encoding="utf-8") as file:
            data = file.readlines()
            player_info = {}
            for line in data:
                key,value = line.strip().split(": ")
                player_info[key] = value


            name = player_info["player"]
            weapon_choice = player_info["weapon_choice"]
            hp = int(player_info["hp"])
            mp = int(player_info["mp"])
            experience = int(player_info["experience"])

            print(f"讀取存檔成功！歡迎回來，{name}!")
            return hp, mp, experience, name, weapon_choice
        
    except FileNotFoundError:
        print("抱歉，我們沒有存找到你的存檔！")
        return startup() # 如果沒有存檔，就回到開始畫面