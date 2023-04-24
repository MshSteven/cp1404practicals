"""
estimate time: 30 minutes
actual time: 40 minutes
"""
CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:
    """Represent a guitar object."""
    def __init__(self, name="", year=0, cost=0):
        """
        name: guitar's name
        year: guitar's built year
        cost: guitar's price
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """format string of display guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get age of a guitar."""
        return CURRENT_YEAR - self.year

    # def is_vintage(self):
    #     return self.get_age() >= VINTAGE_AGE

    def is_vintage(self):
        """Determine is the guitar vintage."""
        if self.get_age() >= VINTAGE_AGE:
            return " (vintage)"
        else:
            return ""

    def __lt__(self, other):
        """Sort guitar object by year."""
        return self.year < other.year
