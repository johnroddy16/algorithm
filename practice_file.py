x = 'A'
print(type(x))

# write an algorithm that will check a player's score in black jack
# after each deal and adjust the value of an Ace when necessary:

import random 

p_cards = ['A', 4]

cards = ['A', 'A', 'A', 'K', 'K', 'K', 'K', 'Q', 'Q', 'Q', 'Q', 'J', 'J',
    'J', 'J', 10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6,
    6, 6, 5, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2]

popped_cards = []

removed_aces = []

def add_score():
    total = 0
    for c in p_cards:
        if c in ['K', 'Q', 'J']:
            total += 10
        elif c == 'A':
            total += 11
        else:
            total += c 
    x = True
    while x:
        y = random.randint(0, len(cards) - 1)
        p_cards.append(cards[y])
        p = cards.pop(y)
        popped_cards.append(p)
        if cards[y] in ['K', 'Q', 'J']:
            total += 10
        elif cards[y] == 'A':
            total += 11 
        else:
            total += cards[y]
        if total == 21:
            return total
        while total > 21 and 'A' in p_cards:
            total -= 10
            p_cards.remove('A')
            removed_aces.append('A')
        if total > 21:
            return total 
            
        # s += 1
        # if s == 4: 
        #     return total 



v = add_score()
print(v)

print(p_cards)
print(len(cards))
print(removed_aces)
print(popped_cards)