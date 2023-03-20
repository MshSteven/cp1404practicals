DISCOUNT = 0.1

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
price_of_item = 0
total_price = 0
for i in range(0, number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price = total_price + price_of_item
if total_price > 100:
    total_price = total_price * (1 - DISCOUNT)
print(f"Total price for 3 items is ${total_price:.2f}")
