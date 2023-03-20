print("Example.")
for i in range(1, 21, 2):
    print(i, end=' ')
print()

print("For loop a.")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

print("For loop b.")
for i in range(0, 20):
    print(20 - i, end=' ')
print()

print("For loop c.")
stars_number = int(input("Number of stars: "))
for i in range(0, stars_number):
    print("*", end="")
print()

print("For loop d.")
for i in range(0, stars_number):
    for j in range(0, i+1):
        print("*", end="")
    print()
