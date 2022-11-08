import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from analyze import analyze
from finder import googleparse
from window import Ui_MainWindow

URL = 'http://www.google.com/search?q='


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushbutton.clicked.connect(self.search)
        self.text = ''
        self.page = ''
        self.dict = ''

    def search(self):
        print(' '.join(analyze(self.linedit.text())))
        print(googleparse(' '.join(analyze(self.linedit.text()))))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
