# Name:QingRu Su, Xia yineng


from random import shuffle
from random import randint


class Player(object):
    def __init__(self):
        self.hand = []
        self.money = 2000

    def bet(self, initial_bet):
        num_in = input("please enter Fold or Check:")

        while num_in != "Fold" and num_in != "Check":
            num_in = input("please enter Fold or Check:")

        if num_in == "Fold":
            return num_in
        elif num_in == "Check":
            return initial_bet

    def get_rank(self, board, hands):
        scores = [(self.evaluate((board + ' ' + hand).split()), i)
                  for i, hand in enumerate(hands)]
        best = max(scores)[0]
        return [x[1] for x in filter(lambda x: x[0] == best, scores)]

    def evaluate(self, hand):
        ranks = '23456789TJQKA'
        if len(hand) > 5:
            result = [self.evaluate(hand[:i] + hand[i + 1:])
                      for i in range(len(hand))]
            return max(result)
        score, ranks = zip(
            *sorted((cnt, rank) for rank, cnt in {ranks.find(r): ''.join(hand).count(r)
                                                  for r, _ in hand}.items())[::-1])
        if len(score) == 5:
            if ranks[0:2] == (12, 3):
                # adjust if 5 high straight
                ranks = (3, 2, 1, 0, -1)
                # high card, straight, flush, straight flush
            score = ([(1,), (3, 1, 2)], [(3, 1, 3), (5,)])[len({suit for _, suit in hand}) == 1][
                ranks[0] - ranks[4] == 4]
        return score, ranks


class AiPlayer(Player):
    def bet(self, initial_bet):
        if self.money < initial_bet:
            return randint(1, initial_bet)
        return randint(initial_bet, self.money)


class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def to_evaluate(self):
        color_mapping = {'heart': 'H', 'diamonds': 'D', 'spades': 'S', 'clubs': 'C'}
        return "{}{}".format(self.value, color_mapping[self.color])

    def __str__(self):
        return "{}:{}".format(self.color, self.value)

    __repr__ = __str__


