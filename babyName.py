from string import *
from random import choice

first = input("Enter first letter: ")
second = input("Enter second letter: ")
third = input("Enter third letter: ")
fourth = input("Enter fouorth letter: ")
fifth = input("Input fifth letter: ")
sixth = input("Input sixth letter: ")


def name():
    if (first == 'c' or first == 'C'):
        one = choice('BCDFGHJKLMNPQRSTVWXZ')
    elif (first == 'v' or first == 'V'):
        one = choice('aeiou')
    else:
        one = first

    if (second == 'c' or second == 'C'):
        two = choice('BCDFGHJKLMNPQRSTVWXZ')
    elif (second == 'v' or second == 'V'):
        two = choice('aeiou')
    else:
        two = second

    if (third == 'c' or third == 'C'):
        three = choice('BCDFGHJKLMNPQRSTVWXZ')
    elif (third == 'v' or third == 'V'):
        three = choice('aeiou')
    else:
        three = third

    if (fourth == 'c' or fourth == 'C'):
        four = choice('BCDFGHJKLMNPQRSTVWXZ')
    elif (fourth == 'v' or fourth == 'V'):
        four = choice('aeiou')
    else:
        four = fourth

    if (fifth == 'c' or fifth == 'C'):
        five = choice('BCDFGHJKLMNPQRSTVWXZ')
    elif (fifth == 'v' or fifth == 'V'):
        five = choice('aeiou')
    else:
        five = fifth

    if (sixth == 'c' or sixth == 'C'):
        six = choice('BCDFGHJKLMNPQRSTVWXZ')
    elif (sixth == 'v' or sixth == 'V'):
        six = choice('aeiou')
    else:
        six = sixth

    babyName = one + two + three + four + five + six
    return babyName

for babynames in range(20):
   print(name())
