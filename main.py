from threading import activeCount

from store import Store
from products import Product

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)

def start(store: Store):
    """
       Starts the interactive store menu.

       Allows the user to:
       1. List all active products in the store
       2. Show total quantity of all products
       3. Make an order by selecting quantities for products
       4. Quit the menu
       """
    while True:
        print("\n--- Store Menu ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        user_choice = input("Please enter a number (1-4): ")

        if user_choice == "1":
            print("\nAll products in store:")
            for product in store.get_all_products():
                product.show()

        elif user_choice == "2":
            total = store.get_total_quantity()
            print(f"\nTotal quantity oin store: {total}")


        elif user_choice == "3":
            print("\nMaking an order: ")

            active_products = store.get_all_products()

            print("Available products:")
            for idx, product in enumerate(active_products, start=1):
                print(f"{idx}. {product.name} (Price: {product.price}, Quantity: {product.get_quantity()})")

            shopping_list = []

            while True:
                try:
                    prod_choice = int(input(f"Select a product by number (1-{len(active_products)}), or 0 to finish: "))
                    if prod_choice == 0:
                        break

                    if not 1 <= prod_choice <= len(active_products):
                        raise ValueError("Invalid product number")

                    product = active_products[prod_choice - 1]

                    while True:
                        try:
                            quant = int(input(f"Enter quantity to buy for {product.name}: "))
                            if quant < 0:
                                raise ValueError("Quantity cannot be negative")
                            shopping_list.append((product, quant))
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}. Please enter a valid number.")

                except ValueError as e:
                    print(f"Invalid input: {e}. Please try again.")

            if shopping_list:
                total_price = store.order(shopping_list)
                print("********")
                print(f"Order made! Total payment: {total_price}")
            else:
                print("No products were ordered.")

        elif user_choice == "4":
            print("Bye!")
            break


if __name__ == "__main__":
    start(best_buy)
