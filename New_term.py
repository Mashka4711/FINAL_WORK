from PyQt4 import QtCore, QtGui
from Common_odj import Common
import db_file


class TermNew(Common):
    def __init__(self, parent=None):
        super(TermNew, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setFixedSize(800, 500)

        self.rw_name = QtGui.QLineEdit()
        self.rw_describe = QtGui.QTextEdit()
        self.button_add = QtGui.QPushButton('  Добавить  ')

        self.contain()

    # Содержимое формы

    def contain(self):
        lab_name = QtGui.QLabel('Термин: ')
        lab_name.setObjectName('lab_name')
        lab_describe = QtGui.QLabel('Описание: ')
        lab_describe.setObjectName('lab_describe')
        self.button_add.setObjectName('but_add')

        self.button_add.clicked.connect(self.save_new_term)

        grid = QtGui.QGridLayout()
        grid.addWidget(lab_name, 0, 0)
        grid.addWidget(lab_describe, 1, 0)
        grid.addWidget(self.rw_name, 0, 1)
        grid.addWidget(self.rw_describe, 1, 1)

        frame = QtGui.QFrame()
        frame.setMaximumSize(500, 300)
        frame.setFrameShape(6)
        frame.setLayout(grid)

        but_lay = QtGui.QHBoxLayout()
        but_lay.addStretch(1)
        but_lay.addWidget(self.button_add)
        but_lay.addStretch(1)

        vertical = QtGui.QVBoxLayout()
        vertical.addWidget(frame)
        # vertical.addLayout(but_lay)

        horizontal = QtGui.QHBoxLayout()
        # horizontal.addStretch(1)
        horizontal.addLayout(vertical)
        # horizontal.addStretch(1)
        result_lay = QtGui.QVBoxLayout()
        result_lay.addLayout(horizontal)
        result_lay.addLayout(but_lay)

        self.setLayout(result_lay)
        self.setStyleSheet('QLabel#lab_name, #lab_describe {color: white; font-size: 20px; font-family: Proggy}'
                           'QLineEdit {font-size: 20px}'
                           'QTextEdit {font-size: 20px}'
                           'QPushButton#but_add {font-size: 20px; font-family: Proggy; border: 2px;'
                           'border-radius: 6px; background-color: white; min-height: 30px;}'
                           'QPushButton#but_add:hover {background-color: #87cefa}'
                           'QComboBox {font-size: 20px}')

    # Запись нового термина в базу

    def save_new_term(self):
        db_file.getConnection()
        name = db_file.term_comparison(self.rw_name.text())
        if len(self.rw_name.text()) == 0 or len(self.rw_describe.toPlainText()) == 0:
            self.warning("Заполните все поля!")
        else:
            if name:
                self.warning("Термин уже существует!")
            else:
                db_file.save_term(self.rw_name.text(), self.rw_describe.toPlainText())
                self.inform('Данные сохранены!')


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     window_main = TermNew()
#     window_main.show()
#     sys.exit(app.exec_())