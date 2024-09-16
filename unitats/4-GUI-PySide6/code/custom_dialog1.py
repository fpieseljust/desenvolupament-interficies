from PySide6.QtWidgets import (
    QMainWindow, QApplication, QDialog, QDialogButtonBox, QVBoxLayout, QLabel,
    QPushButton
)


class DialogoPersonalizado(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Dialogo personalizado")

        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.caja_botones = QDialogButtonBox(botones)
        self.caja_botones.accepted.connect(self.accept)
        self.caja_botones.rejected.connect(self.reject)

        self.layout_dialogo = QVBoxLayout()
        self.layout_dialogo.addWidget(
            QLabel("Estás seguro de querer realizar esta acción?"))
        self.layout_dialogo.addWidget(self.caja_botones)
        self.setLayout(self.layout_dialogo)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicación con diálogo personalizado")

        boton = QPushButton("Haz clic para que el dialogo aparezca")
        boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(boton)

    def mostrar_dialogo(self):
        print("Clic recibido, se mostrará el dialogo.")
        ventana_dialogo = DialogoPersonalizado(self)
        ventana_dialogo.setWindowTitle("Ventana de dialogo personalizado")
        # 1 si s'executa accept
        # 0 si s'executa reject
        resultado = ventana_dialogo.exec()
        if resultado:
            print("Aceptada")
        else:
            print("Cancelada")


app = QApplication([])

ventana_principal = VentanaPrincipal()
ventana_principal.show()

app.exec()
