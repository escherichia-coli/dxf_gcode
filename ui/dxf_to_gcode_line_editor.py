from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui.dxf_to_gcode_line_editor_base import Ui_line_editor_base
import numpy as np


class UI_LineEditor(Ui_line_editor_base):
    def __init__(self, window_widget, mclass):
        self.mclass = mclass
        self.__window_widget = window_widget
        self.__window_widget.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # self.__window_widget.setwindowaFlags()
        super().setupUi(self.__window_widget)

        self.mclass.c.write('Line Editor opened\n')
        self.line_selection = self.mclass.line_selection
        # self.__window_widget.triggered.connect(self.__lineClicked)
        self.btn_select_line.clicked.connect(self.__lineClicked)
        self.btn_select_pnt.clicked.connect(self.__pntClicked)
        self.btn_delete_pnt.clicked.connect(self.__delete)

    def __lineClicked(self):
        print(self.line_selection)
        self.enable_sel = True
        if len(self.mclass.line_selection) > 1:
            self.mclass.line_selection = []
            self.mclass.setLineSelected(add_root=False)
            self.le_selected_line.setText('None')
        else:
            if len(self.mclass.drawing_pnt) != 0:
                for pnt in self.mclass.drawing_pnt:
                    self.mclass.plotW.removeItem(pnt)
                self.mclass.drawing_pnt = []
            self.mclass.drawing_pnt = []
            self.le_selected_line.setText('Line n° ' + str(self.mclass.line_selection[0]))
            self.mclass.scatterPoints(self.mclass.polylines[self.mclass.line_selection[0]])

    def __pntClicked(self):
        if self.mclass.pnt_selection is not None:
            self.le_selected_pnt.setText('Point n° ' + str(self.mclass.pnt_selection))

    def __delete(self):
        n_line = int(self.le_selected_line.text().split(' ')[-1])
        n_pnt = int(self.le_selected_pnt.text().split(' ')[-1])
        print('Polylines : ', self.mclass.polylines)
        print('Polyline : ', self.mclass.polylines[n_line])
        # print('Delete : ', np.delete(self.mclass.polylines[n_line], n_pnt, axis=0))
        pl = np.delete(self.mclass.polylines[n_line], n_pnt, axis=0)
        self.mclass.polylines[n_line] = pl
        print('Polyline after deletion : ', self.mclass.polylines[n_line])
        x = [i[0] for i in self.mclass.polylines[n_line]]
        y = [i[1] for i in self.mclass.polylines[n_line]]
        self.mclass.drawing[n_line].clear()
        self.mclass.drawing[n_line] = self.mclass.plotW.plot(x, y, connect='all', data=n_line, clickable=True)
        self.mclass.drawing[n_line].curve.setClickable(True)
        self.mclass.drawing[n_line].sigClicked.connect(self.mclass.lineClicked)
        # self.mclass.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    ui = UI_LineEditor(w)
    w.show()
    sys.exit(app.exec_())
