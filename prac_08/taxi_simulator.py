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
    while menu_choice != "Q":       # Quit
        if menu_choice == "D":      # Drive
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                taxi = taxis[current_taxi]
                trip_fare = take_taxi_trip(taxi)
                bill_to_date += trip_fare
            print("Bill to date: ${:.2f}".format(bill_to_date))
        elif menu_choice == "C":    # Choose Taxi
            current_taxi = choose_valid_taxi(taxis)
            print("Bill to date: ${:.2f}".format(bill_to_date))
        else:
            print("Invalid Option")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("Total trip cost: ${:.2f}".format(bill_to_date))
    print("Taxis are now:")
    print_available_taxis(taxis)


def take_taxi_trip(taxi):
    """Take taxi trip and return trip fare"""
    distance = float(input("Drive how far? "))
    taxi.start_fare()
    taxi.drive(distance)
    trip_fare = taxi.get_fare()
    print("Your {} trip cost you ${:.2f}".format(taxi.name, trip_fare))
    return trip_fare


def choose_valid_taxi(taxis):
    """Choose a valid taxi from Taxis"""
    print("Taxis available:")
    print_available_taxis(taxis)
    selected_taxi = int(input("Choose taxi: "))
    if selected_taxi >= len(taxis) or selected_taxi < 0:
        print("Invalid taxi choice")
        selected_taxi = None
    return selected_taxi


def print_available_taxis(taxis):
    """Print a list of available taxis"""
    for i, taxi in enumerate(taxis):
        print("{} - ".format(i), taxi)


if __name__ == '__main__':
    main()
