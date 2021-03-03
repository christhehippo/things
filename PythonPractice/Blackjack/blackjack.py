import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

def deal(deck):
    hand = []
    random.shuffle(deck)
    for i in range(2):
        hand.append(deck.pop())


    print(hand)
    return hand

def draw(deck):
    return deck.pop()


def main():
    new_game  = "yes"
    draw_card = "" 
    player_hand_value = 0
    dealer_hand_value = 0
    while new_game.lower() == "yes" or new_game.lower() == "y":
        player_hand_value = dealer_hand_value = 0
        player_hand = deal(deck)
        dealer_hand = deal(deck)

        if player_hand[0] < 11:
            player_hand_value += player_hand[0]
        else:
            if player_hand[0] == 14:
                player_hand_value += 11
            else:
                player_hand_value += 10

        if player_hand[1] < 11:
            player_hand_value += player_hand[1]
        else:
            if player_hand[1] == 14:
                player_hand_value += 11
            else:
                player_hand_value += 10 

        if dealer_hand[0] < 11:
            dealer_hand_value += dealer_hand[0]
        else:
            if dealer_hand[0] == 14:
                dealer_hand_value += 11
            else:
                dealer_hand_value += 10

        if dealer_hand[1] < 11:
            dealer_hand_value += dealer_hand[1]
        else:
            if dealer_hand[1] == 14:
                dealer_hand_value += 11
            else:
                dealer_hand_value += 10 
        
        if draw_card.lower() != "no"  and player_hand_value < 21:
             draw_card = input("Draw card? (yes/no):")
        while draw_card.lower() != "no":
            player_hand.append(deck.pop())

            if player_hand[-1] < 11:
                player_hand_value += player_hand[-1]
            else:
                if player_hand[-1] == 14:
                    player_hand_value += 11
                else:
                    player_hand_value += 10
            print(player_hand)
            if player_hand_value < 21:
                draw_card = input("Draw card? (yes/no):")
            else:   
                draw_card = "no"

        if player_hand_value > 21:
            print(player_hand)
            print("Player bust!")
        else:
            while dealer_hand_value < 17:
                dealer_hand.append(deck.pop())
                if dealer_hand[-1] < 11:
                    dealer_hand_value += dealer_hand[-1]
                else:
                    if dealer_hand[-1] == 14:
                        dealer_hand_value += 11
                    else:
                        dealer_hand_value += 10 

            print(player_hand)
            print(dealer_hand)
            if dealer_hand_value > 21 or player_hand_value > dealer_hand_value: 
                print("Player Wins")
            else:
                print("Dealer Wins")

        new_game = input("Play again? (yes/no): ")



    exit()

if __name__ == "__main__":
    main()
