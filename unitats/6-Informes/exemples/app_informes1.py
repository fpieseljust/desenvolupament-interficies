import os

from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings


class VentanaInformes(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout_vertical = QVBoxLayout()
        self.setLayout(self.layout_vertical)

        ruta_base = os.path.dirname(__file__)
        ruta_absoluta = os.path.join(ruta_base, "informe1.html")

        boton_abrir = QPushButton('Abrir informe')
        boton_abrir.clicked.connect(lambda ruta: self.abrir_informe(ruta=ruta_absoluta))
        self.layout_vertical.addWidget(boton_abrir)

        view = QWebEngineView()
        view.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        view.load(QUrl.fromLocalFile(ruta_absoluta))
        self.layout_vertical.addWidget(view)
		
        self.resize(800,600)
        
    def abrir_informe(self, ruta):              
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta))
        

if __name__ == "__main__":
    app = QApplication([])
    ventana_informes = VentanaInformes()
    ventana_informes.show()
    app.exec()