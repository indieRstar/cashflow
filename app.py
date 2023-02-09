import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cashflow")
        button = QPushButton("Start Analyzing")

        self.setGeometry(300, 300, 300, 200)
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
