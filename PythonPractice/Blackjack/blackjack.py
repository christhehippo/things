import random

deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4

def deal(deck):
    hand = []
    random.shuffle(deck)
    for i in range(2):
        hand.append(deck.pop())


    print(hand)
    return hand


def main():
    new_game = "yes"
    while new_game == "yes" or new_game == "y":
        player_hand = deal(deck)
        dealer_hand = deal(deck)



        new_game = input("Play again? (yes/no): ")


    exit()

if __name__ == "__main__":
    main()
