from random import choice


def game():
    name = input('What is your name? ')
    print(f'Welcome to the hangman {name}')
    sl_word = choice(['Google', 'Apple', 'Microsoft', 'Amazon', 'Facebook'])
    guessed = ''
    tries = 3
    while tries > 0:
        blanks = 0
        for char in sl_word:
            if char in guessed:
                print(char, end='')
            else:
                blanks += 1
                print('-', end='')
        if blanks == 0:
            print('')
            print(f'the word was {sl_word}')
            print('you won')
            break
        print('')
        guess = input('Enter word: ')
        if len(guess) > len(sl_word):
            print("don't cheat")
            guess = ''
        if guess in guessed:
            print('you entered this letter already')
        guessed += guess
        if guess not in sl_word:
            tries -= 1
            print('wrong letter')
            print(f'you have {tries} more tries')


game()
