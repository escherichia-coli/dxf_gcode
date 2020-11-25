# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Python_Project/dxf_gcode/dxf_to_gcode_line_editor_base.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_line_editor_base(object):
    def setupUi(self, line_editor_base):
        line_editor_base.setObjectName("line_editor_base")
        line_editor_base.setWindowModality(QtCore.Qt.WindowModal)
        line_editor_base.resize(289, 223)
        self.gridLayout_2 = QtWidgets.QGridLayout(line_editor_base)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(line_editor_base)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btn_delete_pnt = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_delete_pnt.setObjectName("btn_delete_pnt")
        self.gridLayout_5.addWidget(self.btn_delete_pnt, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 1, 2, 1, 1)
        self.btn_add_before = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_add_before.setObjectName("btn_add_before")
        self.gridLayout_5.addWidget(self.btn_add_before, 2, 1, 1, 1)
        self.btn_add_after = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_add_after.setObjectName("btn_add_after")
        self.gridLayout_5.addWidget(self.btn_add_after, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_ok = QtWidgets.QPushButton(line_editor_base)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)
        self.btn_cancel = QtWidgets.QPushButton(line_editor_base)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.le_selected_line = QtWidgets.QLineEdit(line_editor_base)
        self.le_selected_line.setObjectName("le_selected_line")
        self.gridLayout_3.addWidget(self.le_selected_line, 0, 1, 1, 1)
        self.le_selected_pnt = QtWidgets.QLineEdit(line_editor_base)
        self.le_selected_pnt.setObjectName("le_selected_pnt")
        self.gridLayout_3.addWidget(self.le_selected_pnt, 2, 1, 1, 1)
        self.btn_select_pnt = QtWidgets.QPushButton(line_editor_base)
        self.btn_select_pnt.setObjectName("btn_select_pnt")
        self.gridLayout_3.addWidget(self.btn_select_pnt, 2, 0, 1, 1)
        self.btn_select_line = QtWidgets.QPushButton(line_editor_base)
        self.btn_select_line.setObjectName("btn_select_line")
        self.gridLayout_3.addWidget(self.btn_select_line, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(line_editor_base)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.le_move_y = QtWidgets.QLineEdit(self.groupBox)
        self.le_move_y.setObjectName("le_move_y")
        self.gridLayout_4.addWidget(self.le_move_y, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 1, 1, 1)
        self.le_move_x = QtWidgets.QLineEdit(self.groupBox)
        self.le_move_x.setObjectName("le_move_x")
        self.gridLayout_4.addWidget(self.le_move_x, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 1, 1, 1)

        self.retranslateUi(line_editor_base)
        QtCore.QMetaObject.connectSlotsByName(line_editor_base)

    def retranslateUi(self, line_editor_base):
        _translate = QtCore.QCoreApplication.translate
        line_editor_base.setWindowTitle(_translate("line_editor_base", "Line Editor"))
        self.groupBox_2.setTitle(_translate("line_editor_base", "Points"))
        self.btn_delete_pnt.setText(_translate("line_editor_base", "Delete"))
        self.btn_add_before.setText(_translate("line_editor_base", "Add Before"))
        self.btn_add_after.setText(_translate("line_editor_base", "Add After"))
        self.btn_ok.setText(_translate("line_editor_base", "Ok"))
        self.btn_cancel.setText(_translate("line_editor_base", "Cancel"))
        self.btn_select_pnt.setText(_translate("line_editor_base", "Select point"))
        self.btn_select_line.setText(_translate("line_editor_base", "Select line"))
        self.groupBox.setTitle(_translate("line_editor_base", "Move"))
        self.label_3.setText(_translate("line_editor_base", "   x"))
        self.label_4.setText(_translate("line_editor_base", "y"))
        self.pushButton_3.setText(_translate("line_editor_base", "Move"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    line_editor_base = QtWidgets.QWidget()
    ui = Ui_line_editor_base()
    ui.setupUi(line_editor_base)
    line_editor_base.show()
    sys.exit(app.exec_())
