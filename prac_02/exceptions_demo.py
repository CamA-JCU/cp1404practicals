"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? This will occur if the user enters a type that is not an integer
2. When will a ZeroDivisionError occur? If the user enters 0 for the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError? You can error check the input and ask for it again if it is 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be Zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")