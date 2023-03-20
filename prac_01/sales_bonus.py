"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_LOW = 0.1
BONUS_HIGH = 0.15

sales = float(input("Enter sales: $"))
bonus = 0
while sales >= 0:
    if sales < 1000:
        bonus = sales * BONUS_LOW
    else:
        bonus = sales * BONUS_HIGH
    print(f"Your bonus based on sales is ${bonus}.")
    sales = float(input("Enter sales: $"))
