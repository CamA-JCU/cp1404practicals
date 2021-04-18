"""CP1404/CP5632 Practical - Guitar class."""

CURRENT_YEAR = 2021
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of Guitar object."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return the age of the Guitar object."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if the Guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE
