import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

Game_start = True
Game_start

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]
    def __str__(self):
        return self.rank +" of "+ self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                cards = Card(suit,rank)
                self.deck.append(cards)
    def __str__(self):
        deck = ''
        for card in self.deck:
            deck = deck +'\n'+card.__str__()
        return "Cards are: " + deck

    def shuffle(self):
        random.shuffle(self.deck)

    def Take_one(self):
        return self.deck.pop()

class Cards_Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        self.cards.append(card)    # A lot of stuff happend here
        self.value = self.value + values[card.rank]
        if card.rank == "Ace":
            self.aces =self.aces + 1    #add to self.aces

    def ace_adjust(self):
        while self.value >21 and self.aces:
            self.value = self.value - 10
            self.aces = self.aces -1

class Tokens:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def bet_win(self):
        self.total = self.total + self.bet

    def bet_lose(self):
        self.total = self.total - self.bet

def take_bet(Tokens):
    Game_on = True
    while Game_on:
        try:
            Tokens.bet =int(input("Enter number of tokens you eant to bet: "))
        except ValueError:
            print("Sorry, enter a integer value!!")
        else:
            if Tokens.bet > Tokens.total:
                print("Sorry !! You dont have enough Tokens."+"\n"+Tokens.total)
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.Take_one())
    hand.ace_adjust()

def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("You want to hit or stand? Enter 'h' or 's': ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Stands. Player 2 is playng.")
        else:
            print("Sorry, try again!!")
            continue
        break

def show_few(player,dealer):
    print("\nDealer's Hand:")
    print("<Card Hidden>")
    print("",dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep ='\n')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep= '\n')
    print("Dealer's Hand = ", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep= '\n ')
    print("\nPlayer's Hand =", player.value)

# Functions to handle end of game scenerios

def player_busts(player, dealer,Tokens):
    print("Player busts!")
    Tokens.bet_lose()

def player_wins(player,dealer,Tokens):
    print("Player Wins!!")
    Tokens.bet_win()

def dealer_busts(player,dealer,Tokens):
    print("Dealer Busts!!")
    Tokens.bet_win()

def dealer_wins(player,dealer, Tokens):
    print("Dealer Wins!!")
    Tokens.bet_lose()

def push(player,dealer):
    print("Both Tie!! It's a push.")

while True:
    print("Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.")

    deck = Deck()
    deck.shuffle()

    player_hand = Cards_Hand()
    player_hand.add_card(deck.Take_one())
    player_hand.add_card(deck.Take_one())

    dealer_hand =Cards_Hand()
    dealer_hand.add_card(deck.Take_one())
    dealer_hand.add_card(deck.Take_one())
# Set up player Tokens
    player_tokens = Tokens() # defualt value is 100
# Prompting the player for their bet
    take_bet(player_tokens)
# Show cards but keep one dealer card hidden
    while True:
        hit_or_stand(deck,player_hand) # Prompt for player to either hit or stand
        show_few(player_hand,dealer_hand) # Show cards but one dealer card is hidden

    # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_tokens)
            break

# If player hasn't busted, play dealer's hand until dealer reaches 17
    if player_hand.value <=21:
        while dealer_hand.value<17:
            hit(deck, dealer_hand)
        show_all(player_hand,dealer_hand) #Show all cards

        if dealer_hand.value >21:
            dealer_busts(player_hand,dealer_hand,player_tokens)

        elif dealer_hand.value > player_hand.value:
            dealer_busts(player_hand,dealer_hand,player_tokens)

        elif dealer_hand.value < player_hand.value:
            dealer_busts(player_hand,dealer_hand,player_tokens)

        else:
            push(player_hand,dealer_hand)

# Informing player about his total tokens left
    print("\nPlayer's Winnings stand at", player_tokens.total)
# Ask to play again!!
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() =='y':
        playing = True
        continue
    elif new_game[0].lower() != 'y' or 'n':
        print("Choose either 'y' or 'n' ")
    else:
        print("Thank You for playing!!!")
        break




