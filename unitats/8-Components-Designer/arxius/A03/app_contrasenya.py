from PySide6.QtWidgets import QApplication, QVBoxLayout, QFormLayout, QWidget, QLineEdit, QPushButton
from componente.contraseña import EditorContraseña

class VentanaLogin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout_vertical = QVBoxLayout()
        self.setLayout(layout_vertical)

        layout_formulario = QFormLayout()
        layout_formulario.addRow('Usuario:', QLineEdit())
        layout_formulario.addRow('Contraseña:', EditorContraseña())
        layout_vertical.addLayout(layout_formulario)
        layout_vertical.addWidget(QPushButton('Aceptar'))


if __name__ == "__main__":
    app = QApplication([])
    ventana_login = VentanaLogin()
    ventana_login.show()
    app.exec()