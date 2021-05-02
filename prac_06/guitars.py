"""CP1404/CP5632 Practical - Client code to use the Guitar class."""

from prac_06.guitar import Guitar


def main():
    """Client code to use the Guitar class."""
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        my_guitar = Guitar(name, year, cost)
        guitars.append(my_guitar)
        print("{} added.".format(my_guitar))
        print("")
        name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))


if __name__ == '__main__':
    main()
