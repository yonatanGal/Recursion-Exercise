
def print_to_n(n):
    """ this function prints all the integers from 1 to n"""
    if n < 1:
        return
    elif n >= 1:
        print_to_n(n-1)
        print(n)


def print_reversed(n):
    """ this function prints all the integers from n to 1"""
    if n < 1:
        return
    if n >= 1:
        print(n)
        print_reversed(n-1)


def is_prime(n):
    """ this function checks if a given number n is prime """
    if n == 2:
        return True
    if has_divisor_smaller_than(n, n-1) is False:
        return True
    else:
        return False


def has_divisor_smaller_than(n, i):
    """ this function checks if a given number n has dividers which are
     smaller than i and bigger or equal to 2 """
    if n < 0:
        return True
    if i - 1 == 1:
        return False
    elif n % (i - 1) == 0:
        return True
    return has_divisor_smaller_than(n, i - 1)


def exp_n_x(n, x):
    """ this function gives a the sum of the exp powered by x series """
    if n == 0:
        return 1
    else:
        return (x**n)/factorial(n) + exp_n_x(n-1, x)


def factorial(n):
    """ this function calculates the factorial of a given number n """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def play_hanoi(hanoi, n, src, dest, temp):
    """ this function moves all the disks from src to dest according to the
    laws of the game """
    if n > 0:

        play_hanoi(hanoi, n-1, src, temp, dest)

        hanoi.move(src, dest)

        play_hanoi(hanoi, n-1, temp, dest, src)

    elif n <= 0:
        return


def print_sequences(char_list, n):
    """ this function receives a char list and returns all possible strings
    of n length """
    if n == 0:
        return
    k = len(char_list)
    print_sequences_rec(char_list, '', k, n)


def print_sequences_rec(char_list, sequence, k, n):
    """ this is the recursive function which runs on the char list
    and gives us all possible strings of length n """
    if n == 0:
        print(sequence)
        return
    for i in range(k):
        new_sequence = sequence + char_list[i]
        print_sequences_rec(char_list, new_sequence, k, n-1)


def print_no_repetition_sequences(char_list, n):
    """ same as print_sequences, but this time returns all strings of length
    n without repeating characters"""
    if n == 0:
        return
    k = len(char_list)
    print_no_repetition_sequences_rec(char_list, '', k, n)


def print_no_repetition_sequences_rec(char_list, sequence, k, n):
    """ this is the recursive function which runs on the char list
    and gives us all possible strings of length n, without repeating
    characters"""
    if n == 0:
        print(sequence)
        return
    for i in range(k):
        if char_list[i] in sequence:
            pass
        else:
            new_sequence = sequence + char_list[i]
            print_no_repetition_sequences_rec(char_list, new_sequence, k, n-1)


def parentheses(n, valid_option="", open_bracket=0):
    """ this function receives a number n, and return all legal permutations
    of parentheses"""
    if n == 0:
        if open_bracket == 0:
            return [valid_option]
        return parentheses(n, valid_option + ")", open_bracket - 1)

    if open_bracket == 0:
        return parentheses(n - 1, valid_option + "(", open_bracket + 1)

    return parentheses(n - 1, valid_option + "(", open_bracket + 1)\
           + parentheses(n, valid_option + ")", open_bracket - 1)


def up_and_right(n, k, combination=''):
    """ this function return every possible combination of 'r' and 'u', that
    will lead us to the given point (n,1) """
    if n < 0 or k < 0:
        return
    if n == 0:
        if k == 0:
            print(combination)
            return
        else:
            up_and_right(0, k-1, combination + 'u')
    elif k == 0:
        if n == 0:
            print(combination)
            return
        else:
            up_and_right(n-1, 0, combination + 'r')
    elif n != 0 and k != 0:
        up_and_right(n-1, k, combination + 'r'),\
         up_and_right(n, k-1, combination + 'u')


def flood_fill(image, start):
    """ this function receives a matrix (image) and a
    position in the matrix (start), and based on them change the matrix """
    if image == []:
        return
    if image[start[0]][start[1]] == '.':
        image[start[0]][start[1]] = '*'
    if image[start[0]-1][start[1]] == '.':
        flood_fill(image, (start[0] - 1, start[1]))
    if image[start[0]+1][start[1]] == '.':
        flood_fill(image, (start[0] + 1, start[1]))
    if image[start[0]][start[1]-1] == '.':
        flood_fill(image, (start[0], start[1] - 1))
    if image[start[0]][start[1]+1] == '.':
        flood_fill(image, (start[0], start[1] + 1))
    return
















