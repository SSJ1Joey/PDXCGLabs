

def check_palindrome():
    x = input('Give me a word: ').lower()

    print(f'You typed the word: {x}')

    word = list(x)
    s_word = list(x)

    word.reverse()

    if word == s_word:
        print(f'{x}: is a palindrome.')
    else:
        print(f'{x}: is not a palindrome...')


#check_palindrome()    
    


def check_anagram():
    f_word = input('Please give me a word to check: ').lower()
    s_word = input('Please give a second word to check: ').lower()

    print(f'You typed {f_word} and {s_word}.')
    
    word1 = list(f_word)
    word2 = list(s_word)

    word1.sort()
    word2.sort()

    if word1 == word2:
        print(f'{f_word} and {s_word}: are anagrams.')
    else:
        print(f'{f_word} and {s_word}: are not anagrams...')

    
#check_anagram()
