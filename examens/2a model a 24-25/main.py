from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QHeaderView
from database import Database
import sys
import os

class UserApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestió d'Usuaris")
        self.setGeometry(100, 100, 600, 500)
        self.db = Database(db_name=os.path.join(os.path.dirname(__file__), 'users.db'))

        # Widget principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.layout = QVBoxLayout()
        main_widget.setLayout(self.layout)

        # Formulari (afegit directament a la finestra)
        self.name_input = QLineEdit()
        self.password_input = QLineEdit() 
        self.role_input = QLineEdit() 

        self.layout.addWidget(QLabel("Nom:"))
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(QLabel("Contrasenya:"))  
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(QLabel("Rol (Admin, Usuari, Convidat):")) 
        self.layout.addWidget(self.role_input)

        # Botons per afegir i modificar
        self.add_button = QPushButton("Afegir Usuari")
        self.add_button.clicked.connect(self.add_user)
        self.layout.addWidget(self.add_button)

        self.edit_button = QPushButton("Modificar Usuari")
        self.edit_button.clicked.connect(self.edit_user)
        self.layout.addWidget(self.edit_button)

        # Taula d'usuaris
        self.table = self.create_table()
        self.layout.addWidget(self.table)

        self.load_users()

    def create_table(self):
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Nom", "Contrasenya", "Rol"])  
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  
        table.setSelectionBehavior(QTableWidget.SelectRows)  
        return table

    def load_users(self):
        self.table.setRowCount(0)
        users = self.db.get_users()
        for row_index, (user_id, name, password, role) in enumerate(users):
            self.table.insertRow(row_index)
            self.table.setItem(row_index, 0, QTableWidgetItem(name))
            self.table.setItem(row_index, 1, QTableWidgetItem(password))  
            self.table.setItem(row_index, 2, QTableWidgetItem(role))

    def add_user(self):
        name = self.name_input.text()
        password = self.password_input.text() 
        role = self.role_input.text()  

        if name and password and role:
            self.db.add_user(name, password, role)
            self.load_users()

    def edit_user(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            return

        user_id = self.db.get_users()[selected_row][0]
        new_name = self.name_input.text()
        new_password = self.password_input.text()  
        new_role = self.role_input.text()

        if new_name and new_password and new_role:
            self.db.update_user(user_id, new_name, new_password, new_role)
            self.load_users()

    def delete_user(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            return

        user_id = self.db.get_users()[selected_row][0]
        self.db.delete_user(user_id)
        self.load_users()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserApp()
    window.show()
    sys.exit(app.exec())