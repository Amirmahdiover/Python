import secrets
import string


def upper_case(password):
    for char in password:
        if char.isupper():
            return 'True'

    return 'False'


def symbol(password):
    for char in password:
        if char in string.punctuation:
            return 'True'

    return 'False'


def generate_password(length: int, uppercase: bool, symbol: bool):
    check_u = True
    check_s = True
    while check_u or check_s:
        check_u = True
        check_s = True
        combination = string.digits + string.ascii_lowercase
        new_password = ''
        if uppercase:
            combination += string.ascii_uppercase
        if symbol:
            combination += string.punctuation

        combination_len = len(combination)
        for item in range(length):
            new_password += combination[secrets.randbelow(combination_len)]
        if uppercase:
            for char in new_password:
                if char.isupper():
                    check_u = False
                # check_u = True
        else:
            check_u = False
        if symbol:
            for char in new_password:
                if char in string.punctuation:
                    check_s = False
        else:
            check_s = False
            # pass

            # check_s = True
    return new_password


if __name__ == '__main__':
    password = generate_password(10, False, False)
    symbol_checker = symbol(password)
    uppercase_checker = upper_case(password)
    print(f'password:{password}  (uppercase:{uppercase_checker},sybmol:{symbol_checker})')
