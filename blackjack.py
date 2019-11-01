 
def blackjack():
    
    cards = []

    print('Choose 3 cards: A,K,Q,J,10,9,8,7,6,5,4,3,2\n')

    x = input('What is your first card?: ')
    if x == 'A':
        cards.append('1')
    elif x == 'K':
        cards.append('10')
    elif x == 'Q':
        cards.append('10')
    elif x == 'J':
        cards.append('10')
    else:
        cards.append(x)

    y = input('What is your second card?: ')
    if y == 'A':
        cards.append('1')
    elif y == 'K':
        cards.append('10')
    elif y == 'Q':
        cards.append('10')
    elif y == 'J':
        cards.append('10')
    else:
        cards.append(y)

    z = input('What is your third card?: ')
    if z == 'A':
        cards.append('1')
    elif z == 'K':
        cards.append('10')
    elif z == 'Q':
        cards.append('10')
    elif z == 'J':
        cards.append('10')
    else:
        cards.append(z)

    for i in range(len(cards)):
        cards[i] = int(cards[i])

    print(cards)


    if sum(cards) == 21:
        print('Blackjack!')

    elif sum(cards) < 17:
        print('Hit')

    elif sum(cards) >= 17 and sum(cards) < 21:
        print('Stay')

    else:
        print('Busted')

blackjack()
