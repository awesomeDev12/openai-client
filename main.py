from PySide6.QtWidgets import QApplication
from widget import Widget
from mainwindow import MainWindow

import sys

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()
# widget = Widget()
# widget.show()

app.exec()