import sys
import os

from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QApplication, QMessageBox, QLabel

connection = QSqlDatabase.addDatabase("QSQLITE")
connection.setDatabaseName(
    os.path.join(os.path.dirname(__file__),
                 "contacts.sqlite")
)
# connection.setDatabaseName("/contacts.sqlite")
application = QApplication(sys.argv)

if not connection.open():
    QMessageBox.critical(
        None,
        "Error connectant a la base de dades!",
        f"Database Error: {connection.lastError().databaseText()}"
    )
    sys.exit(1)

window = QLabel("Connectat a la base de dades!")
window.setWindowTitle("Database open")
window.resize(200, 100)
window.show()
sys.exit(application.exec_())
