import sys, os
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

def mainwindow_setup(w):
    w.setWindowTitle("Simple text editor")
    w.cerrar_boton.setText("Close")
    w.limpiar_boton.setText("Clear")

app = QtWidgets.QApplication(sys.argv)
ui_path = os.path.join(os.path.dirname(__file__), "formulari.ui")
window = loader.load(ui_path, None)
mainwindow_setup(window)
window.show()
app.exec_()