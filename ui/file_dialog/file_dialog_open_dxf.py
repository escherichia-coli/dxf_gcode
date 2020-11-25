from ui.file_dialog.file_dialog_main import App

class UI_OpenDXF(App):
    def __init__(self):
        super().__init__()
        self.title = 'Open dxf'
        self.extension = "(*.dxf)"