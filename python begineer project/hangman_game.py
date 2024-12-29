import random
from collections import Counter

someWords = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split()

word = random.choice(someWords)

if __name__ == "__main__":
    print('Guess the word! HINT: the word is the name of a fruit')
    print(' '.join(['_' for _ in word]))

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: ')).lower()
            except KeyboardInterrupt:
                print()
                print('Bye! Try again.')
                exit()

            if not guess.isalpha():
                print('Enter only a letter!')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE LETTER')
                continue

            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                    correct += 1
                else:
                    print('_', end=' ')

            if Counter(letterGuessed) == Counter(word):
                print('\nThe word is:', word)
                flag = 1
                print('Congratulations, you won!')
                break

        if chances <= 0 and Counter(letterGuessed) != Counter(word):
            print()
            print('You lost! Try again..')
            print('The word was', word)

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
