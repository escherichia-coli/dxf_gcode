from PyQt5 import QtCore, QtGui, QtWidgets
from ui.dxf_to_gcode_choose_layer_base import Ui_DXF_to_Gcode_choose_layers

class DXFtoGCODEChooseLayers(Ui_DXF_to_Gcode_choose_layers):

    def __init__(self, window_widget, mclass=None, layers=[0]):
        self.__window_widget = window_widget
        super().setupUi(self.__window_widget)
        self.n_layer = len(layers)
        self.cb_list = []
        self.layers = layers
        self.mclass = mclass
        # self.__window_widget.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.__window_widget.setWindowFlag(QtCore.Qt.FramelessWindowHint, True)

        for i in range(self.n_layer):
            self.cb_list.append(QtWidgets.QCheckBox())
            self.cb_list[-1].setObjectName("cb_" + str(i))
            self.cb_list[-1].setChecked(True)
            self.cb_list[-1].setText(self.layers[i])
            self.vl.addWidget(self.cb_list[-1], 10)

        self.hl = QtWidgets.QHBoxLayout()
        self.hl.setObjectName("hl")
        self.btn_ok = QtWidgets.QPushButton()
        self.btn_ok.setObjectName("btn_ok")
        self.btn_ok.setText('OK')
        self.hl.addWidget(self.btn_ok)
        self.btn_cancel = QtWidgets.QPushButton()
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.setText('Cancel')
        self.hl.addWidget(self.btn_cancel)
        self.vl.addLayout(self.hl)

        self.btn_ok.clicked.connect(self.__ok)
        self.btn_cancel.clicked.connect(self.__cancel)

    def __ok(self):
        status_list = []
        for cb in self.cb_list:

            if cb.isChecked():
                status_list.append(True)
            else:
                status_list.append(False)

        if self.mclass is not None:
            self.mclass.layer_to_display = status_list
        self.__window_widget.close()

    def __cancel(self):

        self.__window_widget.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    ui = DXFtoGCODEChooseLayers(w, None, ['Test', 'Layer 1', 'Layer 2'])
    w.show()
    sys.exit(app.exec_())