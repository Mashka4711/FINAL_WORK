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

        self.contain()


# Смещение окна относительно главного для эффекта каскадного расположения окон

    def center(self):
        offset = 25
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2 + offset, (screen.height() - size.height()) / 2 + offset)

# Содержимое окна

    def contain(self):
        lab_heading = QtGui.QLabel('Справочник: ')
        lab_heading.setObjectName('lab_heading') # может не надо
        lab_search = QtGui.QLabel('Поиск: ')
        lab_search.setObjectName('lab_search')

        self.button_search.setObjectName('button_search')
        self.button_search.setIcon(QtGui.QIcon('png/QampatykB (10).png'))

        search_layout = QtGui.QGridLayout()
        search_layout.addWidget(lab_search, 0, 0)
        search_layout.addWidget(self.rw_input, 0, 1)
        search_layout.addWidget(self.button_search, 0, 2)

        heading_lay = QtGui.QHBoxLayout()
        heading_lay.addWidget(lab_heading)



        search_frame = QtGui.QFrame()
        search_frame.setFrameShape(6)
        search_frame.setLayout(search_layout)
        search_frame.setMaximumSize(500, 200)

        horizontal = QtGui.QHBoxLayout()
        horizontal.addWidget(search_frame)

        vertical = QtGui.QVBoxLayout()

        vertical.addStretch(1)
        vertical.addLayout(heading_lay)
        vertical.addLayout(horizontal)
        vertical.addStretch(2)

        self.setLayout(vertical)

        self.setStyleSheet('QLabel#lab_heading, #lab_search {color: white; font-size: 20px; font-family: Proggy}'
                           'QLineEdit {font-size: 20px}'
                           'QPushButton#button_search {font-size: 20px; font-family: Proggy; border: 2px;'
                           'border-radius: 6px; background-color: white; min-height: 30px;}'
                           'QPushButton#button_search:hover {background-color: #87cefa}')





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = TermList()
    window_main.show()
    sys.exit(app.exec_())