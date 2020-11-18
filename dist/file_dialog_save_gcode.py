from PyQt5 import QtCore, QtGui, QtWidgets
from file_dialog_main import App


class UI_SaveGcode(App):
    def __init__(self):
        super().__init__()
        self.title = 'Export to Gcode'
        self.extension = "(*.gcode)"

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog().Options()
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, self.title, "", self.extension, options=options)
        if fileName[-6:] == '.gcode':
            return fileName
        else:
            return fileName + '.gcode'
