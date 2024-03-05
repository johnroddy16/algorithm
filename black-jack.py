# black jack game in python:

import random 

cards = ['A', 'A', 'A', 'A', 'K', 'K', 'K', 'K', 'Q', 'Q', 'Q', 'Q', 'J', 'J',
    'J', 'J', 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6,
    6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2]

player_cards = []
dealer_cards = []

dealt_cards = []




def sum_cards():
    ps = 0
    ds = 0
    for c in player_cards:
        try:
            ps = ps + c
        except:
            ps += 10
    for c in dealer_cards:
        try:
            ds = ds + c
        except:
            ds += 10
    return ps, ds 
                    
                
def another_card():
    ac = input('Would you like another card? Type y or n ').lower()
    if ac == 'y':
        x = random.randint(0, len(cards) - 1)
        player_cards.append(cards[x])
        print(player_cards)
        another_card()

             

def first_deal():
    x = 0
    while x < 2:
        p = random.randint(0, len(cards) - 1)
        player_cards.append(cards[p])
        r = cards.pop(p)
        dealt_cards.append(r)
        d = random.randint(0, len(cards) - 1)
        dealer_cards.append(cards[d])
        re = cards.pop(d)
        dealt_cards.append(re)
        x += 1
    print(f'You have {player_cards[0]} and {player_cards[1]}')
    print(f'The dealer has {dealer_cards[1]} and some other card')

def black_jack():
    print('Welcome to black jack, let\'s play a game with a fresh single deck!')
    first_deal() 
    x = sum_cards()
    p = x[0]
    d = x[1]
    print(f'Your score is {p}, the dealer\'s score is {d}')
    another_card()
    print(player_cards)



black_jack()