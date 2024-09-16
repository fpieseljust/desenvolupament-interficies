from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class Finestra(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("finestra")
        self.etiqueta1 = QLabel("Hola món!", self)
        self.setCentralWidget(self.etiqueta1)

if __name__ == "__main__":
    app = QApplication([])
    finestra1 = Finestra()
    finestra1.show()
    app.exec()