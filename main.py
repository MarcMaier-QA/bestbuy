from store import Store
from products import Product

def main():
    # Create products
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    # Create store
    best_buy = Store(product_list)

    # Show all active products
    products = best_buy.get_all_products()
    print("Active products:", [p.name for p in products])

    # Total quantity of all products
    print("Total quantity in store:", best_buy.get_total_quantity())

    # Place an order
    total_cost = best_buy.order([(products[0], 1), (products[1], 2)])
    print(f"Order cost: {total_cost} dollars.")

if __name__ == "__main__":
    main()
