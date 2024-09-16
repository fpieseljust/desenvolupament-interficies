import os

from cronometre import CronometroUI
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMessageBox, QMenu
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt, Slot

import recursos_a03 

@Slot()
def mostrar_ocultar():
    if cronometro.isHidden():
        cronometro.show()
    else:
        cronometro.hide()

@Slot()
def mostrar_aviso(mensaje):
    QMessageBox.information(cronometro, "Cronómetro PySide6", mensaje)

if __name__ == "__main__":
   
    app = QApplication([])
    
    # Asignamos un icono a la ventana
    app.setWindowIcon(QIcon(":/icons/cronometro.png"))

    # Para que no se cierre al cerrar la útlima ventana
    app.setQuitOnLastWindowClosed(False)
        
    # Agregamos la aplicación al tray
    icon = QIcon(QIcon(":/icons/cronometro.png"))
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    tray.activated.connect(mostrar_ocultar)
    
    # Creamos un componente cronómetro
    cronometro = CronometroUI()

    # Cambiamos propiedades del componente
    cronometro.setWindowTitle("Cronómetro PySide6")
    # Para que sea siempre visible
    cronometro.setWindowFlag(Qt.WindowStaysOnTopHint) 

    # Creamos un QAction y lo conectamos al slot quit, para cerrar la aplicación
    accion_salir = QAction("Salir", cronometro)
    accion_salir.triggered.connect(app.quit)

    # Creamos un menú y añadimos la acción
    menu = QMenu()
    menu.addAction(accion_salir)

    # Añadimos el menú contextual al icono del tray
    tray.setContextMenu(menu)

    # Utilizamos la señal del componente
    cronometro.mensaje.connect(mostrar_aviso)
    
    cronometro.show()
    app.exec()