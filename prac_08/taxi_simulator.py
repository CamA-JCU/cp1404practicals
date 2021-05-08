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
    bill_to_date = 0.00
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":  # Quit
        if menu_choice == "D":  # Drive
            print("Drive")
        elif menu_choice == "C":  # Choose Taxi
            # print("Choose Taxi")
            current_taxi = choose_valid_taxi(taxis)
            # print(current_taxi)
        else:
            print("Invalid Option")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("Quit")


def choose_valid_taxi(taxis):
    """Choose a valid taxi from Taxis"""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print("{} - ".format(i), taxi)
    selected_taxi = int(input("Choose taxi: "))
    if selected_taxi >= len(taxis) or selected_taxi < 0:
        print("Invalid taxi choice")
        selected_taxi = None
    return selected_taxi


if __name__ == '__main__':
    main()
