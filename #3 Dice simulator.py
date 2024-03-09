import random


#
# while True:
#     result = ''
#     number_dices = input('how many dice you wanna have: ')
#     try:
#         for item in range(int(number_dices)):
#             result += str(random.randint(1, 6)) + ','
#         print(result[:-1])
#     except:
#         if str(number_dices) == 'exit':
#             break
def dices_list(amount=2):
    if amount < 0:
        raise NameError
    dices = []
    for item in range(amount):
        dices.append(random.randint(1, 6))
    sum1=0
    for item in dices:
        sum1 += item
    # print(sum1)
    return dices,sum1


def final():
    while True:
        try:
            number = input('How many dices you want? ')
            if number.lower() == 'exit':
                print('thanks for playing')
                break
            print(*dices_list(int(number)), sep=',')
        except ValueError:
            print('wrong input')


if __name__ == '__main__':
    final()
