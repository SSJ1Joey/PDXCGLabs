


def calc():
    user_op = input("What is the operation you'd like to perform?: ")
    user_num = int(input('What is your first number?: '))
    user_num2 = int(input('What is your second number?: '))
    if user_op == '+':
        ants = user_num + user_num2
    elif user_op == '-':
        ants = user_num - user_num2
    elif user_op == '*':
        ants = user_num * user_num2
    elif user_op == '/':
        ants = user_num / user_num2
    print(f'{user_num} {user_op} {user_num2} = {ants}')




calc()
