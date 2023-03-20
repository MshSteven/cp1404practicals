def main():
    """Get password and display the asterisks"""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Display the asterisks"""
    for i in range(len(password)):
        print("*", end="")


def get_password():
    """Get password"""
    password = input("Enter your password(length large than 5) : ")
    while len(password) <= 5:
        print("Invalid input")
        password = input("Enter your password(length large than 5) : ")
    return password


main()
