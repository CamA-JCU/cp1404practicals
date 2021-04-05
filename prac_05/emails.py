"""
CP1404/CP5632 Practical

"""


def main():
    emails_dict = {}
    email = str(input("Email: "))
    # email = "cameron.attard@my.jcu.edu.au"
    while email != "":
        name = determine_name_from_email(email)
        name_correct = input("Is your name {}? (Y/n) ".format(name))
        if name_correct.upper() != "Y" and name_correct != "":
            name = input("Name: ")
        emails_dict[name] = email
        email = str(input("Email: "))
    print()
    for name, email in emails_dict.items():
        print("{} ({})".format(name, email))


def determine_name_from_email(email):
    """Determines the person's name from their email."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
