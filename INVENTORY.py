store_products = []

print("...Welcome to the store...")

total_day = 0
continue_sale = "yes"
stop = "no"

# While to keep registering sales
while continue_sale == "yes":

    product = input("Product name: ")
    price = float(input("Product price: "))
    quantity = int(input("Quantity sold: "))

    total = price * quantity
    total_day += total

    store_products.append((product, price, quantity))

    print("Sale registered.\nSale total: $", total)

    continue_sale = input("Do you want to register another sale? (yes/no): ").lower()


# While when the user chooses o
while continue_sale == "no":

    print("\nDay summary:")

    for product, price, quantity in store_products:
        print(f"Product: {product} | Price: {price} | Quantity: {quantity}")

    print(f"Total collected during the day: ${total_day:.2f}")
    break
