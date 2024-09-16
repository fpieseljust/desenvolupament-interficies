
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout cuadrícula")

        layout_cuadrícula = QGridLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_cuadrícula)
        self.setCentralWidget(componente_principal)

        layout_cuadrícula.addWidget(QPushButton('0,0'), 0, 0)
        layout_cuadrícula.addWidget(QPushButton('0,1'), 0, 1)
        layout_cuadrícula.addWidget(QPushButton('0,2'), 0, 2)
        layout_cuadrícula.addWidget(QPushButton('0,3'), 0, 3)
        layout_cuadrícula.addWidget(QPushButton('1,0-3'), 1, 0, 1, 4)
        layout_cuadrícula.addWidget(QPushButton('2,0-1'), 2, 0, 1, 2)
        layout_cuadrícula.addWidget(QPushButton('2,2-3'), 2, 2, 1, 2)


app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()