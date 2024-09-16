from PySide6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
    )


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout vertical")

        # Creem un layout vertical
        layout_vertical = QVBoxLayout()

        componente_principal = QWidget()
        componente_principal.setLayout(layout_vertical)
        self.setCentralWidget(componente_principal)

        layout_vertical.addWidget(QPushButton('Uno'))
        layout_vertical.addWidget(QPushButton('Dos'))
        layout_vertical.addWidget(QPushButton('Tres'))
        layout_vertical.addWidget(QPushButton('Cuatro'))


app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()