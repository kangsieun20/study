import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic

class MyForm(QDialog):
    def __init__(self, parent=None):
        #QDialog.__init__(self, parent)
        super().__init__(parent)
        self.ui = uic.loadUi('hello.ui')
        self.ui.show()
        
app = QApplication(sys.argv)
w = MyForm()
sys.exit(app.exec())
