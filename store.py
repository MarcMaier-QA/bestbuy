from products import Product

class Store:
    """
    Represents a store containing multiple products.
    Provides methods to add, remove, and purchase products.
    """

    def __init__(self, products: list[Product] = None):
        """
        Initializes the store with a list of products.
        If no products are provided, starts with an empty list.
        """
        if products is None:
            self.products = []
        else:
            self.products = products


    def add_product(self, product: Product):
        """Adds a product to the store's product list."""
        self.products.append(product)


    def remove_product(self, product: Product):
        """Removes a product from the store's product list if it exists."""
        if product in self.products:
            self.products.remove(product)


    def get_total_quantity(self) -> int:
        """Return the total quantity of all products in the store."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total


    def get_all_products(self) -> list[Product]:
        """Returns a list of all active products in the store."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
        Purchases a list of products with specified quantities.

        Parameters:
            shopping_list (List[Tuple[Product, int]]):
            A list of tuples where each tuple contains a Product and the quantity to buy.

        Retruns:
            float: The total price of the order.

        Raises:
            Exception or ValueError if any product is inactive, quantity <= 0,
            or not enough stock.
        """
        total_prize = 0.0

        for product, quantity in shopping_list:
            total_prize += product.buy(quantity)
        return total_prize
