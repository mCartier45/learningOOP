class Item:
    discount = 0.8  # Pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to received arguments
        assert price >= 0, f"Price={price} is not >= than 0"
        assert quantity >= 0, f"Quantity={quantity} is not >= than 0"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.discount

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)




"""
item1 = Item("Phone", 100, 5)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.discount = 0.7
item2.apply_discount()
print(item2.price)

print(Item.__dict__)  # All attributes at class level
print(item1.__dict__)  # All attributes at instance level
"""
