TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def estimator_first_version():
    print("Electricity bill estimator")
    cents_per_kwh = float(input("Enter cents per kWh: "))
    daily_use_in_kwh = float(input("Enter daily use in kWh: "))
    numbers_of_days = float(input("Enter number of billing days: "))
    estimated_bill = cents_per_kwh * 0.01 * daily_use_in_kwh * numbers_of_days
    print(f"Estimated bill: ${estimated_bill:.2f}")


def estimator_second_version():
    print("Electricity bill estimator 2.0")
    tariff = int(input("Which tariff? 11 or 31: "))
    daily_use_in_kwh = float(input("Enter daily use in kWh: "))
    numbers_of_days = float(input("Enter number of billing days: "))
    estimated_bill = 0
    if tariff == 11:
        estimated_bill = TARIFF_11 * daily_use_in_kwh * numbers_of_days
    elif tariff == 31:
        estimated_bill = TARIFF_31 * daily_use_in_kwh * numbers_of_days
    print(f"Estimated bill: ${estimated_bill:.2f}")


def main():
    # estimator_first_version()
    estimator_second_version()


main()
