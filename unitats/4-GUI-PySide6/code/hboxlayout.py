from PySide6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton
    )


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout horitzontal")

        # Creem un layout vertical
        layout_horitzontal = QHBoxLayout()

        componente_principal = QWidget()
        componente_principal.setLayout(layout_horitzontal)
        self.setCentralWidget(componente_principal)

        layout_horitzontal.addWidget(QPushButton('Uno'))
        layout_horitzontal.addWidget(QPushButton('Dos'))
        layout_horitzontal.addWidget(QPushButton('Tres'))
        layout_horitzontal.addWidget(QPushButton('Cuatro'))


app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()