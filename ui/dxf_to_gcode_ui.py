from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,
                          QTime)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
                             QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout,
                             QWidget, QTreeWidgetItem, QColorDialog)

import pyqtgraph as pg
import pyqtgraph.console
import numpy as np
import time
from ui.dxf_to_gcode_ui_base import Ui_dxf_to_gcode
import ezdxf
import sys
from ui.bin.g_code_process import GcodeProcess
from ui.bin.dxf_to_gcode_geometry import DXFtoGCODE_Geometry
from ui.dxf_to_gcode_line_editor import UI_LineEditor
from ui.export_to_gcode_options import UI_DXF_to_Gcode_options
from ui.dxf_to_gcode_choose_layer import DXFtoGCODEChooseLayers

from ui.file_dialog.file_dialog_open_dxf import UI_OpenDXF
from ui.file_dialog.file_dialog_open_nmodel import UI_OpenNMODEL
from ui.file_dialog.file_dialog_save_gcode import UI_SaveGcode
from ui.file_dialog.file_dialog_save_model import UI_SaveModel


class Decorater(object):
    def __init__(self, mclass):
        self.mclass = mclass

    @property
    def Group(self):
        self.mclass.groupFunc()

    @property
    def Delete(self):
        self.mclass.delete()

    def Offset(self, th=None, of=None):
        if th is not None:
            self.mclass.th = th
        if of is not None:
            self.mclass.geo_tool.offset = of
        self.mclass.offsetFunc()

    def Move(self, x, y):
        self.mclass.move(x, y)

    def Trim(self, n):
        self.mclass.trim(n)

    @property
    def Export(self):
        self.mclass.exportGcode()

    @property
    def Import(self):
        self.mclass.importFunc()

    @property
    def Clean(self):
        self.mclass.geo_tool.clean(self.mclass.polylines)

    @property
    def Modify(self):
        self.mclass.modify()