class Game(object):
    def __init__(self, player1, player2):
        self.player1 = player1
        self.ai = player2

    def split_line(self):
        print("\n------------------------------------------")

    def shuffle_cards(self):
        colors = ['heart', 'diamonds', 'spades', 'clubs']
        values = ['A'] + [i for i in range(2, 10)] + ['J', 'Q', 'K']
        deck = [Card(value, color) for value in values for color in colors]
        shuffle(deck)
        return deck

    def issue_card(self, card_decks, num_cards):
        result = []
        for i in range(num_cards):
            result.append(card_decks.pop())
        return result

    def betting_phase(self, start_amount):
        v2 = self.ai.bet(start_amount)
        print("ai bet: %s" % v2)
        v1 = self.player1.bet(v2)
        print("you bet: %s" % v1)
        if v1 == "Fold":
            return "p1Fold"
        else:
            return v1

    def round_end(self, board):
        self.split_line()
        print("time to decide the winner")
        board_string = ""
        for card in board:
            board_string += "{} ".format(card.to_evaluate())
        board_string = board_string[:-1]

        p1_hand = ""
        for card in self.player1.hand:
            p1_hand += "{} ".format(card.to_evaluate())
        p1_hand = p1_hand[:-1]

        p2_hand = ""
        for card in self.ai.hand:
            p2_hand += "{} ".format(card.to_evaluate())
        p2_hand = p2_hand[:-1]

        print("board: %s" % board)
        print("player1: %s" % self.player1.hand)
        print("AI: %s" % self.ai.hand)
        result = self.player1.get_rank(board_string, [p1_hand, p2_hand])

        return result

    def show_info(self):
        print("AI money:%s" % self.ai.money)
        print("Your money:%s" % self.player1.money)

    def single_round(self):
        print("shuffling the decks")
        card_decks = self.shuffle_cards()
        self.player1.hand = []
        self.ai.hand = []
        starting_amount = 20

        print("issue card to player")
        self.player1.hand = self.issue_card(card_decks, 2)
        self.ai.hand = self.issue_card(card_decks, 2)
        print("Your hand is: %s with money: %s" % (self.player1.hand, self.player1.money))
        print("AI money: %s" % self.ai.money)
        bet = self.betting_phase(starting_amount)
        if bet == "p1Fold":
            print("You fold")
            self.ai.money += starting_amount * 2
            self.player1.money -= starting_amount
            self.show_info()
            return
        else:
            bet = int(bet)
            self.player1.money -= (bet - starting_amount)
            self.ai.money -= (bet - starting_amount)
            starting_amount = bet

        self.split_line()
        print("issue the first 3 cards")
        board = self.issue_card(card_decks, 3)
        print(board)
        print("Your hand is: %s with money: %s" % (self.player1.hand, self.player1.money))
        print("AI money: %s" % self.ai.money)
        bet = self.betting_phase(starting_amount)
        if bet == "p1Fold":
            print("You fold")
            self.ai.money += starting_amount * 2
            self.player1.money -= starting_amount
            self.show_info()
            return
        else:
            bet = int(bet)
            self.player1.money -= (bet - starting_amount)
            self.ai.money -= (bet - starting_amount)
            starting_amount = bet

        self.split_line()
        print("4th card")
        board += self.issue_card(card_decks, 1)
        print(board)
        print("Your hand is: %s with money: %s" % (self.player1.hand, self.player1.money))
        print("AI money: %s" % self.ai.money)
        bet = self.betting_phase(starting_amount)
        if bet == "p1Fold":
            print("You fold")
            self.ai.money += starting_amount * 2
            self.player1.money -= starting_amount
            self.show_info()
            return
        else:
            bet = int(bet)
            self.player1.money -= (bet - starting_amount)
            self.ai.money -= (bet - starting_amount)
            starting_amount = bet

        self.split_line()
        print("5th card")
        board += self.issue_card(card_decks, 1)
        print("board is: ", board)
        print("Your hand is: %s with money: %s" % (self.player1.hand, self.player1.money))
        print("AI money: %s" % self.ai.money)
        bet = self.betting_phase(starting_amount)
        if bet == "p1Fold":
            print("You fold")
            self.ai.money += starting_amount * 2
            self.player1.money -= starting_amount
            self.show_info()
            return
        else:
            bet = int(bet)
            self.player1.money -= (bet - starting_amount)
            self.ai.money -= (bet - starting_amount)
            starting_amount = bet

        # winner phase
        result = self.round_end(board)
        if len(result) == 2:
            print("DRAW!")
        elif result[0] == 0:
            print("Player 1 win this round!")
            self.player1.money += starting_amount * 2
        else:
            print("AI Win this round!")
            self.ai.money += starting_amount * 2

    def start(self):
        for i in range(5):
            print("*****************************")
            print("Round %s start" % i)
            print("Player1 money:%s" % self.player1.money)
            print("AI money:%s" % self.ai.money)
            print("*****************************")
            self.single_round()

            if self.player1.money < 0:
                break

            if self.ai.money < 0:
                break

        print("\n\n-----------------Final Result------------------")
        if self.player1.money > self.ai.money:
            print("You win with Money:%s" % self.player1.money)
        elif self.ai.money == self.player1.money:
            print("Draw with equal money, no winner")
        else:
            print("AI win with Money:%s" % self.ai.money)


def main():
    p1 = Player()
    ai = AiPlayer()
    game = Game(p1, ai)
    game.start()
    total_games = 0
    wins = 0
    keep_playing = True
    while keep_playing:
        # Loop for quitting conditions
        while True:
            # User chooses to keep playing or quit
            print(wins, "wins", "/", total_games, "total games")
            keep_playing = input("Play again? (Y/N): ")
            keep_playing = keep_playing.upper()

            if keep_playing == 'Y':

                break


            elif keep_playing == 'N':

                print('\nThanks for playing!\n')

                keep_playing = False

                # exit()
                return 'q', wins, total_games


            else:

                print('Invalid entry')

                continue


if __name__ == "__main__":
    main()
