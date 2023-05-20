from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>> "


def main():
    """Run a system to get chosen taxi and display the fare of customer."""
    current_taxi = None
    bill_to_date = 0.00
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    options = ["q", "c", "d"]

    print("Let's drive!")
    option = input(MENU).lower()
    while option != options[0]:
        if option == options[1]:    # This option is to display the available taxi.
            display_available_taxi(taxis, "Taxis available:")
            choice = int(input("Choose taxi: "))
            if choice < 0 or choice >= len(taxis):
                print("Invalid taxi choice")
            else:
                current_taxi = choice

        elif option == options[2]:  # This option is to get the drive distance and show the fare.
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                taxis[current_taxi].start_fare()
                distance_driven = taxis[current_taxi].drive(distance)
                print(f"Your {taxis[current_taxi].name} trip cost you ${taxis[current_taxi].get_fare():,.2f}")
                bill_to_date += taxis[current_taxi].get_fare()

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:,.2f}")
        option = input(MENU).lower()
    print(f"Total trip cost: ${bill_to_date:,.2f}")
    display_available_taxi(taxis, "Taxis are now:")


def display_available_taxi(taxis, prompt):
    """Display the available taxi."""
    print(prompt)
    for i, available_taxi in enumerate(taxis):
        print(f"{i} - {available_taxi}")


main()
