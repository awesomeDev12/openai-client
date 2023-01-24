from PySide6.QtWidgets import QWidget, QLabel, QTabWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


class EditQuerySettingsWidget(QWidget):
    def __init__(self):
        super().__init__()


        # Text
        widget_text = QWidget()
        label_max_tokens = QLabel("Max Tokens :")
        line_edit_max_tokens = QLineEdit()

        text_layout = QVBoxLayout()
        text_layout.addWidget(label_max_tokens)
        text_layout.addWidget(line_edit_max_tokens)
        widget_text.setLayout(text_layout)

        # Information / Form
        widget_form = QWidget()
        label_full_name = QLabel("Full Name :")
        line_edit_full = QLineEdit()

        form_layout = QHBoxLayout()
        form_layout.addWidget(label_full_name)
        form_layout.addWidget(line_edit_full)
        widget_form.setLayout(form_layout)

        # Buttons
        widget_buttons = QWidget()
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(button1)
        buttons_layout.addWidget(button2)
        buttons_layout.addWidget(button3)
        widget_buttons.setLayout(buttons_layout)

        # Tab widget
        tab_widget = QTabWidget(self)  # self parent is needed here

        # Add tabs
        tab_widget.addTab(widget_text, "Text")
        tab_widget.addTab(widget_form, "Information")
        tab_widget.addTab(widget_buttons, "Buttons")


        widget_layout = QVBoxLayout()
        widget_layout.addWidget(tab_widget)

        self.setLayout(widget_layout)

