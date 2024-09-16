import os

from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtCore import Qt


# Nuestra ventana principal hereda de QMainWindow
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(
            "Ventana principal con menú i barra de herramientas")
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        ruta_a_icono = os.path.join(os.path.dirname(
            __file__), "images/console.svg")
        accion = QAction(QIcon(ruta_a_icono), "Imprimir por consola", self)
        accion.setWhatsThis(
            "Al pulsar sobre el botón se imprimirá un texto por consola")
        accion.setShortcut(QKeySequence("Ctrl+p"))
        accion.triggered.connect(self.imprimir_por_consola)
        menu.addAction(accion)

        barra_herramientas = QToolBar("Barra de herramientas 1")
        barra_herramientas.addAction(accion)
        self.addToolBar(barra_herramientas)

    def imprimir_por_consola(self):
        print("Acción lanzada a través del menú, del atajo" +
            " o de la barra de herramientas")


if __name__ == "__main__":
    app = QApplication([])
    app.setAttribute(Qt.AA_DontShowIconsInMenus)

    ventana1 = VentanaPrincipal()
    ventana1.show()

app.exec()