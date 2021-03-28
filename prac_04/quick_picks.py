"""
CP1404 - prac_04 - quick_picks.py
Cameron Attard
"""

import random

LOWEST_NUMBER = 1
HIGHEST_NUMBER = 45
NUMBER_OF_RANDOM_NUMBERS = 6


def main():
    """Quick Pick Lottery Ticket Generator"""
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        for j in range(NUMBER_OF_RANDOM_NUMBERS):
            print("{:2}".format(random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)), end=" ")
        print("")


main()
