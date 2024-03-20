def weaponName(job="swordman", weapon_choice=1):
    if job == "swordman":
        if weapon_choice == 1:
            return "單手劍"
        elif weapon_choice == 2:
            return "雙手劍"
    elif job == "magician":
        if weapon_choice == 1:
            return "法杖"
        elif weapon_choice == 2:
            return "魔杖"
    else:
        return "拳頭"