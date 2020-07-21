import sys
from PyQt5.QtWidgets import  QApplication,QFrame
from PyQt5.uic import loadUi

class Ilets(QFrame) :
    def __init__(self):
        super(Ilets,self).__init__()
        loadUi("main.ui",self)
        self.setWindowTitle("ILETS Correct")
app=QApplication(sys.argv)
widget=Ilets()
widget.show()
sys.exit(app.exec_())
