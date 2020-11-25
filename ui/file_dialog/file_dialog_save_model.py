from PyQt5 import QtCore, QtGui, QtWidgets
from ui.file_dialog.file_dialog_main import App


class UI_SaveModel(App):
    def __init__(self):
        super().__init__()
        self.title = 'Save model'
        self.extension = "(*.nmodel)"

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog().Options()
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, self.title, "", self.extension, options=options)
        if fileName[-7:] == '.nmodel':
            return fileName
        else:
            return fileName + '.nmodel'
