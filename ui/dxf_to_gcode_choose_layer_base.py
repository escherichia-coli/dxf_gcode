# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Python_Project/dxf_gcode/ui/dxf_to_gcode_choose_layer_base.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DXF_to_Gcode_choose_layers(object):
    def setupUi(self, DXF_to_Gcode_choose_layers):
        DXF_to_Gcode_choose_layers.setObjectName("DXF_to_Gcode_choose_layers")
        DXF_to_Gcode_choose_layers.resize(176, 66)
        self.vl = QtWidgets.QVBoxLayout(DXF_to_Gcode_choose_layers)
        self.vl.setObjectName("vl")

        self.retranslateUi(DXF_to_Gcode_choose_layers)
        QtCore.QMetaObject.connectSlotsByName(DXF_to_Gcode_choose_layers)

    def retranslateUi(self, DXF_to_Gcode_choose_layers):
        _translate = QtCore.QCoreApplication.translate
        DXF_to_Gcode_choose_layers.setWindowTitle(_translate("DXF_to_Gcode_choose_layers", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DXF_to_Gcode_choose_layers = QtWidgets.QWidget()
    ui = Ui_DXF_to_Gcode_choose_layers()
    ui.setupUi(DXF_to_Gcode_choose_layers)
    DXF_to_Gcode_choose_layers.show()
    sys.exit(app.exec_())
