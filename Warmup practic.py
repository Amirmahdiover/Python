def lesser_two(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 > num2:
            return num2
        else:
            return num1
    else:
        if num1 > num2:
            return num1
        else:
            return num2


# print(lesser_two(45, 35))

def animal_crackers(text):
    text = text.split()
    return text[0][0].upper() == text[1][0].upper()


# print(animal_crackers('salam Shetori'))

def check_twenty(num1, num2):
    if sum((num1, num2)) == 20 or num2 == 20 or num1 == 20:
        return True
    else:
        return False

# print(check_twenty(8, 20))
