from PySide6.QtWidgets import QMenuBar, QMessageBox
from PySide6.QtGui import QAction
from storagehistory import StorageHistory
from edit_query_settings_ui import EditQuerySettingsDialog
import os

class MenuBarMain(QMenuBar):
    def __init__(self, app, main_widget, status_bar):
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
        edit_copy_action.setStatusTip("Copy selected text in Input Box to Clipboard")
        edit_copy_action.triggered.connect(main_widget.input_text_edit.copy)
        edit_menu.addAction(edit_copy_action)

        # Edit Cut Action
        edit_cut_action = QAction("Cut", self)
        edit_cut_action.setStatusTip("Cut selected text in Input Box to Clipboard")
        edit_cut_action.triggered.connect(main_widget.input_text_edit.cut)
        edit_menu.addAction(edit_cut_action)

        # Edit Paste Action
        edit_paste_action = QAction("Paste", self)
        edit_paste_action.setStatusTip("Paste clipboard content to Input Box")
        edit_paste_action.triggered.connect(main_widget.input_text_edit.paste)
        edit_menu.addAction(edit_paste_action)

        # Edit Undo Action
        edit_undo_action = QAction("Undo", self)
        edit_undo_action.setStatusTip("Undo changes in Input Box")
        edit_undo_action.triggered.connect(main_widget.input_text_edit.undo)
        edit_menu.addAction(edit_undo_action)

        # Edit Redo Action
        edit_redo_action = QAction("Redo", self)
        edit_redo_action.setStatusTip("Redo changes in Input Box")
        edit_redo_action.triggered.connect(main_widget.input_text_edit.redo)
        edit_menu.addAction(edit_redo_action)

        # History
        history_menu = self.addMenu("History")

        # Show History Action
        show_history_action = QAction("Show History", self)
        show_history_action.setStatusTip("See Chat History")
        show_history_action.triggered.connect(self.show_history_action_clicked)
        history_menu.addAction(show_history_action)

        # Clear History Action
        clear_history_action = QAction("Clear History", self)
        clear_history_action.setStatusTip("Clear Chat History")
        clear_history_action.triggered.connect(self.clear_history_action_clicked)
        history_menu.addAction(clear_history_action)

        # Settings menu
        settings_menu = self.addMenu("Setting")

        # Edit Settings Action
        edit_settings_action = QAction("Edit Settings", self)
        edit_settings_action.setStatusTip("Edit Query Settings or Set API key")
        edit_settings_action.triggered.connect(self.edit_settings_action_triggered)
        settings_menu.addAction(edit_settings_action)

        # Help Menu
        help_menu = self.addMenu("Help")

        # Reference Manual Action
        reference_manual_action = QAction("Reference Manual", self)
        reference_manual_action.setStatusTip("Information about the Reference Manual")
        reference_manual_action.triggered.connect(self.reference_manual_action_triggered)
        help_menu.addAction(reference_manual_action)

        # About Application Action
        about_application_action = QAction("About", self)
        about_application_action.setStatusTip("Information about the Application")
        about_application_action.triggered.connect(self.about_application_action_triggered)
        help_menu.addAction(about_application_action)

        # About Pricing Action
        about_pricing_action = QAction("Pricing Details", self)
        about_pricing_action.setStatusTip("Information about the Pricing")
        about_pricing_action.triggered.connect(self.about_pricing_action_triggered)
        help_menu.addAction(about_pricing_action)

        # Other Menus
        # self.addMenu("Window")
        # self.addMenu("Help")

    def reference_manual_action_triggered(self):
        print("Reference Manual Triggered")

        message = QMessageBox()
        message.setMinimumSize(300, 200)
        message.setWindowTitle("Reference Manual")

        f_data = ""
        filename = "/home/darklord/Desktop/openai-client/reference_manual.txt"
        # If File does not exist create and empty file
        if not os.path.exists(filename):
            open(filename, 'w').close()
        # if the file is empty, put default settings in the file
        if os.stat(filename).st_size == 0:
            f_data = "Reference Manual is not Available"
        else:  # The file contains information about the reference manual
            with open(filename, "r") as f:
                f_data = f.readline()

        message.setText(f_data)
        # message.setInformativeText("Do you want to do something about it")
        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)

        # Show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose unknown button")
    def about_application_action_triggered(self):
        print("About Application Triggered")

        message = QMessageBox()
        message.setMinimumSize(300, 200)
        message.setWindowTitle("About OpenAI client")

        f_data = ""
        filename = "/home/darklord/Desktop/openai-client/about_application.txt"
        # If File does not exist create and empty file
        if not os.path.exists(filename):
            open(filename, 'w').close()
        # if the file is empty, put default settings in the file
        if os.stat(filename).st_size == 0:
            f_data = "About Application Information is not Available"
        else:  # The file contain information about application
            with open(filename, "r") as f:
                f_data = f.readline()

        message.setText(f_data)
        # message.setInformativeText("Do you want to do something about it")
        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)

        # Show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose unknown button")

    def about_pricing_action_triggered(self):
        print("About Pricing")

        message = QMessageBox()
        message.setMinimumSize(300, 200)
        message.setWindowTitle("Pricing Details")

        pricing_data = ""
        filename = "/home/darklord/Desktop/openai-client/pricing_details.txt"
        # If File does not exist create and empty file
        if not os.path.exists(filename):
            open(filename, 'w').close()
        # if the file is empty, put default settings in the file
        if os.stat(filename).st_size == 0:
            pricing_data = "Pricing Information is not Available"
        else:# The file contains the pricing details
            with open(filename, "r") as f:
                pricing_data = f.readline()

        message.setText(pricing_data)
        # message.setInformativeText("Do you want to do something about it")
        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)

        # Show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
        else:
            print("User chose unknown button")

    def edit_settings_action_triggered(self):
        print("Edit Query Settings")
        dialog = EditQuerySettingsDialog()
        dialog.exec()

    def edit_settings_action_triggered(self):
        print("Edit Query Settings")
        dialog = EditQuerySettingsDialog()
        dialog.exec()



    # History Actions
    def show_history_action_clicked(self):
        print("Show History Action clicked")
        message = QMessageBox()
        message.setMinimumSize(700, 300)
        message.setWindowTitle("Chat History")

        # storage = StorageHistory()
        # history_list = storage.get_history()
        # history_list.reverse()
        # history_string = json.dumps(history_list, indent=4)

        # message.setText(f"This is the chat history {history_string}")
        message.setText(f"This is the chat history ")
        message.setInformativeText("Do you want to do something about it")
        # message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok)
        message.setDefaultButton(QMessageBox.Ok)

        # Show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
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
