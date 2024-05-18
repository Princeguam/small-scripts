import sys
import random as rd



correct_guess = rd.randint(1,10)

while True:
    try:
        user_guess = int(input('Enter your Guess from 0-10: '))
        if user_guess >0 and user_guess < 11:
            if user_guess == correct_guess:
                print(f'YAY! You guessed {correct_guess} correctly')
                break
            else:
                print('Wrong Answer, try again')
        else:
            print('HEY, BOZO! ENTER A NUMBER FROM 1-10')
    except ValueError as err:
        print(err)

