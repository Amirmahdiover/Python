from random import randint
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
x=1
number = randint(0,100)
# print(number)
chosen_number=int(input("Enter your lucky number: "))
while chosen_number != number:
    if  chosen_number < 1 or chosen_number > 100:
        print('OUT OF BOUNDS')
        chosen_number = int(input("Enter your lucky number: "))
        x += 1
    elif chosen_number <= number + 10 and chosen_number >= number:
        print("WARM!")
        break
        chosen_number = int(input("Enter your lucky number: "))
    elif chosen_number >= number - 10 and chosen_number <= number:
        print("WARM!")
        break
        chosen_number = int(input("Enter your lucky number: "))
    elif chosen_number >= number+10 or chosen_number <= number-10:
        print("COLD!")
        break
        chosen_number = int(input("Enter your lucky number: "))
chosen_number2 = int(input("Enter your lucky number: "))
x+=1
while chosen_number2 != number:
    if abs(chosen_number2 - number) > abs(chosen_number - number):
        print('COLDER!')
        chosen_number2 = int(input("Enter your lucky number: "))
        x += 1
    elif abs(chosen_number2 - number) < abs(chosen_number - number):
        print('WARMER!')
        chosen_number2 = int(input("Enter your lucky number: "))
        x += 1


print(f'YOU GUESSED IT IN {x} times')
print('guessed correctly')
