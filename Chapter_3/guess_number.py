import random

number = random.randint(0, 100)


def guess_loop():
    my_number = -1

    while my_number != number:
        try:
            my_number = int(input())
        except ValueError:
            print('input should be an integer, please enter an integer:')
            continue
        if my_number == number:
            print('you guessed right! the number is ' + str(number))
            break
        if my_number > number:  # check if its higher
            print('try lower!')
        else:  # must be higher...
            print('try higher!')


print('a random number between 0-100 has been generated, whats your initial guess?')
guess_loop()
