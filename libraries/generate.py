import random


def main():
    cards = ["jack", "queen", "king"]
    
    coin = random.choice(["heads", "tails"])
    print(f"Tossed: {coin}\n")
    
    number = random.randint(1, 10)
    print(f"Random Number: {number}\n")
    
    print("Shuffled Cards:")
    random.shuffle(cards)
    for card in cards:
        print(card)

main()