from random import choice

words = ['Google', 'Apple', 'Microsoft', 'Amazon', 'Facebook']

sl_word = choice(words)


def game():
    name = input('What is your name? ')
    print(f'Welcome to the hangman {name}')
    dashes = '-' * len(sl_word)
    print(f'Word: {dashes}')
    sep_dashes = [dash for dash in dashes]
    counter = 3
    while True:
        letter = input('Enter a letter: ')
        if letter in sl_word.lower():
            print('Right guess')
            for index, item in enumerate(sl_word.lower()):
                if item == letter:
                    sep_dashes[index] = letter
                    print(*sep_dashes)
        else:
            print(*sep_dashes)
            if counter <= 1:
                print('you lost the word was ', sl_word)
                break
            counter -= 1
            print(f'wrong guess {counter} tries left.')
        if ''.join(sep_dashes) == sl_word.lower():
            print('Congratulations you guessed right the word was ', sl_word)
            break


game()
