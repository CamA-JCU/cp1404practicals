"""CP1404/CP5632 Practical - Test code to use the Guitar class."""

from prac_06.guitar import Guitar


def main():
    """Test code to use the Guitar class."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013)
    print("{} get_age() - Expected 99. Got {}".format(gibson.name, gibson.get_age()))
    print("{} get_age() - Expected 8. Got {}".format(another_guitar.name, another_guitar.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage()))
    print("{} is_vintage() - Expected Flase. Got {}".format(another_guitar.name, another_guitar.is_vintage()))


if __name__ == '__main__':
    main()
