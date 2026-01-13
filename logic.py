import random

START_CREDITS = 10
SPIN_COST = 2
TWO_MATCHREWARD = 5

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

def check_matches(reels):
    unique = set(reels)
    if len(unique) == 1:
        return "three"
    elif len(unique) == 2:
        return "two"
    else:
        return "none"

def calculate_payout(matches_type, reels):
    if matches_type == "two":
        return TWO_MATCHREWARD
    elif matches_type == "three":
        SYMBOLS = reels[0]
        return JACKPOTS[SYMBOLS]
    return 0

def spin(credits):
    if credits < SPIN_COST:
        return credits, None, "Insufficient balance, game will end"
    credits -= SPIN_COST
    reels = roll_reels()
    matches_type = check_matches(reels)
    payout = calculate_payout(matches_type=matches_type, reels=reels)

    credits += payout
    return credits, matches_type, reels, payout

if __name__ == "__main__":
    credits = START_CREDITS

    while credits >= SPIN_COST:
        credits, reels, results, payout = spin(credits)
        print(reels, results, payout, "credits:", credits)
        
    print("Game over!")

