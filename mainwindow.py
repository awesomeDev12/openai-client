from PySide6.QtCore import  QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox
import json
from storage import Storage
from widget import Widget
class MainWindow (QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app # declare an app window
        self.setWindowTitle("Custom Main Window")


        # Menubar and menus
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        # Edit menus
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # History
        history_menu = menu_bar.addMenu("History")

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
        settings_menu = menu_bar.addMenu("Setting")
        settings_menu.addAction("Ada")
        settings_menu.addAction("Babbage")
        settings_menu.addAction("Curie")
        settings_menu.addAction("Da Vinci")

        # Other Menus
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Help")



        # Working with Toolbars
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        # Add Quit action to Toolbar
        toolbar.addAction(quit_action)

        # Create our own action
        action1 = QAction("Custom Action 1", self)
        action1.setStatusTip("Status message for Custom Action 1")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("../icons/start-icon.jpg"),"Custom Action 2", self)
        action2.setStatusTip("Status Message for Custom Action 2")
        action2.triggered.connect(self.toolbar_button_click)
        # action2.setCheckable(True)
        toolbar.addAction(action2)

        # Add separator in toolbar
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Separated button"))

        # Working with Status Bar
        self.setStatusBar(QStatusBar(self))

        # Central Widget
        widget = Widget()
        self.setCentralWidget(widget)



    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        print("Custom Action 1 triggered")
        # self.statusBar().showMessage("Message from Custom Action")
        self.statusBar().showMessage("Message from Custom Action",3000)
        # 3000 is the timeout , this paramater is optional



# History Actions
    def show_history_action_clicked(self):
        print("Button-Hard clicked")
        message = QMessageBox()
        message.setMinimumSize(700,300)
        message.setWindowTitle("Chat History")

        storage = Storage()
        history_list = storage.get_history()
        history_list.reverse()
        history_string = json.dumps(history_list, indent=4)

        message.setText(f"This is the chat history {history_string}")
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

        # storage = Storage()
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
            storage = Storage()
            storage.clear_history()
        elif ret == QMessageBox.Cancel:
            print("User chose Cancel")
        else:
            print("User chose unknown button")