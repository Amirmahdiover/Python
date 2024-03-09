import random

guess_number = random.randint(1, 10)


def ask_num():
    global guess
    while True:
        try:
            guess = int(input('Guess num: '))
            break
        except:
            print('please enter a valid number')


ask_num()
while guess != guess_number:
    if guess_number > guess:
        print('higher')
        ask_num()
    else:
        print('lower')
        ask_num()
print(f'right guess number is {guess_number}')
