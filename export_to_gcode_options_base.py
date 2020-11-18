# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Python_Project/dxf_gcode/export_to_gcode_options_base.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dxf_to_gcode_options(object):
    def setupUi(self, dxf_to_gcode_options):
        dxf_to_gcode_options.setObjectName("dxf_to_gcode_options")
        dxf_to_gcode_options.resize(337, 288)
        self.horizontalLayoutWidget = QtWidgets.QWidget(dxf_to_gcode_options)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 240, 160, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_save = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_quit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_quit.setObjectName("btn_quit")
        self.horizontalLayout.addWidget(self.btn_quit)
        self.gridLayoutWidget = QtWidgets.QWidget(dxf_to_gcode_options)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.power_slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.power_slider.setMaximum(255)
        self.power_slider.setProperty("value", 255)
        self.power_slider.setOrientation(QtCore.Qt.Horizontal)
        self.power_slider.setObjectName("power_slider")
        self.gridLayout.addWidget(self.power_slider, 0, 2, 1, 1)
        self.le_engraving_speed = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_engraving_speed.setObjectName("le_engraving_speed")
        self.gridLayout.addWidget(self.le_engraving_speed, 1, 2, 1, 1)
        self.le_y_offset = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_y_offset.setObjectName("le_y_offset")
        self.gridLayout.addWidget(self.le_y_offset, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.le_travel_speed = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_travel_speed.setObjectName("le_travel_speed")
        self.gridLayout.addWidget(self.le_travel_speed, 2, 2, 1, 1)
        self.le_x_offset = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_x_offset.setObjectName("le_x_offset")
        self.gridLayout.addWidget(self.le_x_offset, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.le_n_layer = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_n_layer.setObjectName("le_n_layer")
        self.gridLayout.addWidget(self.le_n_layer, 5, 2, 1, 1)

        self.retranslateUi(dxf_to_gcode_options)
        QtCore.QMetaObject.connectSlotsByName(dxf_to_gcode_options)

    def retranslateUi(self, dxf_to_gcode_options):
        _translate = QtCore.QCoreApplication.translate
        dxf_to_gcode_options.setWindowTitle(_translate("dxf_to_gcode_options", "Gcode export options"))
        self.btn_save.setText(_translate("dxf_to_gcode_options", "Save"))
        self.btn_quit.setText(_translate("dxf_to_gcode_options", "Quit"))
        self.label_5.setText(_translate("dxf_to_gcode_options", "Y offset [mm]"))
        self.label_3.setText(_translate("dxf_to_gcode_options", "Travel speed [mm/min]"))
        self.label_4.setText(_translate("dxf_to_gcode_options", "X offset [mm]"))
        self.label.setText(_translate("dxf_to_gcode_options", "Laser  power [0 -255] "))
        self.le_engraving_speed.setText(_translate("dxf_to_gcode_options", "200"))
        self.le_y_offset.setText(_translate("dxf_to_gcode_options", "0"))
        self.label_2.setText(_translate("dxf_to_gcode_options", "Engraving speed [mm/min]"))
        self.le_travel_speed.setText(_translate("dxf_to_gcode_options", "6000"))
        self.le_x_offset.setText(_translate("dxf_to_gcode_options", "0"))
        self.label_6.setText(_translate("dxf_to_gcode_options", "Layer\'s number [-]"))
        self.le_n_layer.setText(_translate("dxf_to_gcode_options", "1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dxf_to_gcode_options = QtWidgets.QWidget()
    ui = Ui_dxf_to_gcode_options()
    ui.setupUi(dxf_to_gcode_options)
    dxf_to_gcode_options.show()
    sys.exit(app.exec_())
