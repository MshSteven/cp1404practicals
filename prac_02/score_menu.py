def display_menu():
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def main():
    display_menu()
    choice = input(">>> ").upper()
    score = 0
    result = "Bad"
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_result(score)
            print(result)
        elif choice == "S":
            for i in range(score):
                print("*", end="")
            print()
        else:
            print("Invalid choice")
        display_menu()
        choice = input(">>> ").upper()
    print("farewell")


def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def get_result(score):
    if score < 50:
        result = "Bad"
    elif score < 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()
