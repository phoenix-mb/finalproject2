class ShoppingCart:
    def __init__(self):
        self.items = {
            "Steak": 0,
            "Soda": 0,
            "Fruit": 0,
            "Bread": 0,
            "Water": 0
        }

    def add_item(self, item: str, amount: int):
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.items[item] += amount

    def get_cart(self):
        return self.items.copy()

    def clear_cart(self):
        for key in self.items:
            self.items[key] = 0
