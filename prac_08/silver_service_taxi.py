"""
CP1404/CP5632 Practical
Silver Service Taxi Class
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes a fanciness attribute."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=0):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return "{}, {}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(super().__str__(),
                                                                                          self.fuel,
                                                                                          self.current_fare_distance,
                                                                                          self.price_per_km,
                                                                                          self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip plus flagfall."""
        return self.flagfall + self.price_per_km * self.current_fare_distance
