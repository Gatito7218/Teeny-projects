import random

print("Welcome to blackjack!\n")

def main():
    bank = 2000
    while True:
        bank = Game(bank)
        play_again = input("Would you like to play again? (y/n): ").strip().lower()
        if play_again == 'y':
            continue
        elif play_again == "n":
            break

face = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Card:
    def __init__(self, face):
        self.face = face
        self.hidden = True

        if face in ["Jack", "Queen", "King"]:
            self.value = 10
        elif face == "Ace":
            self.value = 11
        else:
            self.value = int(face)

    def __str__(self) -> str:
        if self.hidden:
            return 'Card'
        else:
            return self.face

class CardDeck:
    def __init__(self):
        self.deck = []

        for _ in range(5):
            for i in face:
                for j in range(4):
                    self.deck.append(Card(i))

    def __str__(self):
        deck_str = ""
        for card in self.deck:
            deck_str += str(card) + " "
        return deck_str.strip()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(0)

class Dealer:
    def __init__(self):
        self.dealer_hand = []

    def add(self, card):
        self.dealer_hand.append(card)

    def show_hand(self):
        for card in self.dealer_hand:
            card.hidden = False
        return ', '.join(str(card) for card in self.dealer_hand)

    def calculate_hand_value(self):
        value = sum(card.value for card in self.dealer_hand)
        #Case for aces (can be worth either 1 or 11)
        num_aces = sum(1 for card in self.dealer_hand if card.face == 'Ace')
        if num_aces:
            values = [value]
            for _ in range(num_aces):
                value -= 10
                values.append(value)
            return values
        return [value]

class Player:
    def __init__(self, bank):
        self.hand = []
        self.bank = bank
        self.bet_amount = 0

    def add(self, card):
        self.hand.append(card)

    def show_hand(self):
        for card in self.hand:
            card.hidden = False
        return ', '.join(str(card) for card in self.hand)

    def calculate_hand_value(self):
        value = sum(card.value for card in self.hand)
        #Case for aces (can be worth either 1 or 11)
        num_aces = sum(1 for card in self.hand if card.face == 'Ace')
        if num_aces:
            values = [value]
            for _ in range(num_aces):
                value -= 10
                values.append(value)
            return values
        return [value]

    def place_bet(self):
        while True:
            try:
                bet = float(input(f"Your current bank is {self.bank}. How much would you like to bet? "))
                if bet > 0 and bet <= self.bank:
                    self.bet_amount = bet
                    self.bank -= bet
                    print(f"You have bet {bet}. Your remaining bank is {self.bank}.")
                    break
                else:
                    print("Invalid bet amount. Please enter a value within your bank amount.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")


def winner(player, dealer):
    player_values = player.calculate_hand_value()
    dealer_values = dealer.calculate_hand_value()

    player_final = min(player_values, key=lambda x: (x > 21, x))
    dealer_final = min(dealer_values, key=lambda x: (x > 21, x))

    if max(player_values) == 21:
        return "Player wins!", True
    elif max(dealer_values) == 21:
        return "Dealer wins!", False
    elif player_final > 21:
        return "Player busts! Dealer wins!", False
    elif dealer_final > 21:
        return "Dealer busts! Player wins!", True
    elif player_final == dealer_final:
        return "It's a tie!", 1
    elif player_final > dealer_final:
        return "Player wins!", True
    else:
        return "Player Loses", False

def Game(bank):
    player = Player(bank=bank)
    dealer = Dealer()
    deck = CardDeck()
    deck.shuffle_deck()

    player.place_bet()

    for i in range(2):
        player.add(deck.deal_card())
        dealer.add(deck.deal_card())

    dealer.dealer_hand[0].hidden = False
    dealer.dealer_hand[1].hidden = True

    print("Player's Hand:")
    print(player.show_hand())
    player_values = player.calculate_hand_value()

    print("Dealer's Hand:")
    print(', '.join(str(card) for card in dealer.dealer_hand))

    # Player's turn
    while True:
        move = input("Do you want to hit or stay? (h/s): ").strip().lower()
        if move == 'h':
            player.add(deck.deal_card())
            print("Player's Hand:")
            print(player.show_hand())
            player_values = player.calculate_hand_value()
            if min(player_values) > 21:
                print("Player busts!")
                break
            if max(player_values) or min(player_values) == 21:
                player_wins = True
                break
        elif move == 's':
            break
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stay.")

    # Dealer's turn
    dealer.dealer_hand[1].hidden = False
    print("Dealer's Hand:")
    print(dealer.show_hand())
    dealer_values = dealer.calculate_hand_value()

    
    while min(dealer_values) < 17:
        dealer.add(deck.deal_card())
        print("Dealer's Hand:")
        print(dealer.show_hand())
        dealer_values = dealer.calculate_hand_value()
    
    result, player_wins = winner(player, dealer)
    print(result)

    if player_wins is True:
        winnings = 1.5 * player.bet_amount
        player.bank += winnings
        print(f"Player wins {winnings}! New bank amount: {player.bank}")
    elif player_wins is False:
        print(f"Player loses their bet {player.bet_amount}. New bank amount: {player.bank}")
    else:
        player.bank += player.bet_amount
        print(f"It's a tie! Bet amount of {player.bet_amount} is returned. New bank amount: {player.bank}")

    return player.bank

def main():
    bank = 1000
    while True:
        bank = Game(bank)
        play_again = input("Would you like to play again? (y/n): ").strip().lower()
        if play_again == 'y':
            continue
        elif play_again == "n":
            break

if __name__ == "__main__":
    main()

