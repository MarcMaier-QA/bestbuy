class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise  ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active: bool = True


    def get_quantity(self) -> int:
        """Returns the current quantity of the product"""
        return self.quantity


    def set_quantity(self, quantity: int):
        """
        Sets the quantity of the product.
        Deactivates the product if quantity is 0.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
            self.quantity = quantity
            if self.quantity == 0:
                self.active = False


    def is_active(self) -> bool:
        """Returns True if the product is active, False otherwise."""
        return self.active


    def activate(self):
        """Activates the product."""
        self.active = True


    def deactivate(self):
        """Deactivates the product."""
        self.active = False


    def show(self):
        """Prints the prodict information to the console."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity) -> float:
        """
        Buys given quantity of the product.
        Returns the total price
        Raises exceptions if product is inactive, quantity <= 0, or not enough stock.
        """
        if not self.active:
            raise Exception("Produkt ist nicht aktiv")
        if quantity <= 0:
            raise ValueError("Menge muss größer als 0 sein")
        if quantity > self.quantity:
            raise ValueError("Nicht genug Produkte im Lager")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return total_price





bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()