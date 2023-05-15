class Band:
    def __init__(self, band_name=""):
        self.band_name = band_name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Musician."""
        return f"{self.band_name} ({', '.join(str(obj) for obj in self.musicians)})"

    def __repr__(self):
        """Return a string representation of a band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician object into musician lists."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musicians playing their first (or no) instrument."""
        message = ""
        for musician in self.musicians:
            message = message + musician.play() + "\n"
        return message
