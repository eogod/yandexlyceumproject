import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

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
        self.msg = QMessageBox()

    def search(self):
        self.textEdit.setPlainText('')
        print(' '.join(analyze(self.linedit.text())))
        print(googleparse(self.linedit.text()))
        try:
            self.textEdit.setPlainText(self.textEdit.toPlainText() + (googleparse(' '.join(analyze(self.linedit.text())))))
        except:
            self.msg.setWindowTitle("Ошибка")
            self.msg.setText("Кажется что-то пошло не так, измените запрос и попробуйте сновa")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
