from PyQt4 import QtCore, QtGui
from Common_odj import Common


class Archive(Common):
    def __init__(self, parent=None):
        super(Archive, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)

        self.expertise_list = QtGui.QListWidget()

        self.contain()

    # Содержимое формы

    def contain(self):
        lab_intro = QtGui.QLabel('Список сотрудников лаборатории:')
        lab_intro.setObjectName('lab_intro')

        # self.word_list_w.addItems(db_file.load_directory(""))
        self.expertise_list.setStyleSheet('font-size: 20px; font-family: Proggy')
        self.expertise_list.setMinimumHeight(350)
        self.expertise_list.itemDoubleClicked.connect(lambda: self.on_qlistwidget_clicked(self.word_list_w.currentRow()))

        vertical = QtGui.QVBoxLayout()
        vertical.addStretch(1)
        vertical.addWidget(self.expertise_list)
        vertical.addStretch(2)
        vertical.setContentsMargins(100, 0, 100, 0)

        self.setLayout(vertical)
        self.setStyleSheet('QLabel#lab_name, #lab_surname, #lab_patr, #lab_age, #lab_post, #lab_education,'
                           '#lab_right, #lab_login_new, #lab_pass_new, #lab_intro'
                           ' {color: white; font-size: 20px; font-family: Proggy}'
                           'QLineEdit {font-size: 20px}'
                           'QComboBox {font-size: 20px}'
                           'QPushButton#button_edit, #button_del {font-size: 20px; font-family: Proggy; border: 2px;'
                           'border-radius: 6px; background-color: white; min-height: 30px;}'
                           'QPushButton#button_edit:hover {background-color: #87cefa}'
                           'QPushButton#button_del:hover {background-color: #87cefa}')




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = Archive()
    window_main.show()
    sys.exit(app.exec_())
