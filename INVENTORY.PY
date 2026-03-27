store_products = []

print("...Welcome to the store...")

total_day = 0
continue_sale = "yes"

# Loop to register sales
while continue_sale == "yes":

    # Validate product name: cannot be empty or contain numbers
    product = input("Product name: ").strip()
    while product == "" or any(char.isdigit() for char in product):
        print("Error: Product name cannot be empty or contain numbers.")
        product = input("Product name: ").strip()

    # Validate price
    try:
        price = float(input("Product price: "))
        while price < 0:
            print("Error: Price cannot be negative.")
            price = float(input("Product price: "))
    except ValueError:
        print("Invalid price. Sale canceled.\n")
        continue

    # Validate quantity
    try:
        quantity = int(input("Quantity sold: "))
        while quantity <= 0:
            print("Error: Quantity must be greater than 0.")
            quantity = int(input("Quantity sold: "))
    except ValueError:
        print("Invalid quantity. Sale canceled.\n")
        continue

    # Calculate total for the sale
    total = price * quantity
    total_day += total

    # Store the sale in the list
    store_products.append((product, price, quantity))

    print(f"Sale registered.\nSale total: ${total:.2f}")

    # Validate yes/no answer to continue sales
    continue_sale = input("Do you want to register another sale? (yes/no): ").lower()
    while continue_sale != "yes" and continue_sale != "no":
        print("Error: Please enter 'yes' or 'no'.")
        continue_sale = input("Do you want to register another sale? (yes/no): ").lower()

# Print the day summary
print("\nDay summary:")

for product, price, quantity in store_products:
    print(f"Product: {product} | Price: {price} | Quantity: {quantity}")

print(f"Total collected during the day: ${total_day:.2f}")
