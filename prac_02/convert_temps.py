def main():
    filename_01 = "temps_input.txt"
    in_file = open(filename_01, "r")
    filename_02 = "temps_output.txt"
    out_file = open(filename_02, "w")
    for line in in_file:
        temp_in_celsius = convert_fahrenheit_to_celsius(float(line))
        print(temp_in_celsius, file=out_file)
    in_file.close()
    out_file.close()


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
