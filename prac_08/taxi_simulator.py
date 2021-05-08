"""
CP1404/CP5632 Prac_08 Taxi Simulator Program
Cameron Attard
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi Simulator."""
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":  # Quit
        if menu_choice == "D":  # Drive
            print("Drive")
        elif menu_choice == "C":  # Choose Taxi
            print("Choose Taxi")
        else:
            print("Invalid Option")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("Quit")


if __name__ == '__main__':
    main()
