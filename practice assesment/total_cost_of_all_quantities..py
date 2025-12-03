class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_cost(self):
        return self.price * self.quantity

# Example usage
product = Product("Laptop", 1000, 3)
total_cost = product.calculate_total_cost()
print(f"Total cost for {product.quantity} {product.name}s is: ${total_cost}")