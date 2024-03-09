import random
import sys
import numpy
tools = {'Rock': '🚑', 'Paper': '📜', 'Scissor': '✂'}
tool_names = ['Rock', 'Paper', 'Scissor']


def game():
    while True:
        ai_choice = random.choice(tool_names)
        your_choice = input('\nRock Paper or Scissor? ')
        your_choice = your_choice.capitalize()
        while your_choice not in tool_names and your_choice != 'Exit':
            print('You can just select between [ Rock , Paper , Scissor ]')
            your_choice = input('Select again: ')
        if your_choice in tool_names:
            print()
            print(f'Ai:  {tools[ai_choice]}')
            print()
            print(f'Human:  {tools[your_choice]}\n-----------------')
        if ai_choice == 'Rock' and your_choice == 'Paper':
            print('Human won')
        elif ai_choice == 'Rock' and your_choice == 'Scissor':
            print('Ai won')
        elif ai_choice == 'Rock' and your_choice == 'Rock':
            print('Tie')
        elif ai_choice == 'Paper' and your_choice == 'Rock':
            print('Ai won')
        elif ai_choice == 'Paper' and your_choice == 'Scissor':
            print('Human won')
        elif ai_choice == 'Paper' and your_choice == 'Paper':
            print('Tie')
        elif ai_choice == 'Scissor' and your_choice == 'Rock':
            print('Human won')
        elif ai_choice == 'Scissor' and your_choice == 'Scissor':
            print('Tie')
        elif ai_choice == 'Scissor' and your_choice == 'Paper':
            print('Ai won')
        if your_choice.lower() == 'exit':
            sys.exit()


game()
