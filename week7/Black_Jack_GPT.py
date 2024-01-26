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
outcome = ""
score = 0
next_deal =""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if suit in SUITS and rank in RANKS:
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card:", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (
            CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit),
        )
        canvas.draw_image(
            card_images,
            card_loc,
            CARD_SIZE,
            [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
            CARD_SIZE,
        )


# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return "Hand contains " + " ".join(str(card) for card in self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = sum(VALUES[card.get_rank()] for card in self.cards)
        for card in self.cards:
            if card.get_rank() == "A" and value + 10 <= 21:
                value += 10
        return value

    def draw(self, canvas, pos):
        for i, card in enumerate(self.cards):
            card.draw(canvas, [pos[0] + i * 80, pos[1]])


# define deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __str__(self):
        return "Deck contains " + " ".join(str(card) for card in self.cards)


# define event handlers for buttons
def deal():
    global outcome, in_play, score, deck, player_hand, dealer_hand,next_deal

    if in_play:
        outcome = "Player forfeits. New deal started. "
        score -= 1

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())

    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    in_play = True
    outcome = "Hit or stand?"
    next_deal = ""

def hit():
    global in_play, score, outcome ,next_deal

    if in_play:
        player_hand.add_card(deck.deal_card())

        if player_hand.get_value() > 21:
            outcome = "You went bust and lose"
            next_deal = "New deal?"
            score -= 1
            in_play = False


def stand():
    global in_play, score, outcome,next_deal

    if not in_play:
        return

    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())

    if dealer_hand.get_value() > 21 or dealer_hand.get_value() < player_hand.get_value():
        outcome = "You win!"
        next_deal = "New deal?"
        score += 1
    else:
        outcome = "You lose."
        next_deal = "New deal?"
        score -= 1

    in_play = False


# draw handler
def draw(canvas):
    canvas.draw_text("Blackjack", (80, 80), 48, "Cyan")
    canvas.draw_text("Score: " + str(score), (400, 80), 36, "Black")
    canvas.draw_text("Dealer", (80, 160), 36, "Black")
    canvas.draw_text(outcome, (280, 160), 24, "Black")
    canvas.draw_text(next_deal, (280, 380), 24, "Black")
    canvas.draw_text("Player", (80, 380), 36, "Black")

    dealer_hand.draw(canvas, [80, 180])

    if in_play:
        canvas.draw_image(
            card_back,
            CARD_BACK_CENTER,
            CARD_BACK_SIZE,
            [80 + CARD_BACK_CENTER[0], 180 + CARD_BACK_CENTER[1]],
            CARD_BACK_SIZE,
        )

    player_hand.draw(canvas, [80, 410])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
