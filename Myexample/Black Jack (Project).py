# We are gonna create a Game that selects a deck of cards and equally divide it into two players.
# The both player takes a card from their deck and place it.....The player which have high value wins.
# Say six of hearts > four of diamonds
# Player 1 Wins
# If the game ties or they both put same value cards then another chance will be given to each player and before that player can put..
# ..any number of cards over the matching ones.
# The player that wins in next chance will take all the cards.
# The player that ends up having 0 card will lose and the game will end.

# GAME LOGIC :- we will create a CARD() class


import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card(object):
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return self.rank+ " of " + self.suit


# We create a new DECK() class

class Deck():
    def __init__(self):
        self.all_card= []
        for suit in suits:
            for rank in ranks:
                # Create a card object here
                card_created = Card(suit,rank)
                self.all_card.append(card_created)

    def shuffle(self):
        random.shuffle(self.all_card)

    def Pop_one(self):
        return self.all_card.pop()


decks = Deck()
# Without giving a proper indexing to the list, it will just show us random locations of the list objects stored in our computer location.
decks.shuffle()
my_cards= decks.Pop_one()



class Player():
    def __init__(self,name):
        self.name = name
        self.all_card= []

    def remove_one(self):
        return self.all_card.pop(0)

    def add_card(self,new_cards):
        self.new_cards = new_cards
        if type(self.new_cards) == type([]):
            self.all_card.extend(new_cards)
        else:
            self.all_card.append(new_cards)

    def __str__(self):
        return f'{self.name} has {len(self.all_card)} card(s).'

##############  START GAME ###############

player_one = Player("Nilabh")
player_two = Player("Munni")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_card(new_deck.Pop_one())
    player_two.add_card(new_deck.Pop_one())

game_on = True

round_num = 0
while game_on:
    round_num +=1
    print(f'Round {round_num}')

    if len(player_one.all_card) == 0:
        print("Player One has 0 cards! Player two wins!")
        game_on=False
        break

    if len(player_two.all_card)== 0:
        print("Player two has 0 cards ! Player one wins!")
        game_on= False
        break
    # New Round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # At War
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war= False


        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_card(player_two_cards)
            player_two.add_card(player_one_cards)
            at_war= False

        else:
            print('WARRRR!!!!')

            if len(player_one.all_card) < 3:
                print("The Player ONE cannot War")
                print("Player TWO WINS!!!")
                game_on= False
                break

            elif len(player_two.all_card) < 3:
                print("The Player TWO cannot War")
                print("Player ONE WINS!!!")
                game_on= False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

