from random import randint

guesses = [0]
num = randint(0, 100)
print(num)
while True:
    guess = int(input('Enter your number: '))
    if guess < 1 or guess > 100:
        print('out of bound')
        continue
    if num == guess:
        print(f'afarin to dar {len(guesses)} hads zadi')
        break
    guesses.append(guess)
    if guesses[-2]:
        if abs(num - guess) > abs(num - guesses[-2]):
            print('COLDER!')
            continue
        elif abs(num - guess) < abs(num - guesses[-2]):
            print('WAROMER!')
            continue

    if abs(num - guess) <= 10:
        print("WARM!")
    elif abs(num - guess) >= 10:
        print("COLD!")
