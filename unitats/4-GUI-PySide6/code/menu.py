from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction, QKeySequence


# Nuestra ventana principal hereda de QMainWindow
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal con menú")
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        
        accion = QAction("&Imprimir por consola", self)
        accion.setShortcut(QKeySequence("Ctrl+p"))
        accion.triggered.connect(self.imprimir_por_consola)

        menu.addAction(accion)

    def imprimir_por_consola(self):
        print("Acción lanzada a través del menú o del atajo")


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()
