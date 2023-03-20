def display_menu():
    print("1. Show the even numbers from x to y")
    print("2. Show the odd numbers from x to y")
    print("3. Show the squares from x to y")
    print("4. Exit the program")


def determine_parity(number_x, number_y):
    parity_of_x = number_x % 2
    parity_of_y = number_y % 2
    return parity_of_x, parity_of_y


def main():
    number_x = int(input("Enter integer x: "))
    number_y = int(input("Enter integer y: "))
    display_menu()
    parity_of_x, parity_of_y = determine_parity(number_x, number_y)
    choice = int(input("Choose sequence: "))
    while choice != 4:
        if choice == 1:
            for i in range(number_x + parity_of_x, number_y - parity_of_y + 1, 2):
                print(i, end=" ")
            print()
        elif choice == 2:
            for i in range(number_x - parity_of_x + 1, number_y + parity_of_y, 2):
                print(i, end=" ")
            print()
        elif choice == 3:
            for i in range(number_x, number_y + 1):
                print(i * i, end=" ")
            print()
        else:
            print("Invalid choice")
        display_menu()
        choice = int(input("Choose sequence: "))
    print("Finished.")


main()
