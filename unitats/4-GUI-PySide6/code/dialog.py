from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicació amb dialegs")

        boton = QPushButton("Fes clic per a que aparega el dialeg")
        boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(boton)

    def mostrar_dialogo(self):
        print("Clic rebut, es mostrarà el dialeg.")
        ventana_dialogo = QDialog(self)
        # ventana_dialogo.setWindowTitle("Finestra de dialeg")
        ventana_dialogo.exec()


app = QApplication([])

ventana_principal = VentanaPrincipal()
ventana_principal.show()

app.exec()
