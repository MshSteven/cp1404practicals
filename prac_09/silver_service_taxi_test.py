from prac_09.silver_service_taxi import SilverServiceTaxi

NAME = "Hummer"
FUEL = 200
FANCINESS_1 = 4
FANCINESS_2 = 2

test_taxi = SilverServiceTaxi(NAME, FUEL, FANCINESS_1)
print(test_taxi)
print()

print(f"For an 18 km trip in a SilverServiceTaxi with fanciness of 2, the fare should be $48.78 (yikes!)")
test_taxi = SilverServiceTaxi(NAME, FUEL, FANCINESS_2)
test_taxi.drive(18)
print(test_taxi)
print(f"{test_taxi.get_fare():,.2f}")
