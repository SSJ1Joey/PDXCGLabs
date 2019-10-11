import random

print('Hello, lets ask the ball a question.\n')
print('****' * 9)

preds = [
    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'Yes definitely',
    'You may rely on it',
    'As I see it, yes',
    'Most likely',
    'Outlook good',
    'Yes',
    'Signs point to yes',
    'Reply hazy try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    "Don't count on it",
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful' ]

def game():
    question = input('Ask me anything: ')
    answer = random.choice(preds)
    print(answer)
    cont = input('Would you like to ask me anything else? (y/n): ')
    if cont == 'y':
        input('Ask me another question: ')
        print(answer)
    else:
        print('Thank you, come again!')

game()
