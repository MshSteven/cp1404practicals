"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""


def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


def main():
    name = input("Enter name: ")
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")
        display_menu()
        choice = input(">>> ").upper()
    print("Finished.")


main()

