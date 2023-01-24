from PySide6.QtWidgets import QTableWidget

from storagehistory import StorageHistory
class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.fill()
        self.ncols = 3
        # self.setRowCount(10)
        # self.setColumnCount(3)

    def fill(self):
        storage = StorageHistory()
        history_list = storage.get_history()
        self.nrows  = len(history_list)
        self.setRowCount(self.nrows)
        self.setColumnCount(self.ncols)

        for i in range(self.nrows):
            # for col in range(self.ncols)
            self.setItem(i,0,history_list[i]["datatime"])
            self.setItem(i,0,history_list[i]["input"])
            self.setItem(i,0,history_list[i]["output"])





