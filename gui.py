from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit,
    QHBoxLayout, QMessageBox, QApplication, QDialog
)
from logic import ShoppingCart

class StoreGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.cart = ShoppingCart()
        self.setWindowTitle("STORE GUI")
        self.setFixedSize(400, 300)
        self.layout = QVBoxLayout()
        self.item_prices = {
            "Steak": "$13.99",
            "Soda": "$4.99",
            "Fruit": "$3.99",
            "Bread": "$2.99",
            "Water": "$3.50"
        }
        self.amount_fields = {}
        self.init_ui()
        self.setLayout(self.layout)

    def init_ui(self):
        header = QLabel("<h1>VERY BASIC STORE</h1>")
        self.layout.addWidget(header)

        for item, price in self.item_prices.items():
            row = QHBoxLayout()
            row.addWidget(QLabel(f"{item:<8} {price:>6}"))
            amount_input = QLineEdit()
            amount_input.setFixedWidth(40)
            self.amount_fields[item] = amount_input
            row.addWidget(amount_input)

            btn = QPushButton("Add to cart")
            btn.clicked.connect(lambda _, name=item: self.add_to_cart(name)) #AI used here
            row.addWidget(btn)
            self.layout.addLayout(row)

        control_row = QHBoxLayout()
        view_cart_btn = QPushButton("View Cart")
        view_cart_btn.clicked.connect(self.view_cart)

        checkout_btn = QPushButton("Checkout")
        checkout_btn.clicked.connect(self.checkout)

        control_row.addWidget(view_cart_btn)
        control_row.addWidget(checkout_btn)
        self.layout.addLayout(control_row)

    def add_to_cart(self, item):
        input_field = self.amount_fields[item]
        try:
            amount = int(input_field.text())
            self.cart.add_item(item, amount)
            input_field.setText("")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid integer.")

    def view_cart(self):
        cart_data = self.cart.get_cart()
        cart_text = "\n".join([f"{key}: {value}" for key, value in cart_data.items()])
        dlg = QDialog(self)
        dlg.setWindowTitle("Cart")
        dlg.setFixedSize(100, 100)
        layout = QVBoxLayout()
        layout.addWidget(QLabel(cart_text))
        dlg.setLayout(layout)
        dlg.exec() #AI used here to make sure that users dont go back to main screen without closing out

    def checkout(self):
        #calculate total
        cart_data = self.cart.get_cart()
        prices = {
            "Steak" : 13.99,
            "Soda" : 4.99,
            "Fruit" : 3.99,
            "Bread" : 2.99,
            "Water" : 3.50
        }

        total = sum(cart_data[item] * prices[item] for item in cart_data)

        #display checkout screen
        dlg = QDialog(self)
        dlg.setWindowTitle("Checkout")
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Checkout complete. Total is: {total:.2f}\nHave a great day!"))
        dlg.setLayout(layout)
        dlg.exec() #AI used here to make sure that users dont go back to main screen without closing out

        #clears the cart
        self.cart.clear_cart()
