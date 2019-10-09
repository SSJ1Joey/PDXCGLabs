


def calc():
    user_op = input("What is the operation you'd like to perform?: ")
    user_num = int(input('What is your first number?: '))
    user_num2 = int(input('What is your second number?: '))
    if user_op == '+':
        print(user_num + user_num2)
    elif user_op == '-':
        print(user_num - user_num2)
    elif user_op == '*':
        print(user_num * user_num2)
    elif user_op == '/':
        print(user_num / user_num2)




calc()
