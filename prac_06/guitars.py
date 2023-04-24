from prac_06.guitar import Guitar


guitars = []
# guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("My guitars!")
name = input("Name: ")
year = int(input("Year: "))
cost = float(input("Cost: $"))
while name != "":
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost} added.")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))

guitars.sort()
print("There is my guitars:")
for i, guitar in enumerate(guitars, 1):
    # do something with i (the index) and guitar (the element)
    vintage_string = guitar.is_vintage()
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
