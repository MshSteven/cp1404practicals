# def create_dictionary(food, calories):
#     food_to_calories = {}
#     for i in range(len(food)):
#         food_to_calories[food[i]] = calories[i]
#     food_to_calories = sorted(food_to_calories.items(), key=lambda x: x[1], reverse=True)
#     food_to_calories = dict(food_to_calories)
#     return food_to_calories
#
#
# calories = [75, 65, 6175]
# food = ["Egg", "Apple", "Carrot Cake"]
# print(create_dictionary(food, calories))


# def do_thing(i):
#     return "**" * i
#
#
# def main():
#     for i in range(5):
#         print(do_thing(i))
#
#
# main()

# from prac_06.car import Car
#
#
# test_car = Car()
# assert test_car._odometer == 0
# print("Work")
