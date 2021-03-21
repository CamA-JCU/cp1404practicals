"""
CP1404 - password_check.py
Cameron Attard
"""

MIN_LENGTH = 8

password = str(input("Enter password that is {} in length: ".format(MIN_LENGTH)))
while len(password) < MIN_LENGTH:
    print("Password does not meet minimum length requirements")
    password = str(input("Enter password that is {} in length: ".format(MIN_LENGTH)))

print("*" * len(password))