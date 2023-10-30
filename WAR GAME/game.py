#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        # Creating a Deck of Cards (52) using SUITE (4) and DECK (13)
        print("Inside Deck Constructor")
        self.allcards=[(s,r)for s in SUITE for r in RANKS]
        # print(self.allcards)

    def shuffle(self):
        # Shuffling the deck of cards for a FAIR game before splitting
        print("Shuffling Deck ...")
        shuffle(self.allcards)

    def split_deck_half(self):
        # Splitting the deck in half after shuffling so as to start game
        return self.allcards[:26], self.allcards[26:]

class Hand:
    """
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    """
    def __init__(self,cards):
        self.cards=cards

    def __str__(self):
        # report the number of cards that player have in hand
        return "Contains {} cards".format(len(self.cards))

    def add(self,more_cards):
        # add new cards that player had in his current set of cards
        self.cards.extend(more_cards)

    def remove_card(self):
        # removing cards from player's deck
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
        # initialsing name and instance of class
        self.name=name
        self.hand=hand

    def play_cards(self):
        # drawn_card is basically the card which player removes from his set of cards
        drawn_card=self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        return drawn_card

    def remove_war_cards(self):
        # remove first 3 war cards
        war_cards=[]
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for i in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        """
        Return True if player is still left with cards in hand.
        """
        return len(self.hand.cards)!=0

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Create a new deck and split it in half
d=Deck()
d.shuffle()
half1,half2=d.split_deck_half()

# Create both players
# Hand class will be initialised with half cards
comp=Player("computer",Hand(half1))

name=input("What is your name? ")
player=Player(name,Hand(half2))

total_rounds=0
war_count=0

while player.still_has_cards() and comp.still_has_cards():
    total_rounds+=1
    print("Time for a new round")
    print("Here are the current standings")
    print(player.name+"has the count: "+str(len(player.hand.cards)))
    print(comp.name+"has the count: "+str(len(comp.hand.cards)))
    print("Both Players play a card  !!")
    print("\n")

    # cards thrown on table by player and computer
    table_card=[]
    c_card=comp.play_cards()
    p_card=player.play_cards()

    table_card.append(c_card)
    table_card.append(p_card)

    if c_card[1]==p_card[1]:
        war_count+=1
        print("War!!")
        table_card.extend(player.remove_war_cards())
        table_card.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1])<RANKS.index(p_card[1]):
            print(player.name + " has the higher card, adding to hand.")
            user.hand.add(table_card)
        else:
            # even in case of tie computer will get all cards
            print(comp.name + " has the higher card, adding to hand.")
            comp.hand.add(table_card)

    else:
        if RANKS.index(c_card[1])<RANKS.index(p_card[1]):
            print(player.name + " has the higher card, adding to hand.")
            player.hand.add(table_card)
        else:
            # even in case of tie computer will get all cards
            print(comp.name + " has the higher card, adding to hand.")
            comp.hand.add(table_card)


print("Game over, number of rounds: "+str(total_rounds))
print("A WAR happend "+str(war_count)+" times")
print("Does Computer have cards ?",comp.still_has_cards())
print("Does Player have have cards",player.still_has_cards())
