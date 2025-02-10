from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QHeaderView
from database import Database
import sys

class ProductApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestió de Productes")
        self.setGeometry(100, 100, 600, 500)
        self.db = Database()

        # Widget principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.layout = QVBoxLayout()
        main_widget.setLayout(self.layout)

        # Formulari (tot amb QLineEdit)
        self.name_input = QLineEdit()
        self.price_input = QLineEdit()  
        self.category_input = QLineEdit()  

        self.layout.addWidget(QLabel("Nom del Producte:"))
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(QLabel("Preu (€):"))
        self.layout.addWidget(self.price_input)
        self.layout.addWidget(QLabel("Categoria:"))
        self.layout.addWidget(self.category_input)

        # Botons per afegir i modificar
        self.add_button = QPushButton("Afegir Producte")
        self.add_button.clicked.connect(self.add_product)
        self.layout.addWidget(self.add_button)

        self.edit_button = QPushButton("Modificar Producte")
        self.edit_button.clicked.connect(self.edit_product)
        self.layout.addWidget(self.edit_button)

        # Taula de productes
        self.table = self.create_table()
        self.layout.addWidget(self.table)

        self.load_products()

    def create_table(self):
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Nom", "Preu", "Categoria"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setSelectionBehavior(QTableWidget.SelectRows)
        return table

    def load_products(self):
        self.table.setRowCount(0)
        products = self.db.get_products()
        for row_index, (product_id, name, price, category) in enumerate(products):
            self.table.insertRow(row_index)
            self.table.setItem(row_index, 0, QTableWidgetItem(name))
            self.table.setItem(row_index, 1, QTableWidgetItem(price))
            self.table.setItem(row_index, 2, QTableWidgetItem(category))

    def add_product(self):
        name = self.name_input.text()
        price = self.price_input.text()
        category = self.category_input.text()

        if name and price and category:
            self.db.add_product(name, price, category)
            self.load_products()

    def edit_product(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            return

        product_id = self.db.get_products()[selected_row][0]
        new_name = self.name_input.text()
        new_price = self.price_input.text()
        new_category = self.category_input.text()

        if new_name and new_price and new_category:
            self.db.update_product(product_id, new_name, new_price, new_category)
            self.load_products()

    def delete_product(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            return

        product_id = self.db.get_products()[selected_row][0]
        self.db.delete_product(product_id)
        self.load_products()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductApp()
    window.show()
    sys.exit(app.exec())
