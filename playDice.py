import random

def playDice():
    dice = random.randint(1, 6)
    print(f"骰子點數為 {dice}")
    return dice