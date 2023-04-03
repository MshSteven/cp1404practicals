"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    total_incomes = []
    total = 0
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
        total += income
        total_incomes.append(total)

    print_report(incomes, total_incomes)


def print_report(incomes, total_incomes):
    """Display the incomes details."""
    print("\nIncome Report\n-------------")
    for month in range(1, len(incomes) + 1):
        print(f"Month {month:2} - Income: ${incomes[month - 1]:10.2f} Total: ${total_incomes[month - 1]:10.2f}")


main()
