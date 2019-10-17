#Write a dictionary comprehension to print each letter of the alphabet and its correstponding ASCII code

import string
print({char: ord(char) for char in string.ascii_lowercase})



