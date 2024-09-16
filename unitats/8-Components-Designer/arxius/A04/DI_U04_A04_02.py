import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from DI_U04_A02_01 import CronometroUI

loader = QUiLoader()
app = QApplication(sys.argv)
loader.registerCustomWidget(CronometroUI)
window = loader.load("DI_U04_A04_01.ui", None)
window.show()
app.exec()