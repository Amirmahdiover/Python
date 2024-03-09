def spy_game(my_list):
    add = True
    zero_count = 0
    for item in my_list:
        while add:
            if item == 0:
                zero_count += 1
                if zero_count == 2:
                    add = False
                    continue
            else:
                break
        while not add:
            if item == 7:
                return True
            else:
                break
    return False


# print(spy_game([1, 2, 4, 0, 0, 7, 5]))


def spy_game2(my_list2):
    code = [0, 0, 7, 'x']
    for item in my_list2:
        if item == code[0]:
            code.pop(0)
    return len(code) == 1


# print(spy_game2([1, 2, 4, 0, 0, 7, 5]))


def count_primes(number):
    counter = 2
    prime_list = [2, 3]
    if number == 2:
        prime_list.pop(1)
        print(prime_list)
        return 1
    for item in range(4, number + 1):
        for item2 in range(2, item):
            if item % item2 == 0:
                break
        else:
            prime_list.append(item)
            counter += 1
    print(prime_list)
    return counter


# print(count_primes(55))


def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x < num:
        for item in range(3, x, 2):
            if x % item == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


# print(count_primes2(55))


def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        if pattern == 2:
            pass
        print(patterns[pattern])

# print_big('a')