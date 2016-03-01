# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Going on!!!"
score = 0
text="Hit or Stand ?"

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards_list=[]
        self.value=0

    def __str__(self):
        pass	# return a string representation of a hand

    def add_card(self, card):
        pass	# add a card object to a hand
        self.cards_list.append(card)
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        pass	# compute the value of the hand, see Blackjack video
        flag=0
        self.value=0 
        for c in self.cards_list:
            if(c.get_rank()=='A'):
                flag+=1;
        if(flag==0):
            for c in self.cards_list:
                self.value+=VALUES.get(c.get_rank())
                print self.value
        if(flag==1):
            for c in self.cards_list:
                self.value+=VALUES.get(c.get_rank())
                print self.value
                if(self.value+10<=21):
                    self.value+=10
        if(flag>1):
            for c in self.cards_list:
                self.value+=VALUES.get(c.get_rank())
                if(self.value+10<=21):
                    self.value+=10
        return self.value
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards
        for c in self.cards_list:
            c.draw(canvas,pos)
            pos[0]+=72
        
# define deck class 
class Deck:
    def __init__(self):
        pass	# create a Deck object
        self.number=range(1,53)
        self.num=0
        self.c=Card('S','2')
    def shuffle(self):
        # shuffle the deck 
        pass    # use random.shuffle()
        random.shuffle(self.number)
    def deal_card(self):
        pass	# deal a card object from the deck
        v=self.number[self.num]
        self.c=Card(SUITS[v//13],RANKS[v%13])
        self.num+=1;
        return self.c
    def __str__(self):
        pass	# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play,dealer_hand,player_hand,deck,outcome
    deck=Deck()
    deck.shuffle()
    # your code goes here
    dealer_hand=Hand()
    player_hand=Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    in_play = True
    outcome="Going On!!!"
def hit():
    global outcome,text,score
    pass	# replace with your code below
    # if the hand is in play, hit the player
    if(in_play):
        player_hand.add_card(deck.deal_card())
        print player_hand.get_value()
        if(player_hand.get_value()>=21):
            score-=1
            outcome="Dealer Wins!!"
            print score
    else:
        dealer_hand.add_card(deck.deal_card())
        #if(dealer_hand.get_value()>21):
            #   score+=1
            #	 outcome="Player Wins"
            # print score
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome,text,in_play,score
    pass	# replace with your code below
    if(in_play==True):
        in_play=False
        while(dealer_hand.get_value()<17):
            hit()
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        
    # assign a message to outcome, update in_play and score
        if(dealer_hand.get_value()>21):
            outcome="Player Wins!!"
            score+=1
        elif(dealer_hand.get_value()>player_hand.get_value()):
            outcome="dealer Wins!!"
            score-=1
        else:
            outcome="Player Wins!!"
            score+=1
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BLACKJACK",[50,80],60,"Red")
    card_loc1 = (CARD_BACK_CENTER[0], 
                    CARD_BACK_CENTER[1])
    canvas.draw_image(card_back, card_loc1, CARD_SIZE, [100 + CARD_CENTER[0], 100 + CARD_CENTER[1]], CARD_SIZE)    
    dealer_hand.draw(canvas,[172,100])
    player_hand.draw(canvas,[100,200])
    canvas.draw_text(outcome,[50,400],60,"Blue")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric