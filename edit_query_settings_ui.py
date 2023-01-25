from PySide6.QtWidgets import QDialog, QWidget, QLabel, QTabWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout
from PySide6.QtWidgets import QPushButton, QSpinBox, QGroupBox, QRadioButton, QTextEdit, QMessageBox
from PySide6.QtGui import QClipboard
from PySide6.QtGui import QTextOption
from PySide6.QtCore import QSize
from storage_query_settings import StorageQuerySettings
from apicontroller import APIController


class EditQuerySettingsDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Text Tab
        widget_text = QWidget()

        # Radio buttons : answers
        self.group_box_text_engine = QGroupBox("Engine")
        self.radio_button_text_engine_davinci = QRadioButton("Da Vinci")
        self.radio_button_text_engine_davinci.toggled.connect(self.radio_button_text_engine_davinci_toggled)

        self.radio_button_text_engine_curie = QRadioButton("Curie")
        self.radio_button_text_engine_curie.toggled.connect(self.radio_button_text_engine_curie_toggled)

        self.radio_button_text_engine_babbage = QRadioButton("Babbage")
        self.radio_button_text_engine_babbage.toggled.connect(self.radio_button_text_engine_babbage_toggled)

        self.radio_button_text_engine_ada = QRadioButton("Ada")
        self.radio_button_text_engine_ada.toggled.connect(self.radio_button_text_engine_ada_toggled)

        # self.radio_button_text_engine_curie.setChecked(True)

        group_box_text_engine_layout = QVBoxLayout()
        group_box_text_engine_layout.addWidget(self.radio_button_text_engine_davinci)
        group_box_text_engine_layout.addWidget(self.radio_button_text_engine_curie)
        group_box_text_engine_layout.addWidget(self.radio_button_text_engine_babbage)
        group_box_text_engine_layout.addWidget(self.radio_button_text_engine_ada)
        self.group_box_text_engine.setLayout(group_box_text_engine_layout)

        # Temperature
        label_text_temperature = QLabel("Temperature :")
        self.spin_box_text_temperature = QSpinBox()
        self.spin_box_text_temperature.setRange(0, 100)
        self.spin_box_text_temperature.setSingleStep(10)
        # Connect to File
        self.spin_box_text_temperature.valueChanged.connect(self.text_temperature_value_changed)

        # Max Tokens
        label_text_max_tokens = QLabel("Max Tokens :")
        self.spin_box_text_max_tokens = QSpinBox()
        self.spin_box_text_max_tokens.setRange(50, 500)
        # self.spin_box_text_max_tokens.setValue(100)
        self.spin_box_text_max_tokens.setSingleStep(50)
        # Connect to File
        self.spin_box_text_max_tokens.valueChanged.connect(self.text_max_tokens_value_changed)

        text_engine_layout = QHBoxLayout()
        # text_engine_layout.addWidget(label_text_engine)
        text_engine_layout.addWidget(self.group_box_text_engine)

        text_temperature_layout = QHBoxLayout()
        text_temperature_layout.addWidget(label_text_temperature)
        text_temperature_layout.addWidget(self.spin_box_text_temperature)

        text_max_token_layout = QHBoxLayout()
        text_max_token_layout.addWidget(label_text_max_tokens)
        text_max_token_layout.addWidget(self.spin_box_text_max_tokens)

        # Merge Temperature and MaxTokens
        text_max_token_and_temperature_layout = QVBoxLayout()
        text_max_token_and_temperature_layout.addLayout(text_max_token_layout)
        text_max_token_and_temperature_layout.addLayout(text_temperature_layout)

        # Layout of Text settings Tab
        text_layout = QVBoxLayout()
        text_layout.addLayout(text_engine_layout)
        text_layout.addLayout(text_max_token_and_temperature_layout)
        widget_text.setLayout(text_layout)

        # Image
        # Text Tab
        widget_image = QWidget()

        # Radio buttons : answers
        self.group_box_image_engine = QGroupBox("Engine")
        self.radio_button_image_engine_davinci = QRadioButton("Da Vinci")
        self.radio_button_image_engine_davinci.toggled.connect(self.radio_button_image_engine_davinci_toggled)

        self.radio_button_image_engine_curie = QRadioButton("Curie")
        self.radio_button_image_engine_curie.toggled.connect(self.radio_button_image_engine_curie_toggled)

        self.radio_button_image_engine_babbage = QRadioButton("Babbage")
        self.radio_button_image_engine_babbage.toggled.connect(self.radio_button_image_engine_babbage_toggled)

        self.radio_button_image_engine_ada = QRadioButton("Ada")
        self.radio_button_image_engine_ada.toggled.connect(self.radio_button_image_engine_ada_toggled)

        # self.radio_button_image_engine_curie.setChecked(True)

        group_box_image_engine_layout = QVBoxLayout()
        group_box_image_engine_layout.addWidget(self.radio_button_image_engine_davinci)
        group_box_image_engine_layout.addWidget(self.radio_button_image_engine_curie)
        group_box_image_engine_layout.addWidget(self.radio_button_image_engine_babbage)
        group_box_image_engine_layout.addWidget(self.radio_button_image_engine_ada)
        self.group_box_image_engine.setLayout(group_box_image_engine_layout)

        # Temperature
        label_image_temperature = QLabel("Temperature :")
        self.spin_box_image_temperature = QSpinBox()
        self.spin_box_image_temperature.setRange(0, 100)
        self.spin_box_image_temperature.setSingleStep(10)
        # Connect to File
        self.spin_box_image_temperature.valueChanged.connect(self.image_temperature_value_changed)

        # Max Tokens
        label_image_max_tokens = QLabel("Max Tokens :")
        self.spin_box_image_max_tokens = QSpinBox()
        self.spin_box_image_max_tokens.setRange(50, 500)
        # self.spin_box_image_max_tokens.setValue(100)
        self.spin_box_image_max_tokens.setSingleStep(50)
        # Connect to File
        self.spin_box_image_max_tokens.valueChanged.connect(self.image_max_tokens_value_changed)

        image_engine_layout = QHBoxLayout()
        # image_engine_layout.addWidget(label_image_engine)
        image_engine_layout.addWidget(self.group_box_image_engine)

        image_temperature_layout = QHBoxLayout()
        image_temperature_layout.addWidget(label_image_temperature)
        image_temperature_layout.addWidget(self.spin_box_image_temperature)

        image_max_token_layout = QHBoxLayout()
        image_max_token_layout.addWidget(label_image_max_tokens)
        image_max_token_layout.addWidget(self.spin_box_image_max_tokens)

        # Merge Temperature and MaxTokens
        image_max_token_and_temperature_layout = QVBoxLayout()
        image_max_token_and_temperature_layout.addLayout(image_max_token_layout)
        image_max_token_and_temperature_layout.addLayout(image_temperature_layout)

        # Layout of Text settings Tab
        image_layout = QVBoxLayout()
        image_layout.addLayout(image_engine_layout)
        image_layout.addLayout(image_max_token_and_temperature_layout)
        widget_image.setLayout(image_layout)


        # Authentication
        widget_auth = QWidget()
        label_apikey = QLabel("API key :")
        self.text_edit_apikey = QTextEdit()
        self.text_edit_apikey.setStyleSheet("font-size: 16pt; font-family : monospace;")
        # self.text_edit_apikey.setFontFamily("monospace")
        # self.text_edit_apikey.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
        self.text_edit_apikey.setLineWrapMode(QTextEdit.LineWrapMode.FixedColumnWidth)
        self.text_edit_apikey.setLineWrapColumnOrWidth(20)
        # self.text_edit_apikey.setWordWrapMode(QTextOption.NoWrap)
        # self.text_edit_apikey.setLineWrapMode(QTextEdit.LineWrapMode.WordWrap)
        # self.text_edit_apikey.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        # self.text_edit_apikey.setMaxLength(50)

        # Auth Buttons
        button_apikey_undo = QPushButton("Undo")
        button_apikey_undo.clicked.connect(self.text_edit_apikey.undo)
        button_apikey_paste = QPushButton("Paste")
        button_apikey_paste.clicked.connect(self.text_edit_apikey.paste)
        button_apikey_save = QPushButton("Save")
        button_apikey_save.clicked.connect(self.text_edit_apikey_save)

        # Merge auth buttons
        auth_buttons_layout = QHBoxLayout()
        auth_buttons_layout.addWidget(button_apikey_undo)
        auth_buttons_layout.addWidget(button_apikey_paste)
        auth_buttons_layout.addWidget(button_apikey_save)

        # Layout of Auth Tab
        auth_layout = QVBoxLayout()
        auth_layout.addWidget(label_apikey)
        auth_layout.addWidget(self.text_edit_apikey)
        auth_layout.addLayout(auth_buttons_layout)
        widget_auth.setLayout(auth_layout)

        # Tab widget
        tab_widget = QTabWidget(self)  # self parent is needed here

        # Add tabs
        tab_widget.addTab(widget_text, "Text")
        tab_widget.addTab(widget_image,"Image")
        # tab_widget.addTab(widget_form, "Information")
        tab_widget.addTab(widget_auth, "API")  # Authentication
        # tab_widget.addTab(widget_buttons, "Buttons")

        # Confirmation Buttons
        # self.button_cancel_changes = QPushButton("Cancel")
        # self.button_save_changes = QPushButton("Save")

        # Layout Confirmation Button
        # confirm_button_layout = QHBoxLayout()
        # confirm_button_layout.addWidget(self.button_cancel_changes)
        # confirm_button_layout.addWidget(self.button_save_changes)

        widget_layout = QVBoxLayout()
        widget_layout.addWidget(tab_widget)
        # widget_layout.addLayout(confirm_button_layout)

        self.setLayout(widget_layout)

        # Load values
        self.load_init()

    def text_edit_apikey_paste(self):
        print("Clipboard content Pasted to QTextEdit APIkey")
        self.text_edit_apikey.clear()
        clipboard = QClipboard()
        clipboard_content = clipboard.text()
        self.text_edit_apikey.setPlainText(clipboard_content)
        self.text_edit_apikey.setStyleSheet("font-size: 16pt; font-family : monospace;")
        # self.text_edit_apikey.setFontFamily("monospace")

    # Functions
    def text_edit_apikey_save(self):
        print("API KEY SAVE Button Clicked")
        message = QMessageBox()
        message.setMinimumSize(700, 300)
        message.setWindowTitle("Save API key")
        message.setText("Do you want to set a new API key")
        message.setInformativeText("Think Carefully Then Decide")
        message.setIcon(QMessageBox.Question)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Cancel)

        # Show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
            api_controller = APIController()
            api_controller.set_apikey(self.text_edit_apikey.toPlainText())
        elif ret == QMessageBox.Cancel:
            print("User chose Cancel")
        else:
            print("User chose unknown button")

    def load_init(self):
        storage = StorageQuerySettings()

        # Load Text settings
        settings_text_dic = storage.get_text_settings()

        if settings_text_dic["model"] == "text-davinci-003":
            self.radio_button_text_engine_davinci.setChecked(True)
        elif settings_text_dic["model"] == "text-curie-001":
            self.radio_button_text_engine_curie.setChecked(True)
        elif settings_text_dic["model"] == "text-babbage-001":
            self.radio_button_text_engine_babbage.setChecked(True)
        elif settings_text_dic["model"] == "text-ada-001":
            self.radio_button_text_engine_ada.setChecked(True)

        self.spin_box_text_temperature.setValue(
            settings_text_dic["temperature"] * 100)  # as Temperature is always b/w 0 and 1
        self.spin_box_text_max_tokens.setValue(settings_text_dic["max_tokens"])

        # Load Image settings
        settings_image_dic = storage.get_image_settings()

        if settings_image_dic["model"] == "image-davinci-003":
            self.radio_button_image_engine_davinci.setChecked(True)
        elif settings_image_dic["model"] == "image-curie-001":
            self.radio_button_image_engine_curie.setChecked(True)
        elif settings_image_dic["model"] == "image-babbage-001":
            self.radio_button_image_engine_babbage.setChecked(True)
        elif settings_image_dic["model"] == "image-ada-001":
            self.radio_button_image_engine_ada.setChecked(True)

        self.spin_box_image_temperature.setValue(
            settings_image_dic["temperature"] * 100)  # as Temperature is always b/w 0 and 1
        self.spin_box_image_max_tokens.setValue(settings_image_dic["max_tokens"])


        # Load API key
        api_controller = APIController()
        self.text_edit_apikey.setPlainText(api_controller.get_apikey())


    # Text Functions
    def text_max_tokens_value_changed(self):
        new_value = self.spin_box_text_max_tokens.value()
        print("Text Max tokens new value : ", new_value)
        storage = StorageQuerySettings()
        settings_dic = storage.get_text_settings()
        settings_dic["max_tokens"] = new_value
        storage.set_text_settings(settings_dic)

    def text_temperature_value_changed(self):
        new_value = (self.spin_box_text_temperature.value()) / 100  # Temperature is between 0 and 1
        print("Text Temperature new value : ", new_value)
        storage = StorageQuerySettings()
        settings_dic = storage.get_text_settings()
        settings_dic["temperature"] = new_value
        storage.set_text_settings(settings_dic)

    def radio_button_text_engine_davinci_toggled(self, checked):
        if (checked):
            print("Radio Button Text Engine - Davinci : CHECKED")
            storage = StorageQuerySettings()
            settings_dic = storage.get_text_settings()
            settings_dic["model"] = "text-davinci-003"
            storage.set_text_settings(settings_dic)
        else:
            print("Radio Button Text Engine - Davinci : UNCHECKED")

    def radio_button_text_engine_curie_toggled(self, checked):
        if (checked):
            print("Radio Button Text Engine - Curie : CHECKED")
            storage = StorageQuerySettings()
            settings_dic = storage.get_text_settings()
            settings_dic["model"] = "text-curie-001"
            storage.set_text_settings(settings_dic)
        else:
            print("Radio Button Text Engine - Curie : UNCHECKED")

    def radio_button_text_engine_babbage_toggled(self, checked):
        if (checked):
            print("Radio Button Text Engine - Babbage : CHECKED")
            storage = StorageQuerySettings()
            settings_dic = storage.get_text_settings()
            settings_dic["model"] = "text-babbage-001"
            storage.set_text_settings(settings_dic)
        else:
            print("Radio Button Text Engine - Babbage : UNCHECKED")

    def radio_button_text_engine_ada_toggled(self, checked):
        if (checked):
            print("Radio Button Text Engine - Ada : CHECKED")
            storage = StorageQuerySettings()
            settings_dic = storage.get_text_settings()
            settings_dic["model"] = "text-ada-001"
            storage.set_text_settings(settings_dic)
        else:
            print("Radio Button Text Engine - Ada : UNCHECKED")


    # Image functions
    def image_max_tokens_value_changed(self):
        new_value = self.spin_box_image_max_tokens.value()
        print("Image Max tokens new value : ", new_value)
        storage = StorageQuerySettings()
        settings_dic = storage.get_image_settings()
        settings_dic["max_tokens"] = new_value
        storage.set_image_settings(settings_dic)

    def image_temperature_value_changed(self):
        new_value = (self.spin_box_image_temperature.value()) / 100  # Temperature is between 0 and 1
        print("Image Temperature new value : ", new_value)
        storage = StorageQuerySettings()
        settings_dic = storage.get_image_settings()
        settings_dic["temperature"] = new_value
        storage.set_image_settings(settings_dic)

    def radio_button_image_engine_davinci_toggled(self, checked):
        if (checked):
            print("Radio Button Image Engine - Davinci : CHECKED")
            storage = StorageQuerySettings()
            settings_dic = storage.get_image_settings()
            settings_dic["model"] = "image-davinci-003"
            storage.set_image_settings(settings_dic)
        else:
            print("Radio Button Image Engine - Davinci : UNCHECKED")

    def radio_button_image_engine_curie_toggled(self, checked):
        if (checked):
            print("Radio Button Image Engine - Curie : CHECKED")
            storage = StorageQuerySettings()
            settings_dic = storage.get_image_settings()
            settings_dic["model"] = "image-curie-001"
            storage.set_image_settings(settings_dic)
        else:
            print("Radio Button Image Engine - Curie : UNCHECKED")

    def radio_button_image_engine_babbage_toggled(self, checked):
        if (checked):
            print("Radio Button Image Engine - Babbage : CHECKED")
            storage = StorageQuerySettings()
            settings_dic = storage.get_image_settings()
            settings_dic["model"] = "image-babbage-001"
            storage.set_image_settings(settings_dic)
        else:
            print("Radio Button Image Engine - Babbage : UNCHECKED")

    def radio_button_image_engine_ada_toggled(self, checked):
        if (checked):
            print("Radio Button Image Engine - Ada : CHECKED")
            storage = StorageQuerySettings()
            settings_dic = storage.get_image_settings()
            settings_dic["model"] = "image-ada-001"
            storage.set_image_settings(settings_dic)
        else:
            print("Radio Button Image Engine - Ada : UNCHECKED")