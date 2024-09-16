from PySide6.QtWidgets import (
    QMainWindow, QApplication, QDialog, QDialogButtonBox, QVBoxLayout, QLabel,
    QPushButton, QHBoxLayout
)


class DialogoPersonalizado(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Dialeg personalitzat")

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.button_clicked)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.button_clicked)

        buttons = QHBoxLayout()
        buttons.addWidget(self.ok_button)
        buttons.addWidget(self.cancel_button)

        self.dialog_layout = QVBoxLayout()
        self.dialog_layout.addWidget(
            QLabel("Estàs segur de realitzar esta acció??"))
        self.dialog_layout.addLayout(buttons)
        self.setLayout(self.dialog_layout)
        self.result = False

    def button_clicked(self):
        sender = self.sender()
        if sender == self.ok_button:
            print("Accept")
            self.result = True
        else:
            print("Cancel")

        self.hide()


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicació amb dialeg personalitzat")

        boton = QPushButton("Fes clic per a que aparega el dialeg")
        boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(boton)

    def mostrar_dialogo(self):
        print("Clic rebut, es mostrarà eln dialeg.")
        ventana_dialogo = DialogoPersonalizado(self)
        ventana_dialogo.setWindowTitle("Finestra de dialeg personalitzat")
        ventana_dialogo.exec()
        print(ventana_dialogo.result)
        

app = QApplication([])

ventana_principal = VentanaPrincipal()
ventana_principal.show()

app.exec()
