from PySide6.QtCore import  QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar
from widget import Widget
from menu_bar_main import MenuBarMain
from status_bar_main import StatusBarMain
from toolbar_main import ToolBarMain

class MainWindow (QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app # declare an app window
        self.setWindowTitle("Custom Main Window")

        # Central Widget
        widget = Widget()

        # Working with Status Bar
        status_bar = StatusBarMain()
        self.setStatusBar(status_bar)

        # Menubar and menus
        menu_bar = MenuBarMain(app,widget,status_bar)
        self.setMenuBar(menu_bar)

        # Working with Toolbars
        tool_bar = ToolBarMain(status_bar)
        self.addToolBar(tool_bar)

        # Set Central Widget
        self.setCentralWidget(widget)





