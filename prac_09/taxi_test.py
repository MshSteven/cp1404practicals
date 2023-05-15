from prac_09.taxi import Taxi

NAME = "Prius 1"
FUEL = 100
# PRICE = 1.23

my_taxi = Taxi(NAME, FUEL)
my_taxi.drive(40)
print(my_taxi)
print(my_taxi.current_fare_distance)
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
print(my_taxi.current_fare_distance)