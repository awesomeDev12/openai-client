from PySide6.QtWidgets import QDialog, QWidget, QLabel, QTabWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QSpinBox, QGroupBox, QRadioButton, QTextEdit
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
        self.spin_box_text_temperature.setRange(0,100)
        self.spin_box_text_temperature.setSingleStep(10)
        # Connect to File
        self.spin_box_text_temperature.valueChanged.connect(self.text_temperature_value_changed)

        # Max Tokens
        label_text_max_tokens = QLabel("Max Tokens :")
        self.spin_box_text_max_tokens = QSpinBox()
        self.spin_box_text_max_tokens.setRange(50,500)
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

        # Authentication
        widget_auth = QWidget()
        label_apikey = QLabel("API key :")
        self.text_edit_apikey = QTextEdit()
        # self.text_edit_apikey.setEchoMode(QLineEdit.PasswordEchoOnEdit)


        # Auth Buttons
        button_apikey_undo = QPushButton("Undo")
        button_apikey_undo.clicked.connect(self.text_edit_apikey.undo)
        button_apikey_redo = QPushButton("Redo")
        button_apikey_redo.clicked.connect(self.text_edit_apikey.redo)
        button_apikey_save = QPushButton("Save")
        button_apikey_save.clicked.connect(self.text_edit_apikey_save)

        # Merge auth buttons
        auth_buttons_layout = QHBoxLayout()
        auth_buttons_layout.addWidget(button_apikey_undo)
        auth_buttons_layout.addWidget(button_apikey_redo)
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
        # tab_widget.addTab(widget_form, "Information")
        tab_widget.addTab(widget_auth, "API") # Authentication
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


    # Functions
    def text_edit_apikey_save(self):
        print("API KEY SAVED")
        api_controller =  APIController()
        api_controller.set_apikey(self.text_edit_apikey.toPlainText())

    def load_init(self):
        storage = StorageQuerySettings()
        settings_dic = storage.get_settings()

        if settings_dic["model"] == "text-davinci-003" :
            self.radio_button_text_engine_davinci.setChecked(True)
        elif settings_dic["model"] == "text-curie-001":
            self.radio_button_text_engine_curie.setChecked(True)
        elif settings_dic["model"] == "text-babbage-001" :
            self.radio_button_text_engine_babbage.setChecked(True)
        elif settings_dic["model"] == "text-ada-001" :
            self.radio_button_text_engine_ada.setChecked(True)

        self.spin_box_text_temperature.setValue(settings_dic["temperature"] * 100) # as Temperature is always b/w 0 and 1
        self.spin_box_text_max_tokens.setValue(settings_dic["max_tokens"])

        # Load API key
        api_controller = APIController()
        self.text_edit_apikey.setPlainText(api_controller.get_apikey())



    def text_max_tokens_value_changed(self):
        new_value = self.spin_box_text_max_tokens.value()
        print("Text Max tokens new value : ",new_value)
        storage = StorageQuerySettings()
        settings_dic = storage.get_settings()
        settings_dic["max_tokens"] = new_value
        storage.set_settings(settings_dic)

    def text_temperature_value_changed(self):
        new_value = (self.spin_box_text_temperature.value())/100 # Temperature is between 0 and 1
        print("Text Temperature new value : ", new_value)
        storage = StorageQuerySettings()
        settings_dic = storage.get_settings()
        settings_dic["temperature"] = new_value
        storage.set_settings(settings_dic)

    def radio_button_text_engine_davinci_toggled(self,checked):
        if (checked):
            print("Radio Button Text Engine - Davinci : CHECKED")
            storage = StorageQuerySettings()
            settings_dic = storage.get_settings()
            settings_dic["model"] = "text-davinci-003"
            storage.set_settings(settings_dic)
        else:
            print("Radio Button Text Engine - Davinci : UNCHECKED")

    def radio_button_text_engine_curie_toggled(self, checked):
        if (checked):
            print("Radio Button Text Engine - Curie : CHECKED")
            storage = StorageQuerySettings()
            settings_dic = storage.get_settings()
            settings_dic["model"] = "text-curie-001"
            storage.set_settings(settings_dic)
        else:
            print("Radio Button Text Engine - Curie : UNCHECKED")

    def radio_button_text_engine_babbage_toggled(self, checked):
        if (checked):
            print("Radio Button Text Engine - Babbage : CHECKED")
            storage = StorageQuerySettings()
            settings_dic = storage.get_settings()
            settings_dic["model"] = "text-babbage-001"
            storage.set_settings(settings_dic)
        else:
            print("Radio Button Text Engine - Babbage : UNCHECKED")

    def radio_button_text_engine_ada_toggled(self, checked):
        if (checked):
            print("Radio Button Text Engine - Ada : CHECKED")
            storage = StorageQuerySettings()
            settings_dic = storage.get_settings()
            settings_dic["model"] = "text-ada-001"
            storage.set_settings(settings_dic)
        else:
            print("Radio Button Text Engine - Ada : UNCHECKED")