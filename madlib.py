import random

print("Welcome to Mad Libs!")

answer = ['yes' , 'no']
noun = input("Give me 3 nouns separated by commas: ")
n = noun.split()
noun_plural = input("Give me a plural noun: ")
place = input("Name a place: ")
adj = input("Give me an adjective: ")

userQuestion = input("Would you like to see your madlib? [yes or no]: ")



mad = print(f"Be kind to your {random.choice(n)}-footed {random.choice(n)}. For a duck may be somebody`s {noun_plural}. Be kind to your {random.choice(n)} in {place}. Where the weather is always {adj}. You may think that this is the {random.choice(n)}. Well it is.")
