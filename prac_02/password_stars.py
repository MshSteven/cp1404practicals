password = input("Enter your password(length large than 5) : ")
length = len(password)
while length <= 5:
    print("Invalid input")
    password = input("Enter your password(length large than 5) : ")
    length = len(password)
for i in range(length):
    print("*", end="")