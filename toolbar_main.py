from PySide6.QtWidgets import QToolBar, QPushButton
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize

class ToolBarMain(QToolBar):
    def __init__(self,status_bar):
        super().__init__()

        self.status_bar = status_bar

        self.setIconSize(QSize(16, 16))
        # Add Quit action to Toolbar
        # toolbar.addAction(quit_action)

        # Create our own action
        action1 = QAction("Custom Action 1", self)
        action1.setStatusTip("Status message for Custom Action 1")
        action1.triggered.connect(self.toolbar_button_click)
        self.addAction(action1)

        action2 = QAction(QIcon("../icons/start-icon.jpg"), "Custom Action 2", self)
        action2.setStatusTip("Status Message for Custom Action 2")
        action2.triggered.connect(self.toolbar_button_click)
        # action2.setCheckable(True)
        self.addAction(action2)

        # Add separator in toolbar
        self.addSeparator()
        self.addWidget(QPushButton("Separated button"))

    def toolbar_button_click(self):
            print("Custom Action 1 triggered")
            # self.statusBar().showMessage("Message from Custom Action")
            self.status_bar.showMessage("Message from Custom Action",3000)
            # 3000 is the timeout , this paramater is optional