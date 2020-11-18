from file_dialog_main import App

class UI_OpenNMODEL(App):
    def __init__(self):
        super().__init__()
        self.title = 'Open nmodel'
        self.extension = "(*.nmodel)"