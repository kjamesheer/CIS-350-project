import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My PyQt MainWindow")
        self.setGeometry(100, 100, 400, 200) # (x, y, width, height)

        self.label = QLabel("Hello, PyQt MainWindow!", self)
        self.label.setGeometry(50, 50, 300, 100) # (x, y, width, height)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
