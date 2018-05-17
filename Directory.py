from PyQt4 import QtCore, QtGui
from Common_odj import Common
import db_file


class TermList(Common):
    def __init__(self, parent=None):
        super(TermList, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)

        self.rw_input = QtGui.QLineEdit()
        self.button_search = QtGui.QPushButton(' Искать ')

        self.word_list_w = QtGui.QListWidget()

        self.describe = QtGui.QLabel("")

        self.contain()

# Содержимое окна

    def contain(self):
        lab_search = QtGui.QLabel('Поиск: ')
        lab_search.setObjectName('lab_search')

        self.button_search.setObjectName('button_search')
        self.button_search.setIcon(QtGui.QIcon('png/QampatykB (10).png'))
        self.button_search.clicked.connect(self.run_search)

        search_layout = QtGui.QGridLayout()
        search_layout.addWidget(lab_search, 0, 0)
        search_layout.addWidget(self.rw_input, 0, 1)
        search_layout.addWidget(self.button_search, 0, 2)

        self.word_list_w.addItems(db_file.load_directory(""))
        self.word_list_w.setStyleSheet('font-size: 20px; font-family: Proggy')
        self.word_list_w.setMinimumHeight(350)
        self.word_list_w.itemDoubleClicked.connect(lambda: self.on_qlistwidget_clicked(self.word_list_w.currentRow()))

        search_frame = QtGui.QFrame()
        search_frame.setFrameShape(6)
        search_frame.setLayout(search_layout)
        search_frame.setMaximumSize(500, 200)

        horizontal = QtGui.QHBoxLayout()
        horizontal.addWidget(search_frame)

        vertical = QtGui.QVBoxLayout()

        vertical.addStretch(1)
        vertical.addLayout(horizontal)
        vertical.addStretch(1)
        vertical.addWidget(self.word_list_w)
        vertical.addStretch(2)
        vertical.setContentsMargins(100, 0, 100, 0)

        self.setLayout(vertical)

        self.setStyleSheet('QLabel#lab_heading, #lab_search {color: white; font-size: 20px; font-family: Proggy}'
                           'QLineEdit {font-size: 20px}'
                           'QPushButton#button_search {font-size: 20px; font-family: Proggy; border: 2px;'
                           'border-radius: 6px; background-color: white; min-height: 30px;}'
                           'QListWidget {border: 5px solid #888888}'
                           'QPushButton#button_search:hover {background-color: #87cefa}')

    # Обработчик нажатия на пункт списка

    def on_qlistwidget_clicked(self, row):
        self.describe.setWordWrap(True)
        self.describe.setText(self.word_list_w.currentItem().text() + " - " +
                              db_file.load_description(self.word_list_w.currentItem().text()))
        self.describe.setStyleSheet('font-size: 20px; font-family: Proggy; background-color: #bed2f7;'
                                    'margin-left: 10px; margin-right: 10px; margin-top: 10px; margin-bottom: 10px;')
        self.describe.setMinimumSize(600, 200)
        self.describe.setMaximumSize(600, 200)
        self.describe.show()

    # Поиск по справочнику

    def run_search(self):
        self.word_list_w.clear()
        self.word_list_w.addItems(db_file.load_directory(self.rw_input.text()))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = TermList()
    window_main.show()
    sys.exit(app.exec_())