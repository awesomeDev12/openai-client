from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QSizePolicy, QTextBrowser, QLineEdit, QLabel
from PySide6.QtGui import QClipboard
from apicontroller import APIController
from storage import Storage
import json

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.api_controller = APIController()
        self.storage = Storage()
        # font = QtGui.QFont("Arial", 20)
        # self.setWindowTitleFont(font)
        self.setWindowTitle("Open AI client")




        self.setMinimumSize(700, 500)
        self.input_text_edit = QTextEdit()
        self.input_text_edit.setFixedHeight(100)
        # self.input_text_edit.textChanged.connect(self.text_changed)

        self.output_text_edit = QTextEdit()

        self.search_bar = QLineEdit()
        self.history_text_browser = QTextBrowser()

        # connect the search bar to the text browser
        self.search_bar.textChanged.connect(self.history_text_browser.find)
        # self.search_bar.returnPressed.connect(self.history_text_browser.find)
        # self.search_bar.editingFinished.connect(self.history_text_browser.find)

        # Buttons

        clear_input_button = QPushButton("Clear Input")
        clear_input_button.clicked.connect(self.input_text_edit.clear)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_button_clicked)

        clear_all_button = QPushButton("Clear All")
        clear_all_button.clicked.connect(self.clear_all_button_clicked)

        show_history_button = QPushButton("Show History")
        show_history_button.clicked.connect(self.show_history_button_clicked)

        copy_output_button = QPushButton("Copy Output")
        copy_output_button.clicked.connect(self.copy_output_button_clicked)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_button_clicked)

        history_next_button = QPushButton("Next")
        # history_next_button.clicked.connect(self.history_text_browser.find(self.search_bar.text()))
        # history_next_button.clicked.connect(self.history_text_browser.forward)

        history_previous_button = QPushButton("Previous")
        # history_previous_button.clicked.connect(self.history_text_browser.backward)




        # Layout
        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(show_history_button)
        h_layout1.addWidget(clear_input_button)
        h_layout1.addWidget(clear_all_button)
        h_layout1.addWidget(history_previous_button)
        h_layout1.addWidget(history_next_button)
        h_layout1.addWidget(copy_output_button)
        h_layout1.addWidget(save_button)
        h_layout1.addWidget(submit_button)

        v_layout_left = QVBoxLayout()
        v_layout_left.addWidget(self.input_text_edit)
        v_layout_left.addWidget(self.output_text_edit)

        h_layout_search_bar = QHBoxLayout()
        h_layout_search_bar.addWidget(QLabel("Search  :"))
        h_layout_search_bar.addWidget(self.search_bar)

        v_layout_right = QVBoxLayout()
        v_layout_right.addLayout(h_layout_search_bar)
        v_layout_right.addWidget(self.history_text_browser)

        h_layout2 = QHBoxLayout()
        h_layout2.addLayout(v_layout_left)
        h_layout2.addLayout(v_layout_right)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)

        self.setLayout(v_layout)


    def submit_button_clicked(self):
        print("Submit button clicked")
        message = QMessageBox()
        message.setMinimumSize(700, 300)
        message.setWindowTitle("Submit Confirmation")

        message.setText("Do you want to submit this query")
        message.setInformativeText("Click on Ok only if you have verified your query")
        # message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Cancel)

        # Show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
            self.query_submit()
        elif ret == QMessageBox.Cancel:
            print("User chose Cancel")
        else:
            print("User chose unknown button")


    def query_submit(self):
        input_string = self.input_text_edit.toPlainText()
        output_dic = self.api_controller.get_response_string(input_string)
        if output_dic["status"] == True:
            # First two lines provided by the API is empty
            # output_string = output_dic["text"].split("\n", 2)[2]
            output_string = output_dic["text"]
            # New Query added to history
            storage = Storage()
            storage.insert(input_string, output_string)
        else:
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

    def show_history_button_clicked(self):
        print("Show History Button clicked")

        storage = Storage()
        history_list = storage.get_history()
        history_list.reverse()

        history_string = ""
        for i in  range(len(history_list)):
            history_string += "Input : \n" + history_list[i]["input"]+"\n"
            history_string += "Output : " + history_list[i]["output"]+"\n"
            history_string += "DateTIme : \n" + history_list[i]["datetime"]+"\n"

        self.history_text_browser.setPlainText(history_string)
