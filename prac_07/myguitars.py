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

    def __lt__(self, other):
        """Sort guitar object by year."""
        return self.year < other.year


guitars = []
in_file = open('guitars.csv', 'r')
for line in in_file:
    parts = line.strip().split(',')
    guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
    guitars.append(guitar)
in_file.close()

guitars.sort()
print("There is my guitars:")
for i, guitar in enumerate(guitars, 1):
    # do something with i (the index) and guitar (the element)
    print(f"Guitar {i}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:10,.2f}")

print("Please add new guitars(Stop when the name get an blank enter):")
out_file = open('guitars.csv', 'w')
name = input("Name: ")
year = input("Year: ")
cost = input("Cost: $")
while name != "":
    guitar = Guitar(name, int(year), float(cost))
    guitars.append(guitar)
    name = input("Name: ")
    year = input("Year: ")
    cost = input("Cost: $")
for guitar in guitars:
    print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
out_file.close()
