from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6.QtGui import QClipboard
from apicontroller import APIController
from storage import Storage

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.api_controller = APIController()
        self.storage = Storage()
        # font = QtGui.QFont("Arial", 20)
        # self.setWindowTitleFont(font)
        self.setWindowTitle("Open AI client")




        self.setMinimumSize(1400, 700)
        self.input_text_edit = QTextEdit()
        # self.input_text_edit.textChanged.connect(self.text_changed)

        self.output_text_edit = QTextEdit()

        # Buttons
        # copy_button = QPushButton("Copy")
        # copy_button.clicked.connect(self.input_text_edit.copy)  # Connect to built in QTextEdit slot
        #
        # cut_button = QPushButton("Cut")
        # cut_button.clicked.connect(self.input_text_edit.cut)
        #
        # paste_button = QPushButton("Paste")  # Custom paste not built-in
        # paste_button.clicked.connect(self.paste_button_clicked)

        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.input_text_edit.undo)

        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.input_text_edit.redo)

        clear_button = QPushButton("Clear Input")
        clear_button.clicked.connect(self.input_text_edit.clear)


        clear_all_button = QPushButton("Clear All")
        clear_all_button.clicked.connect(self.clear_all_button_clicked)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_button_clicked)

        # read_button = QPushButton("Read")
        # read_button.clicked.connect(self.read_button_clicked)


        copy_output_button = QPushButton("Copy Output")
        copy_output_button.clicked.connect(self.copy_output_button_clicked)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_button_clicked)


        # Layout
        h_layout1 = QHBoxLayout()
        # h_layout1.addWidget(copy_button)
        # h_layout1.addWidget(cut_button)
        # h_layout1.addWidget(paste_button)
        h_layout1.addWidget(undo_button)
        h_layout1.addWidget(redo_button)
        h_layout1.addWidget(clear_button)
        h_layout1.addWidget(clear_all_button)
        h_layout1.addWidget(save_button)
        h_layout1.addWidget(copy_output_button)
        h_layout1.addWidget(submit_button)
        # h_layout1.addWidget(read_button)

        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(self.input_text_edit)
        h_layout2.addWidget(self.output_text_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)

        self.setLayout(v_layout)

    def current_text_button_clicked(self):
        print("Current Text : ", self.input_text_edit.toPlainText())

    def paste_button_clicked(self):
        self.input_text_edit.paste()

    def submit_button_clicked(self):
        input_string = self.input_text_edit.toPlainText()
        output_dic = self.api_controller.get_response_string(input_string)
        if output_dic["status"] == True:
            # First two lines provided by the API is empty
            output_string = output_dic["text"].split("\n", 2)[2]
        else :
            # If the response status is failure the Print the Error message
            output_string = output_dic["text"]

        self.output_text_edit.clear()
        self.output_text_edit.setPlainText(output_string)

    def copy_output_button_clicked(self):
        output_string = self.output_text_edit.toPlainText()
        clipboard = QClipboard()
        clipboard.setText(output_string)

    def save_button_clicked(self):
        input_string = self.input_text_edit.toPlainText()
        output_string = self.output_text_edit.toPlainText()
        self.storage.insert(input_string,output_string)

    def clear_all_button_clicked(self):
        print("Clear Input and Output Text Boxes")
        self.input_text_edit.clear()
        self.output_text_edit.clear()



    # def read_button_clicked(self):
    #     self.storage.read()
