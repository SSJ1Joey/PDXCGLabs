import random

balance = 0


def pick_6():
    luck = range(1, 100)
    numbers = []
    first = random.choice(luck) 
    second = random.choice(luck) 
    third = random.choice(luck) 
    forth = random.choice(luck) 
    fifth = random.choice(luck) 
    sixth = random.choice(luck) 
    numbers.append(first)
    numbers.append(second)
    numbers.append(third)
    numbers.append(forth)
    numbers.append(fifth)
    numbers.append(sixth)

def ticket():
    t_list = []
    for item in range(6):
        nums = int(input('Please pick 6 numbers form 1 - 99: '))
        t_list.append(nums)
    print(f'You chose {t_list}')
           

def jackpot():
    if ticket() == pick_6():
        print('You won the Jackpot!(25,000)')
        balance += 25000
    else:
        print('sorry no win')
    

ticket(pick_6())

    


    



pick_6()


