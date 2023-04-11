"""
Word Occurrences
Estimate: 20 minutes
Actual:   26 minutes
"""


def main():
    email = input("Email: ")
    email_to_name = {}
    while email != "":
        name = extract_name(email)
        name_check = input(f"Is your name {name}? (Y/n)").upper()
        if name_check != "Y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    name = email.split("@")
    name = name[0].split(".")
    label = " "
    name = label.join(name)
    return name


main()
