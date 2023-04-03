import random

NUMBER_OF_RANDOM = 6
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 45


def get_valid_quick_picks():
    """Get quick picks with sorted and no repeat number."""
    quick_picks = []
    for i in range(NUMBER_OF_RANDOM):
        number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER + 1)
        while number in quick_picks:
            number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER + 1)
        quick_picks.append(number)
    quick_picks.sort()
    return quick_picks


def display_quick_picks(quick_picks):
    """Display quick picks"""
    for number in quick_picks:
        print(f"{number:2}", end=" ")
    print()


def main():
    """Get the number of quick picks line then create and display quick picks."""
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_picks = get_valid_quick_picks()
        display_quick_picks(quick_picks)


main()


