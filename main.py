import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from analyze import analyze
from finder import googleparse
from window import Ui_MainWindow
URL = 'http://www.google.com/search?q='
from docks import loadbd


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushbutton.clicked.connect(self.search)
        self.text = ''
        self.page = ''
        self.dict = ''
        self.msg = QMessageBox()
        self.pushButton2.clicked.connect(self.load_from_bd)

    def search(self):
        self.textEdit.setPlainText('')
        try:
            self.textEdit.setPlainText(self.textEdit.toPlainText() + (googleparse(' '.join(analyze(self.linedit.text())))))
        except:
            self.msg.setWindowTitle("Ошибка")
            self.msg.setText("Кажется что-то пошло не так, измените запрос и попробуйте сновa")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()

    def load_from_bd(self):
        self.textEdit.setPlainText(loadbd())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
