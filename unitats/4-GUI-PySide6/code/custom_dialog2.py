from PySide6.QtWidgets import (
    QMainWindow, QApplication, QDialog, QDialogButtonBox, QVBoxLayout, QLabel,
    QPushButton
)

from PySide6.QtCore import QTranslator, QLibraryInfo


class DialogoPersonalizado(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Dialeg personalitzat")

        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.caja_botones = QDialogButtonBox(botones)
        self.caja_botones.accepted.connect(self.accept)
        self.caja_botones.rejected.connect(self.reject)

        self.layout_dialogo = QVBoxLayout()
        self.layout_dialogo.addWidget(
            QLabel("Estàs segur de realitzar esta acció??"))
        self.layout_dialogo.addWidget(self.caja_botones)
        self.setLayout(self.layout_dialogo)


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
        # 1 si s'executa accept
        # 0 si s'executa reject
        resultado = ventana_dialogo.exec()
        if resultado:
            print("Acceptada")
        else:
            print("Cancelada")

    def load_translator(self, app):
        translator = QTranslator(app)
        translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
        translator.load("qt_ca", translations)
        app.installTranslator(translator)


app = QApplication([])

ventana_principal = VentanaPrincipal()
ventana_principal.load_translator(app)
ventana_principal.show()

app.exec()
