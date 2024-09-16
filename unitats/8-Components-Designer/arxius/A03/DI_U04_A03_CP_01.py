from PySide6.QtWidgets import QApplication, QVBoxLayout, QFormLayout, QWidget, QLineEdit, QPushButton, QLabel
from DI_U04_A02_CP_01 import EditorContraseña

class VentanaLogin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout_vertical = QVBoxLayout()
        self.setLayout(self.layout_vertical)

        layout_formulario = QFormLayout()
        self.usuario = QLineEdit()
        layout_formulario.addRow('Usuario:', self.usuario)
        self.contraseña = EditorContraseña()
        layout_formulario.addRow('Contraseña:', self.contraseña)
        self.layout_vertical.addLayout(layout_formulario)
        boton_aceptar = QPushButton('Aceptar')
        boton_aceptar.clicked.connect(self.comprobar_credenciales)
        self.layout_vertical.addWidget(boton_aceptar)
        self.label = QLabel()
        self.label_añadido = False

    def comprobar_credenciales(self):        
        if (self.usuario.text() == 'admin' and self.contraseña.text() == '1234'):
            self.label.setText('Credenciales correctas')
            self.label.setStyleSheet('color: green')            
        else:
            self.label.setText('Credenciales incorrectas')
            self.label.setStyleSheet('color: red')
        if (not self.label_añadido):
            self.label_añadido = True
            self.layout_vertical.addWidget(self.label)
        

if __name__ == "__main__":
    app = QApplication([])
    ventana_login = VentanaLogin()
    ventana_login.show()
    app.exec()