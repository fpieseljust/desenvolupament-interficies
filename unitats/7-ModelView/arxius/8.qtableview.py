import sys
import os

from PySide6.QtCore import Qt, QTimer
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableView,
    QVBoxLayout,
    QPushButton,
    QWidget
)


class Contacts(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(415, 200)
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        # Set up the model
        self.model = QSqlTableModel(self)
        self.model.setTable("contacts")
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnRowChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Job")
        self.model.setHeaderData(3, Qt.Horizontal, "Email")
        self.model.select()
        # Set up the view
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.resizeColumnsToContents()

        layout.addWidget(self.view)
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_update)
        self.timer.start(500)
        

        self.update = QPushButton("Update")
        self.update.clicked.connect(self.on_update)
        layout.addWidget(self.update)
        self.setCentralWidget(widget)

    def on_update(self):
        if not self.view.isPersistentEditorOpen(self.view.currentIndex()):
            self.model.select()
            self.view.resizeColumnsToContents()



def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName(os.path.join(os.path.dirname(__file__),
                 "contacts.sqlite"))
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True


app = QApplication(sys.argv)
if not createConnection():
    sys.exit(1)
win = Contacts()
win.show()
sys.exit(app.exec_())