class UI_DXF_to_Gcode(Ui_dxf_to_gcode):
    def __init__(self, window_widget):
        self.__window_widget = window_widget
        super().setupUi(self.__window_widget)
        self.btn_import.clicked.connect(self.importFunc)
        self.file = None
        self.polylines = []
        self.drawing = []
        self.lines_color = []
        self.test = 0
        self.deleted_lines = []
        self.c_hfile = open('console.history', 'w')
        self.c_hfile.close()

        self.gcode_processer = GcodeProcess()
        self.geo_tool = DXFtoGCODE_Geometry()

        self.deco = Decorater(self)

        self.OpenDXF = UI_OpenDXF()
        self.OpenNMODEL = UI_OpenNMODEL()
        self.SaveGcode = UI_SaveGcode()
        self.SaveModel = UI_SaveModel()

        namespace = {'pg': pg, 'np': np, 'dxf': self.deco}

        self.plotW = pg.PlotWidget()
        self.plot_layout = QtWidgets.QVBoxLayout(self.w_plot)
        self.plot_layout.addWidget(self.plotW)
        self.plotW.plot([0, 0, 200, 200, 0], [0, 200, 200, 0, 0], pen='g')
        self.plotW.setAspectLocked(lock=True, ratio=1)

        self.c = pg.console.ConsoleWidget(namespace=namespace)
        self.console_layout = QtWidgets.QVBoxLayout(self.w_console)
        self.console_layout.addWidget(self.c)
        self.line_selection = []
        self.tv.itemSelectionChanged.connect(self.__treeClicked)
        self.lines_group = []

        self.actionOpen.triggered.connect(self.open)
        self.actionDeleteG.triggered.connect(self.delete)
        self.actionGroup.triggered.connect(self.groupFunc)
        self.actionSet_color.triggered.connect(self.__setLinesColor)
        self.actionOptions.triggered.connect(self.__defineExportOptions)
        self.actionImport_dxf.triggered.connect(self.importFunc)
        self.actionModify.triggered.connect(self.modify)
        self.actionSetOffsetThickness.triggered.connect(self.__setTh)
        self.actionSetOffsetValue.triggered.connect(self.__setOffVal)

        self.btn_group.clicked.connect(self.groupFunc)
        self.btn_export_gcode.clicked.connect(self.exportGcode)
        self.btn_offset.clicked.connect(self.offsetFunc)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_save.clicked.connect(self.save)
        self.btn_quit.clicked.connect(self.quit)

        self.offset = 0.1
        self.th = 1

        self.w_line_editor = QtWidgets.QWidget()
        self.ui_line_editor = UI_LineEditor(self.w_line_editor, self)

        self.drawing_pnt = []

        self.btn_offset.setText("Offset (" + str(self.th) + ' - ' + str(self.offset) + ')')

        print(self.c.input.history)

    def quit(self):
        self.__window_widget.close()

    def __defineExportOptions(self):
        self.w_export_options = QtWidgets.QMainWindow()

        self.ui_export_options = UI_DXF_to_Gcode_options(self.w_export_options)
        self.w_export_options.show()

    def __readFile(self):
        try:
            doc = ezdxf.readfile(self.file_name)
            # doc = ezdxf.readfile("PLANdZ.dxf")

        except IOError:
            print(f'Not a DXF file or a generic I/O error.')
            sys.exit(1)
        except ezdxf.DXFStructureError:
            print(f'Invalid or corrupted DXF file.')
            sys.exit(2)

        msp = doc.modelspace()
        psp = doc.layers
        n_layer = len(doc.layers)
        self.layer_to_display = [True]
        layer_names = []
        for layer in psp:
            layer_names.append(layer.dxf.name)

        if n_layer > 1:
            self.c.write(str(n_layer) + ' layers have been detected.\nPlease select the layers to be displayed\n')
            self.w_choose_layer = QtWidgets.QWidget()
            self.choose_layer = DXFtoGCODEChooseLayers(self.w_choose_layer, self, layer_names)
            self.w_choose_layer.show()

            while len(self.layer_to_display) == 1:
                QtCore.QCoreApplication.processEvents()

        i = 0
        # for e in psp[0]:
        for e in msp:
            polyline = []
            if e.dxftype() == 'LWPOLYLINE' and self.layer_to_display[layer_names.index(e.get_dxf_attrib("layer"))]:
                # print(e.get_dxf_attrib("layer"))
                # print(e.dxf.flags)
                for f in e:
                    polyline.append([f[0], f[1]])
                if e.dxf.flags == 1:
                    polyline.append([e[0][0], e[0][1]])
                self.polylines.append(polyline)
            i = i + 1
        # self.polylines = self.geo_tool.clean(self.polylines)
        text = 'File ' + str(self.file_name) + ' loaded. \n'
        text = text + str(i) + ' polylines succefully imported\n'
        self.polylines_number = [i for i in range(len(self.polylines))]
        # print(self.polylines_number)

        self.c.write(text)

    def __setLinesColor(self):
        color = QColorDialog.getColor()
        for i in self.line_selection:
            self.lines_color[i] = color
            self.drawing[i].setPen(self.lines_color[i])

    def __treeClicked(self):
        self.line_selection = []
        for i in range(self.root.childCount()):
            if self.root.child(i).childCount() > 0:
                if self.root.child(i).isSelected():
                    for j in range(self.root.child(i).childCount()):
                        self.line_selection.append(int(self.lines_group[i].child(j).text(0).split(' ')[-1]))
                else:
                    for j in range(self.root.child(i).childCount()):
                        if self.root.child(i).child(j).isSelected():
                            self.line_selection.append(int(self.lines_group[i].child(j).text(0).split(' ')[-1]))
            else:

                if self.root.child(i).isSelected():
                    # print(int(self.root.child(i).text(0).split(' ')[-1]))
                    self.line_selection.append(int(self.root.child(i).text(0).split(' ')[-1]))

        self.__setLineSelected(True)

    def __setLineSelected(self, selected=True):
        if selected:
            self.ui_line_editor.line_selection = self.line_selection
            for i in range(len(self.drawing)):
                # print(self.drawing[i].opts.get('pen'))
                if self.drawing[i].opts.get('pen') != 'w':
                    self.drawing[i].setPen(self.lines_color[i])
            self.c.write('Line(s) ' + str(self.line_selection) + ' currently selected\n')

            for i in self.line_selection:
                for j in range(self.root.childCount()):
                    if self.root.child(j).childCount() > 0:
                        for k in range(self.root.child(j).childCount()):
                            if int(self.root.child(j).child(k).text(0).split(' ')[-1]) == i:
                                self.drawing[i].setPen('b')
                    else:
                        if int(self.root.child(j).text(0).split(' ')[-1]) == i:
                            self.drawing[i].setPen('b')

    def __setTh(self):
        self.c.write('Set the offset thickness and press enter \n')
        h_len = len(self.c.input.history)
        while self.c.input.history[0] != '' or len(self.c.input.history) == h_len:
            QtCore.QCoreApplication.processEvents()

        self.th = float(self.c.input.history[1])
        self.c.write('Offset thickness set to ' + str(self.th) + '\n')
        self.btn_offset.setText("Offset (" + str(self.th) + ' - ' + str(self.offset) + ')')

    def __setOffVal(self):
        self.c.write('Set the offset value and press enter \n')
        h_len = len(self.c.input.history)
        while self.c.input.history[0] != '' or len(self.c.input.history) == h_len:
            QtCore.QCoreApplication.processEvents()

        self.offset = float(self.c.input.history[1])
        self.c.write('Offset value set to ' + str(self.offset) + '\n')
        self.btn_offset.setText("Offset (" + str(self.th) + ' - ' + str(self.offset) + ')')

    def setLineSelected(self, add_root=True):
        self.__setLineSelected()
        # self.__updateTree(add_root=add_root)

    def lineClicked(self, c_line):
        n_curve = c_line.opts.get('data')
        self.ui_line_editor.le_selected_line.setText('Line n° ' + str(n_curve))
        self.line_selection.append(int(n_curve))

        for i in range(self.root.childCount()):
            if self.root.child(i).childCount() > 0:
                for j in range(self.root.child(i).childCount()):
                    if int(self.root.child(i).child(j).text(0).split(' ')[-1]) == n_curve:
                        self.root.child(i).child(j).setSelected(True)
            else:
                if int(self.root.child(i).text(0).split(' ')[-1]) == n_curve:
                    self.root.child(i).setSelected(True)

        self.__setLineSelected(True)

    def draw(self, ind=0):
        i = ind
        for polyline in self.polylines[ind:]:
            x = [j[0] for j in polyline]
            y = [j[1] for j in polyline]
            self.drawing.append(self.plotW.plot(x, y, connect='all', data=i, clickable=True))
            self.plotW.setAspectLocked(lock=True, ratio=1)
            self.lines_color.append('w')
            self.drawing[-1].setPen(self.lines_color[-1])
            self.drawing[-1].curve.setClickable(True)
            self.drawing[-1].sigClicked.connect(self.lineClicked)
            i = i + 1

    def __updateTree(self, ind=0, add_root=True):
        if add_root and ind == 0:
            self.root = QTreeWidgetItem([self.file_name])
        i = ind
        for polyline in self.polylines[ind:]:
            line = QTreeWidgetItem(['Line n° ' + str(i)])
            self.root.addChild(line)
            i = i + 1
        if self.tv.topLevelItem(0) is not None:
            if self.tv.topLevelItem(0).text(0) != self.file_name:
                print('Delete')
                self.drawing = []
                self.plotW.clear()
                self.plotW.plot([0, 0, 200, 200, 0], [0, 200, 200, 0, 0], pen='g')
                self.plotW.setAspectLocked(lock=True, ratio=1)
                self.tv.clear()
        self.tv.addTopLevelItem(self.root)
        self.tv.expandItem(self.root)

    def importFunc(self):

        self.polylines = []
        # self.file_name = 'PLANdZ2.dxf'
        # self.w_file_dialog = QtWidgets.QMainWindow()
        self.file_name = self.OpenDXF.openFileNameDialog()
        if self.file_name is not None:
            self.__readFile()
            self.__updateTree()
            self.draw(0)

    def delete(self):
        for i in self.line_selection:
            self.deleted_lines.append(i)
            self.drawing[i].clear()

        for items in self.tv.selectedItems():
            self.root.removeChild(items)

    def move(self, x, y):
        for polyline in self.polylines:
            for points in polyline:
                points[0] = points[0] + x
                points[1] = points[1] + y
        self.plotW.clear()
        self.plotW.plot([0, 0, 200, 200, 0], [0, 200, 200, 0, 0], pen='g')
        self.drawing = []
        self.draw()

    def trim(self, n):
        for i in self.line_selection:
            if n > 0:
                self.polylines[i] = self.polylines[i][n:]
                print(self.drawing[i])
            elif n < 0:
                self.polylines[i] = self.polylines[i][:n]

        # self.draw()

    def __pntClicked(self, pnt):
        self.pnt_selection = int(pnt.opts.get('data'))
        self.c.write('\nPnt n°' + str(self.pnt_selection) + ' selected\n')
        self.ui_line_editor.le_selected_pnt.setText('Point n° ' + str(self.pnt_selection))
        # pass

    def scatterPoints(self, polyline):
        # x = [j[0] for j in polyline]
        # y = [j[1] for j in polyline]
        i = 0
        for pnt in polyline:
            # print(pnt[0])
            # print(pnt[1])
            self.drawing_pnt.append(self.plotW.scatterPlot([pnt[0]], [pnt[1]], data=i, pen='r', clickable=True))
            self.drawing_pnt[-1].scatter.setSize(10)
            self.drawing_pnt[-1].sigClicked.connect(self.__pntClicked)
            i = i + 1

    def modify(self):
        # self.ui_line_editor = UI_LineEditor(self.w_line_editor, self)
        print(self.w_line_editor.isVisible())
        self.w_line_editor.show()
        self.ui_line_editor.isOpen = True
        # print(self.ui_line_editor.isOpen)
        # self.drawing_pnt = []
        # for i in self.line_selection:
        #     self.__scatterPoints(self.polylines[i])

    def groupFunc(self):
        to_add = []

        for i in range(self.root.childCount()):
            if self.root.child(i).childCount() == 0:
                for lines in self.line_selection:
                    if int(self.root.child(i).text(0).split(' ')[-1]) == lines:
                        to_add.append(self.root.child(i))
                        break

        if len(to_add) > 1:
            self.root.addChild
            self.lines_group.append(QTreeWidgetItem(['Group n° ' + str(len(self.lines_group))]))
            for i in range(len(to_add)):
                self.root.removeChild(to_add[i])
                self.lines_group[-1].addChild(to_add[i])

            self.root.insertChild(len(self.lines_group) - 1, self.lines_group[-1])

    def offsetFunc(self):
        # print(self.geo_tool.offset)
        self.btn_offset.setText("Offset (" + str(self.th) + ' - ' + str(self.offset) + ')')

        line_selected = self.line_selection
        for i in line_selected:
            len_polylines = len(self.polylines)
            offset_lines = self.geo_tool.setThickness(self.polylines[i], self.th, 'alt', self.offset)
            for offset_line in offset_lines:
                self.polylines.append(offset_line)

            self.draw(len_polylines)
            self.__updateTree(len_polylines)
            self.line_selection = range(len_polylines, len(self.polylines))
            self.groupFunc()
            self.lines_group[-1].setText(0, 'Offset line n° ' + str(i))
            self.line_selection = []

    def exportGcode(self):
        if len(self.polylines) == 0:
            self.c.write('No geometry to export\n')
            return None
        polylines_to_export = []
        for i in range(len(self.polylines)):
            if i not in self.deleted_lines:
                polylines_to_export.append(self.polylines[i])

        gcode_file_name = self.SaveGcode.openFileNameDialog()
        print(gcode_file_name)
        self.gcode_processer.buildGcode(polylines_to_export, file_name=gcode_file_name)
        self.c.write('Gcode succefully exported\n')
        minutes = int(self.gcode_processer.e_time)
        seconds = int(60 * (self.gcode_processer.e_time - minutes))
        self.c.write('Estimated engraving time : ' + str(minutes) + ' min ' + str(seconds) + ' sec\n')

    def save(self):
        save_file_name = self.SaveModel.openFileNameDialog()
        save_file = open(save_file_name, 'w')

        for polyline in self.polylines:
            i = 0
            length = len(polyline)
            for pnt in polyline:
                save_file.write(str(pnt[0]))
                save_file.write(' ')
                save_file.write(str(pnt[1]))
                i = i + 1
                if i != length:
                    save_file.write(',')
            save_file.write('\n')

        save_file.close()

    def open(self):
        open_file_name = self.OpenNMODEL.openFileNameDialog()
        open_file = open(open_file_name, 'r')
        lines = open_file.readlines()
        self.polylines = []
        for line in lines:
            self.polylines.append([])
            line = line.replace('\n', '')
            line = line.split(',')
            for pnt in line:
                # print(pnt)
                pnt = pnt.split(' ')
                # print(pnt)
                if len(pnt) == 2:
                    x = float(pnt[0])
                    y = float(pnt[1])
                    self.polylines[-1].append([x, y])
        self.file_name = open_file_name
        self.__updateTree()
        self.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = UI_DXF_to_Gcode(w)
    w.show()
    sys.exit(app.exec_())
