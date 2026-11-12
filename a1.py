def calculate_change(paid,price):
    change = paid - price
    return change

snack_price = 25
print("vending machine")
print(f"this is the price of the snack: {snack_price} units")
print("accecpted coins: 1, 5, 10,25\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("iinsert a coin(1, 5, 10, 25): "))

    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("invalid coin, please insert a valid coin")
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"inserted (coin). total so far: {total_inserted}\n")

    if total_inserted >= snack_price:
        print("enough money inserted, processing your snack...")
        break

change_due = calculate_change(total_inserted, snack_price)
print("dispensing snack...")
if change_due == 0:
    pass
else:
    print(f"dispensing change: {change_due} units")


print("\n ==========purchase summary===========")
print("snack price: ", snack_price)
print("coins inserted: ", coins_inserted)
print("total paid: ", total_inserted)
print("change given: ", change_due)
print("thank you for your purchase!")
