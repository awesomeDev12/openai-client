from PySide6.QtWidgets import QApplication
from edit_query_settings_ui import EditQuerySettingsWidget
import sys

app = QApplication(sys.argv)
widget = EditQuerySettingsWidget()
widget.show()


app.exec()