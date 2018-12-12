import random
import sys
import time


class Card:
    def __init__(self, card_type, card_text, card_value):
        self.card_type = card_type
        self.card_text = card_text
        self.card_value = card_value


class Role:
    def __init__(self):

        # set your card as empty
        self.cards = []

    # show what card you have
    def show_card(self):
        for card in self.cards:
            print(card.card_type, card.card_text, sep='', end='')
        # switch the line
        print()

    def get_value(self, min_or_max):

        sum = 0
        # SET A as 0
        A = 0
        for card in self.cards:
            # sum up the points
            sum += card.card_value
            if card.card_text == 'A':
                A += 1

        if min_or_max == "max":
            # change the value of A to get the maximum points
            for i in range(A):
                value = sum - i * 10
                if value <= 21:
                    return value
        return sum - A * 10

    def burst(self):

        # test whether points larger than 21 or not
        return self.get_value("min") > 21


class CardManager:

    def __init__(self):
        # Set a new card
        self.cards = []
        # def all cards
        all_card_type = "♥♠♣♦"
        all_card_text = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        all_card_value = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]

        # manage the card
        for card_type in all_card_type:
            for index, card_text in enumerate(all_card_text):
                card = Card(card_type, card_text, all_card_value[index])
                self.cards.append(card)

        # shuffle cards
        random.shuffle(self.cards)

    # send cards
    def send_card(self, role, num=1):

        for i in range(num):
            card = self.cards.pop()
            role.cards.append(card)


# create card manager
cards = CardManager()
# create dealer
dealer = Role()
# create player role
player = Role()

# At the beginning, send one card to dealer, two cards to player
cards.send_card(dealer)
cards.send_card(player, num=2)

# show cards
dealer.show_card()
player.show_card()

# Ask player if he/she wants to add cards
while True:
    choice = input("Do you want one more card? Y for YES, N for NO: ")
    if choice == 'Y':
        cards.send_card(player)
        # Show cards
        dealer.show_card()
        player.show_card()
        # define player whether burst or not
        if player.burst():
            print("Your points over 21, YOU LOSE!")
            sys.exit()
    else:
        break

# dealer keeps getting cards until 17
while True:
    print("Card manager is sending cards to dealer......")
    # add time gap for dealer
    time.sleep(1)
    # send card to dealer
    cards.send_card(dealer)
    # show cards
    dealer.show_card()
    player.show_card()
    # define dealer whether burst or not
    if dealer.burst():
        print("Computer player's points over 21, YOU WIN!")
        sys.exit()
    # if not burst,break
    elif dealer.get_value("max") >= 17:
        break


def main():
    player_value = player.get_value(max or min)
    dealer_value = dealer.get_value(max or min)
    # Comparing total points players get
    if player_value > dealer_value:
        print("YOU WIN!")
    elif player_value == dealer_value:
        print("DRAW")
    else:
        print("YOU LOSE!")


if __name__ == '__main__':
    main()
