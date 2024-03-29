import random

def playDice():
    dice = random.randint(1, 6)
    print(f"骰子點數為 {dice}")
    return dice

def dodgeDice():
    getDice = playDice()
    finalRate = 0
    if getDice > 0 and getDice <= 2:
        finalRate += random.choice([10,20,30,])
    if getDice > 2 and getDice <= 4:
        finalRate += random.choice([40,50,60,])
    if getDice == 5:
        finalRate += random.choice([70,80,90,])
    if getDice == 6:
        finalRate+= random.choice([100])

    return finalRate