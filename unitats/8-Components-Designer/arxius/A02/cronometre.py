from PySide6.QtWidgets import (
    QLabel, QWidget, QPushButton, QVBoxLayout, QCheckBox,
    QTimeEdit, QHBoxLayout
)
from PySide6.QtCore import (
    QTime, QTimer, Slot, QElapsedTimer, QSize, Qt, Signal
)
from PySide6.QtGui import QIcon

import recursos_cronometre


class Cronometro():
    def __init__(self):
        self.__tiempo_transcurrido = QElapsedTimer()
        self.__tiempo_pausa = QElapsedTimer()
        self.__acumulador = 0

    def iniciar(self):
        self.__tiempo_transcurrido.restart()
        self.__acumulador = 0

    def obtenerTiempo(self):
        return QTime(0, 0).addMSecs(
            self.__tiempo_transcurrido.elapsed() - self.__acumulador)

    def pausar(self):
        self.__tiempo_pausa.restart()

    def continuar(self):
        self.__acumulador = self.__acumulador + self.__tiempo_pausa.elapsed()


class CronometroUI(QWidget):
    mensaje = Signal(str)

    CRONOMETRO_RESET = 0
    CRONOMETRO_INICIADO = 1
    CRONOMETRO_PAUSADO = 2
    CRONOMETRO_PARADO = 3

    LISTA_ICONOS = {
        'play': ':/icons/play.png',
        'pause': ':/icons/pause.png',
        'stop': ':/icons/stop.png',
        'resume': ':/icons/resume.png',
        'restart': ':/icons/restart.png'
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.__estado = self.CRONOMETRO_RESET

        self.setLayout(layout)
        self.__cronometro = Cronometro()
        self.__tiempo = QTimer(self)
        self.__tiempo_aviso = QTime(0, 0, 0, 0)

        self.etiqueta = QLabel(QTime(0, 0).toString("hh:mm:ss"), self)
        self.etiqueta.setMinimumHeight(50)
        self.etiqueta.setAlignment(Qt.AlignCenter)
        self.etiqueta.setStyleSheet(
            "background-color: white;"
            "border: 2px solid black;"
            "font-size: 25px"
        )

        self.boton_inicio = QPushButton(
            QIcon(self.LISTA_ICONOS['play']), "", self)
        self.boton_inicio.setIconSize(QSize(50, 50))
        # self.boton_inicio.setCheckable(True)
        self.boton_pausa = QPushButton(
            QIcon(self.LISTA_ICONOS['pause']), "", self)
        self.boton_pausa.setIconSize(QSize(50, 50))
        # self.boton_inicio.setCheckable(True)
        self.boton_pausa.setDisabled(True)

        self.aviso = QCheckBox("Avisar quan arribe a ...", self)
        self.editor_tiempo_aviso = QTimeEdit(QTime(0, 0), self)
        self.editor_tiempo_aviso.setDisplayFormat("hh:mm:ss")

        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(self.aviso)
        layout_horizontal.addWidget(self.editor_tiempo_aviso)

        layout.addLayout(layout_horizontal)
        layout.addWidget(self.etiqueta)
        layout.addWidget(self.boton_inicio)
        layout.addWidget(self.boton_pausa)

        self.__tiempo.timeout.connect(self.actualizar_tiempo)
        self.boton_inicio.clicked.connect(self.iniciar_parar)
        self.boton_pausa.clicked.connect(self.pausar_continuar)
        self.editor_tiempo_aviso.timeChanged.connect(
            self.actualizar_tiempo_aviso)

    @Slot()
    def actualizar_tiempo(self):
        crono_actual = self.__cronometro.obtenerTiempo()
        self.etiqueta.setText(
            crono_actual.toString("hh:mm:ss"))
        self.etiqueta.repaint()  # Actualiza el valor antes de lanzar aviso
        if self.aviso.isChecked():
            if -200 < self.__tiempo_aviso.msecsTo(crono_actual) < 200:
                self.mensaje.emit("Temps límit alcançat")

    @Slot()
    def iniciar_parar(self):
        if self.__estado == self.CRONOMETRO_RESET:  # Iniciar
            self.__cronometro.iniciar()
            self.__tiempo.start(1000)
            self.__estado = self.CRONOMETRO_INICIADO
            self.boton_pausa.setDisabled(False)
            self.boton_inicio.setIcon(QIcon(self.LISTA_ICONOS['stop']))
        elif self.__estado == self.CRONOMETRO_PARADO:  # Reiniciar
            self.__estado = self.CRONOMETRO_RESET
            self.etiqueta.setText(
                QTime(0, 0).toString("hh:mm:ss"))
            self.boton_inicio.setIcon(QIcon(self.LISTA_ICONOS['play']))
        else:  # Parar
            self.__tiempo.stop()
            self.__estado = self.CRONOMETRO_PARADO
            self.boton_inicio.setIcon(QIcon(self.LISTA_ICONOS['restart']))
            self.boton_pausa.setDisabled(True)

    @Slot()
    def pausar_continuar(self):
        if self.__estado == self.CRONOMETRO_INICIADO:  # Pausar
            self.__cronometro.pausar()
            self.__tiempo.stop()

            self.__estado = self.CRONOMETRO_PAUSADO
            self.boton_pausa.setIcon(QIcon(self.LISTA_ICONOS['resume']))
            self.boton_inicio.setDisabled(True)
        else:  # Continuar
            self.__cronometro.continuar()
            self.__tiempo.start()

            self.__estado = self.CRONOMETRO_INICIADO
            self.boton_pausa.setIcon(QIcon(self.LISTA_ICONOS['pause']))
            self.boton_inicio.setDisabled(False)

    @Slot()
    def actualizar_tiempo_aviso(self):
        self.__tiempo_aviso = self.editor_tiempo_aviso.time()


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication([])

    crono = CronometroUI()
    crono.show()

    app.exec()
