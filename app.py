import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.show()

app.exec()
