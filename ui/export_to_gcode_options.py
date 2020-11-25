from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui.export_to_gcode_options_base import Ui_dxf_to_gcode_options
from ui.lib.g_code_process import GcodeProcess


class UI_DXF_to_Gcode_options(Ui_dxf_to_gcode_options):
    def __init__(self, window_widget):
        self.__window_widget = window_widget
        super().setupUi(self.__window_widget)
        self.btn_save.clicked.connect(self.save)
        self.btn_quit.clicked.connect(self.quit)
        # self.file = open('DXF_toGcode.options', 'w')
        self.read()

    def read(self):
        option_file = open('DXF_toGcode.options', 'r')
        lines = option_file.readlines()
        for line in lines:
            if line.split(':')[0] == 'LASER POWER ':
                self.power_slider.setValue(int(line.split(':')[1].replace('\n', '')))

            if line.split(':')[0] == 'ENGRAVING SPEED ':
                self.le_engraving_speed.setText(str(int(line.split(':')[1].replace('\n', ''))))

            if line.split(':')[0] == 'TRAVEL SPEED ':
                self.le_travel_speed.setText(str(int(line.split(':')[1].replace('\n', ''))))

            if line.split(':')[0] == 'X OFFSET ':
                self.le_x_offset.setText(str(int(line.split(':')[1].replace('\n', ''))))

            if line.split(':')[0] == 'Y OFFSET ':
                self.le_y_offset.setText(str(int(line.split(':')[1].replace('\n', ''))))

            if line.split(':')[0] == 'N LAYER ':
                self.le_n_layer.setText(str(int(line.split(':')[1].replace('\n', ''))))
        option_file.close()

    def save(self):
        file = open('DXF_toGcode.options', 'w')
        file.truncate(0)
        file = open('DXF_toGcode.options', 'w')
        file.write('LASER POWER : ')
        file.write(str(self.power_slider.value()))
        file.write('\n')

        file.write('ENGRAVING SPEED : ')
        file.write(str(self.le_engraving_speed.text()))
        file.write('\n')

        file.write('TRAVEL SPEED : ')
        file.write(str(self.le_travel_speed.text()))
        file.write('\n')

        file.write('X OFFSET : ')
        file.write(str(self.le_x_offset.text()))
        file.write('\n')

        file.write('Y OFFSET : ')
        file.write(str(self.le_y_offset.text()))
        file.write('\n')

        file.write('N LAYER : ')
        file.write(str(self.le_n_layer.text()))

        file.close()
        self.__window_widget.close()

    def quit(self):
        self.__window_widget.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = UI_DXF_to_Gcode_options(w)
    w.show()
    sys.exit(app.exec_())
