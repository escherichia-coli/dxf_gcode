from PyQt5 import QtCore, QtGui, QtWidgets
from dxf_to_gcode_ui import UI_DXF_to_Gcode
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = UI_DXF_to_Gcode(w)
    w.show()
    sys.exit(app.exec_())