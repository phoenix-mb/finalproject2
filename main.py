import sys
from PyQt6.QtWidgets import *
from gui import StoreGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StoreGUI()
    window.show()
    sys.exit(app.exec())
