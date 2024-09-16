from PySide6.QtCore import QLibraryInfo, QTranslator
from PySide6.QtWidgets import (
    QApplication, QMessageBox, QMainWindow, QPushButton
)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicación con mesaje crítico")

        boton = QPushButton("Haz clic para ver el mensaje crítico")
        boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(boton)

    def mostrar_dialogo(self):
        boton_pulsado = QMessageBox.critical(
            self,
            "Ejemplo de cuadro de mensaje crítico",
            "Ha habído algun problema al realizar la acción",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll |
                QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard
        )

        if boton_pulsado == QMessageBox.Discard:
            print("Descartado!")
        elif boton_pulsado == QMessageBox.NoToAll:
            print("No a todo!")
        else:
            print("Ignorado!")

def cargar_traductor(app):
    translator = QTranslator(app)
    translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    translator.load("qt_ca", translations)
    app.installTranslator(translator)


app = QApplication([])

# cargar_traductor(app)

ventana_principal = VentanaPrincipal()
ventana_principal.show()

app.exec()
