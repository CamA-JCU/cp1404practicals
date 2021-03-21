"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """Score Status Program"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    result = determine_result(random.randint(0,101))
    print(result)


def determine_result(score):
    """Determine result from score"""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()