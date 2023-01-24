from PySide6.QtWidgets import QMenuBar, QMessageBox
from PySide6.QtGui import QAction
from storagehistory import StorageHistory
class MenuBarMain(QMenuBar):
    def __init__(self,app,main_widget,status_bar):
        super().__init__()

        # Menubar and menus
        # menu_bar = self.menuBar()

        file_menu = self.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.setStatusTip("Press this to Quit the Application")
        # Quit action calls the quit slot of QApplication
        quit_action.triggered.connect(app.quit)

        # Edit menus
        edit_menu = self.addMenu("Edit")
        # Edit Copy Action
        edit_copy_action = QAction("Copy", self)
        edit_copy_action.setStatusTip("Press this to See History")
        edit_copy_action.triggered.connect(main_widget.input_text_edit.copy)
        edit_menu.addAction(edit_copy_action)

        # Edit Cut Action
        edit_cut_action = QAction("Cut", self)
        edit_cut_action.setStatusTip("Press this to See History")
        edit_cut_action.triggered.connect(main_widget.input_text_edit.cut)
        edit_menu.addAction(edit_cut_action)

        # Edit Paste Action
        edit_paste_action = QAction("Paste", self)
        edit_paste_action.setStatusTip("Press this to See History")
        edit_paste_action.triggered.connect(main_widget.input_text_edit.paste)
        edit_menu.addAction(edit_paste_action)

        # Edit Undo Action
        edit_undo_action = QAction("Undo", self)
        edit_undo_action.setStatusTip("Press this to See History")
        edit_undo_action.triggered.connect(main_widget.input_text_edit.undo)
        edit_menu.addAction(edit_undo_action)

        # Edit Redo Action
        edit_redo_action = QAction("Redo", self)
        edit_redo_action.setStatusTip("Press this to See History")
        edit_redo_action.triggered.connect(main_widget.input_text_edit.redo)
        edit_menu.addAction(edit_redo_action)

        # edit_menu.addAction("Cut")
        # edit_menu.addAction("Paste")
        # edit_menu.addAction("Paste")
        # edit_menu.addAction("Undo")
        # edit_menu.addAction("Redo")

        # History
        history_menu = self.addMenu("History")

        # Show History Action
        show_history_action = QAction("Show History", self)
        show_history_action.setStatusTip("Press this to See History")
        show_history_action.triggered.connect(self.show_history_action_clicked)
        history_menu.addAction(show_history_action)

        # Clear History Action
        clear_history_action = QAction("Clear History", self)
        clear_history_action.setStatusTip("Press this to Clear History")
        clear_history_action.triggered.connect(self.clear_history_action_clicked)
        history_menu.addAction(clear_history_action)

        # Settings menu
        settings_menu = self.addMenu("Setting")
        settings_menu.addAction("Ada")
        settings_menu.addAction("Babbage")
        settings_menu.addAction("Curie")
        settings_menu.addAction("Da Vinci")

        # Other Menus
        self.addMenu("Window")
        self.addMenu("Help")


    # History Actions
    def show_history_action_clicked(self):
        print("Button-Hard clicked")
        message = QMessageBox()
        message.setMinimumSize(700,300)
        message.setWindowTitle("Chat History")

        # storage = StorageHistory()
        # history_list = storage.get_history()
        # history_list.reverse()
        # history_string = json.dumps(history_list, indent=4)

        # message.setText(f"This is the chat history {history_string}")
        message.setInformativeText("Do you want to do something about it")
        # message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        # Show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok :
            print("User chose Ok")
        elif ret == QMessageBox.Cancel :
            print("User chose Cancel")
        else:
            print("User chose unknown button")


    def clear_history_action_clicked(self):
        print("Clear History Action clicked")
        message = QMessageBox()
        message.setMinimumSize(700, 300)
        message.setWindowTitle("Clear Chat History")

        # storage = StorageHistory()
        # history_list = storage.get_history()
        # history_list.reverse()
        # history_string = json.dumps(history_list, indent=4)

        message.setText("Do you want to Clear Chat History")
        message.setInformativeText("Think Carefully Then Decide")
        # message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Cancel)

        # Show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
            storage = StorageHistory()
            storage.clear_history()
        elif ret == QMessageBox.Cancel:
            print("User chose Cancel")
        else:
            print("User chose unknown button")



