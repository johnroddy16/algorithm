# write an algorithm that will check a player's score in black jack
# after each deal and adjust the value of an Ace when necessary:

import random 

import time 

p_cards = []

d_cards = []

cards = ['A', 'A', 'A', 'A', 'K', 'K', 'K', 'K', 'Q', 'Q', 'Q', 'Q', 'J', 'J',
    'J', 'J', 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6,
    6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2]


popped_cards = []

removed_aces = []

d_r_a = []

b = 0
while b < 2:
    e = random.randint(0, len(cards) - 1)
    p_cards.append(cards[e])
    a = cards.pop(e)
    popped_cards.append(a)
    g = random.randint(0, len(cards) - 1)
    d_cards.append(cards[g])
    h = cards.pop(g)
    popped_cards.append(h)
    b += 1

def add_score():
    total = 0
    for c in p_cards:
        if c in ['K', 'Q', 'J']:
            total += 10
        elif c == 'A':
            total += 11
        else:
            total += c 
    print(total)
    if total == 21:
        print('You win with 21!')
        print('your cards,', p_cards)
        exit() 
    x = True
    while x:
        deal = input(f'You have {p_cards + removed_aces} and the dealer has {d_cards[1]} and some other card. Would you like another card? Type y or n ').lower()
        if deal == 'n':
            print(f'You end with a total of {total}.')
            return total
        y = random.randint(0, len(cards) - 1)
        p_cards.append(cards[y])
        p = cards.pop(y)
        popped_cards.append(p)
        print('card,', p)
        if p in ['K', 'Q', 'J']:
            total += 10
        elif p == 'A':
            total += 11 
        else:
            total += p
        if total > 21 and 'A' in p_cards:
            total -= 10
            p_cards.remove('A')
            removed_aces.append('A')
        if total == 21:
            print('You win the game with a 21!')
            print('your cards,', p_cards + removed_aces, 'dealer cards,', d_cards)
            exit()
        if total > 21:
            print('You went over 21 and you lose!')
            print('your cards,', p_cards + removed_aces, 'dealer cards,', d_cards)
            exit()
            
        


v = add_score()
print()

dealer_total = 0
for a in d_cards:
    if a in ['K', 'Q', 'J']:
        dealer_total += 10
    elif a == 'A':
        dealer_total += 11
    else:
        dealer_total += a 

while dealer_total <= v:
    x = random.randint(0, len(cards) - 1)
    d_cards.append(cards[x])
    a = cards.pop(x)
    popped_cards.append(a)
    print('card,', a)
    if a in ['K', 'Q', 'J']:
        dealer_total += 10
    elif a == 'A':
        dealer_total += 11
    else:
        dealer_total += a
    if dealer_total > 21 and 'A' in d_cards:
        dealer_total -= 10
        d_cards.remove('A')
        d_r_a.append('A')
    if dealer_total == 21:
        print('The dealer wins with a 21!')
        print(f'your cards,', p_cards + removed_aces, 'dealer cards', d_cards + d_r_a)
        exit()
    if dealer_total > 21:
        print('The dealer went over 21 and you win!')
        print(f'your cards,', p_cards + removed_aces, 'dealer cards', d_cards + d_r_a)
        exit()

print(f'the dealer has {d_cards + d_r_a} for a total of {dealer_total}.')
if dealer_total > v:
    print('Dealer wins, you lose!')
elif dealer_total < v:
    print('You win!')
else:
    print('Draw!')
# print(len(cards))
player_cards = p_cards + removed_aces
print('player cards,', player_cards)
dealer_cards = d_cards + d_r_a
print('dealer cards,', dealer_cards)