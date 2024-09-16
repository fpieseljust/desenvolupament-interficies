from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
    )


class OtraVentana(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("La otra ventana")


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.otra_ventana = None  # Referència nula
        self.setWindowTitle("Aplicación con dos ventanas")
        self.boton = QPushButton("Mostrar/ocultar otra ventana")
        self.boton.clicked.connect(self.mostrar_otra_ventana)
        self.setCentralWidget(self.boton)

    def mostrar_otra_ventana(self):
        if self.otra_ventana is None:
            self.otra_ventana = OtraVentana()
            self.otra_ventana.move(self.pos())
            self.otra_ventana.show()
        else:
            if self.otra_ventana.isHidden():
                self.otra_ventana.move(self.pos())
                self.otra_ventana.show()
            else:
                self.otra_ventana.hide()


app = QApplication([])
ventana_principal = VentanaPrincipal()
ventana_principal.show()
app.exec()
