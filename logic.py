import random

START_CREDITS = 1
SPIN_COST = 0.20
TWO_MATCHREWARD = 0.50

SYMBOLS = ["Mandarin Orange", "Young Fruit", "Sakura Cherry", "Jack Fruit", "Cocoa Brownie", "Cody","Jinx Fruit"]

JACKPOTS = {
    "Mandarin Orange": 23,
    "Young Fruit": 23,
    "Sakura Cherry": 50,
    "Jack Fruit": 23,
    "Cocoa Brownie": 67,
    "Cody": 160,
    "Jinx": 2500,
}

def roll_reels():
    return [random.choice(SYMBOLS) for _ in range(3)]    

if __name__ == "__main__":
    print(roll_reels())

