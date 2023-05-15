from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that has an fanciness price_per_km and extra flag fall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a price_per_km, based on parent class Taxi and pass-in variable fanciness."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with flag fall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:,.2f}"

    def get_fare(self):
        """Get fare similar with Taxi but with extra flag fall."""
        return super().get_fare() + self.flagfall
