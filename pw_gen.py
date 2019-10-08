import random
import string

def main(pw_length = 10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(pw_length))


print('Here is your random password:', main())
