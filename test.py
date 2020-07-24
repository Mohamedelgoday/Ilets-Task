import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import  QApplication,QFrame
from PyQt5.uic import loadUi

@pyqtSlot()
class Ilets(QFrame) :
    def __init__(self):
        super(Ilets,self).__init__()
        loadUi("main.ui",self)
        self.setWindowTitle("ILETS Correct")
        #intro_correct_button
        self.intro_correct_button.clicked.connect(self.actionButton)

    def actionButton(self):
        self.intr_lexis_lable.setText("Ok Dev")
        self.intro_grammer_lable.setText("Ok Gogo"+self.intro_textEdit.toPlainText ())
        t=self.intro_textEdit.toPlainText ()
        self.intro_textEdit.setText("Ok Gogo"+t)

    
app=QApplication(sys.argv)
widget=Ilets()
widget.show()
sys.exit(app.exec_())
