"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    filename = "results.txt"
    out_file = open(filename, "w")
    number_of_scores = int(input("Enter the number of scores: "))
    for i in range(number_of_scores):
        score = random.randint(0, 100)
        result = get_result(score)
        print(f"{score} is {result}", file=out_file)
    out_file.close()


def get_result(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score < 50:
        result = "Bad"
    elif score < 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()
