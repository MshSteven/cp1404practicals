# Block 1
user_name = input("Enter your name: ")
filename = "name.txt"
out_file = open(filename, "w")
print(user_name, file=out_file)
out_file.close()

# Block 2
in_file = open(filename, "r")
user_name = in_file.readline()
print(f"Your name is {user_name}")
in_file.close()

# Block 3
filename = "numbers.txt"
in_file = open(filename, "r")
numbers = in_file.readlines()
sum_number = int(numbers[0]) + int(numbers[1])
print(sum_number)
in_file.close()

# Block 4
filename = "numbers.txt"
in_file = open(filename, "r")
total_number = 0
for line in in_file.readlines():
    total_number = total_number + int(line)
print(total_number)
in_file.close()

