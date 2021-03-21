"""
CP1404 - password_check.py
Cameron Attard
"""

MIN_LENGTH = 8

def main():
    """Password Checker Program"""
    password = get_password()
    print_password(password)


def print_password(password):
    """Print password using asterisks"""
    print("*" * len(password))


def get_password():
    """Get Password from user"""
    password = str(input("Enter password that is {} in length: ".format(MIN_LENGTH)))
    while len(password) < MIN_LENGTH:
        print("Password does not meet minimum length requirements")
        password = str(input("Enter password that is {} in length: ".format(MIN_LENGTH)))
    return password


main()