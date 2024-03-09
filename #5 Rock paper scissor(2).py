import random
import sys


class Rps():
    # def __init__(self):
    #     self.tools = {'rock': '🚑', 'paper': '📜', 'scissor': '✂'}
    #     self.validtools = list(self.tools.keys())
    tools = {'rock': '🚑', 'paper': '📜', 'scissor': '✂'}
    validtools = list(tools.keys())
    def play_game(self):
        your_choice = input('rock,paper,or scissors? ')
        ai_choice = random.choice(self.validtools)
        if your_choice.lower() == 'exit':
            print('thanks for playing')
            sys.exit()
        if your_choice not in self.validtools:
            print('valid tool')
            return self.play_game()
        self.display(your_choice, ai_choice)
        self.check(your_choice, ai_choice)

    def display(self, your_choice, ai_choice):
        print('-------------')
        print(f'Ai: {self.tools[ai_choice]}')
        print(f'Human: {self.tools[your_choice]}')
        print('-------------')

    def check(self, your_choice, ai_choice):
        if your_choice == ai_choice:
            print('Tie')
        elif your_choice == 'rock' and ai_choice == 'scissor':
            print('you won')
        elif your_choice == 'scissors' and ai_choice == 'paper':
            print('you won')
        elif your_choice == 'paper' and ai_choice == 'rock':
            print('you won')
        else:
            print('ai won')


if __name__ == '__main__':
    object1 = Rps()
    while True:
        object1.play_game()
