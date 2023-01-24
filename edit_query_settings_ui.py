from PySide6.QtWidgets import QDialog, QWidget, QLabel, QTabWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QSpinBox, QGroupBox, QRadioButton, QTextEdit
from PySide6.QtCore import QSize

class EditQuerySettingsDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Text
        widget_text = QWidget()
        label_text_engine = QLabel("Engine :")

        # Radio buttons : answers
        group_box_text_engine = QGroupBox("Engine")
        radio_button_text_engine_davinci = QRadioButton("Da Vinci")
        radio_button_text_engine_curie = QRadioButton("Curie")
        radio_button_text_engine_babbage = QRadioButton("Babbage")
        radio_button_text_engine_ada = QRadioButton("Ada")
        radio_button_text_engine_davinci.setChecked(True)

        group_box_text_engine_layout = QVBoxLayout()
        group_box_text_engine_layout.addWidget(radio_button_text_engine_davinci)
        group_box_text_engine_layout.addWidget(radio_button_text_engine_curie)
        group_box_text_engine_layout.addWidget(radio_button_text_engine_babbage)
        group_box_text_engine_layout.addWidget(radio_button_text_engine_ada)
        group_box_text_engine.setLayout(group_box_text_engine_layout)

        # Temperature
        label_text_temperature = QLabel("Temperature :")
        spin_box_text_temperature = QSpinBox()
        spin_box_text_temperature.setRange(0,7)

        # Max Tokens
        label_text_max_tokens = QLabel("Max Tokens :")
        spin_box_text_max_tokens = QSpinBox()
        spin_box_text_max_tokens.setRange(10,500)
        spin_box_text_max_tokens.setSingleStep(20)

        text_engine_layout = QHBoxLayout()
        # text_engine_layout.addWidget(label_text_engine)
        text_engine_layout.addWidget(group_box_text_engine)

        text_temperature_layout = QHBoxLayout()
        text_temperature_layout.addWidget(label_text_temperature)
        text_temperature_layout.addWidget(spin_box_text_temperature)

        text_max_token_layout = QHBoxLayout()
        text_max_token_layout.addWidget(label_text_max_tokens)
        text_max_token_layout.addWidget(spin_box_text_max_tokens)

        # Merge Temperature and MaxTokens
        text_max_token_and_temperature_layout = QVBoxLayout()
        text_max_token_and_temperature_layout.addLayout(text_max_token_layout)
        text_max_token_and_temperature_layout.addLayout(text_temperature_layout)
        # text_max_token_and_temperature_layout.setContentsMargins(10,40,10,10)
        # margin : left, top, right, bottom

        # Layout of Text settings Tab
        text_layout = QVBoxLayout()
        text_layout.addLayout(text_engine_layout)
        text_layout.addLayout(text_max_token_and_temperature_layout)
        widget_text.setLayout(text_layout)


        # text_layout = QGridLayout()
        # text_layout.addLayout(text_engine_layout,0,0,4,3)
        # # starts at row 0, col 0 and takes up 4 rows and 3 columns
        # text_layout.addLayout(text_max_token_and_temperature_layout,0,2,2,1)
        # # starts at row 0, col 2 and takes up 2 rows and 1 columns
        # widget_text.setLayout(text_layout)

        # Authentication
        widget_auth = QWidget()
        label_apikey = QLabel("API key :")
        text_edit_apikey = QTextEdit()

        # Auth Buttons
        button_apikey_save = QPushButton("Save")
        # button_apikey_ok.clicked.connect(self.update_api_key)
        button_apikey_undo = QPushButton("Undo")
        button_apikey_undo.clicked.connect(text_edit_apikey.undo)

        # Merge auth buttons
        auth_buttons_layout = QHBoxLayout()
        auth_buttons_layout.addWidget(button_apikey_undo)
        auth_buttons_layout.addWidget(button_apikey_save)

        # Layout of Auth Tab
        auth_layout = QVBoxLayout()
        auth_layout.addWidget(label_apikey)
        auth_layout.addWidget(text_edit_apikey)
        auth_layout.addLayout(auth_buttons_layout)
        widget_auth.setLayout(auth_layout)

        # # Buttons
        # widget_buttons = QWidget()
        # button1 = QPushButton("Button 1")
        # button2 = QPushButton("Button 2")
        # button3 = QPushButton("Button 3")
        #
        # buttons_layout = QVBoxLayout()
        # buttons_layout.addWidget(button1)
        # buttons_layout.addWidget(button2)
        # buttons_layout.addWidget(button3)
        # widget_buttons.setLayout(buttons_layout)

        # Tab widget
        tab_widget = QTabWidget(self)  # self parent is needed here

        # Add tabs
        tab_widget.addTab(widget_text, "Text")
        # tab_widget.addTab(widget_form, "Information")
        tab_widget.addTab(widget_auth, "API") # Authentication
        # tab_widget.addTab(widget_buttons, "Buttons")


        widget_layout = QVBoxLayout()
        widget_layout.addWidget(tab_widget)

        self.setLayout(widget_layout)

