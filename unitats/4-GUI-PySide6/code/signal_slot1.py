from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow, QLabel, QVBoxLayout

class FinestraPrincipal(QMainWindow):
    '''
    Classe FinestraPrincipal, hereta de QMainWindow.
    El QMainWindow és un component pensat per ser
    la finestra principal d'una aplicació.
    '''

    def __init__(self):
        super().__init__()
        self.setWindowTitle("finestra")
        self.layout1 = QVBoxLayout()
        self.widget = QWidget()
        self.widget.setLayout(self.layout1)

        
        self.boton1 = QPushButton("Borrar", self)
        self.etiqueta1 = QLabel('''<a href='http://stackoverflow.com'>stackoverflow</a>''')
        self.etiqueta1.setOpenExternalLinks(True)
        self.layout1.addWidget(self.boton1)
        self.layout1.addWidget(self.etiqueta1)
        # Configurem el botó com a element principal de la finestra.
        # Això és perquè estem usant un QMainWindow. No calia
        # passar-li el parent en la seua creació.
        self.setCentralWidget(self.widget)
        # Connectem l'esdeveniment clic del botó a la ranura clic_de_boton
        self.boton1.clicked.connect(self.etiqueta1.clear)
        self.etiqueta1.linkHovered.connect(lambda _:print("Link clicked!!"))

if __name__ == "__main__":
    app = QApplication([])
    finestra1 = FinestraPrincipal()
    finestra1.show()
    app.exec()