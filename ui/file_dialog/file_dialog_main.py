from PyQt5 import QtCore, QtGui, QtWidgets
import os

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.extension = "(*.txt)"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog().Options()

        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, self.title, "", self.extension, options=options)
        if fileName:
            temp_filepath = str(fileName).split('/')
            filepath = ''
            for step in temp_filepath[:-1]:
                filepath = filepath + '/' + step
            return fileName
