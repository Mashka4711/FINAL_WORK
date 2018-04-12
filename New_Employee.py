from PyQt4 import QtCore, QtGui
from Common_odj import Common


class Wind(Common):
    def __init__(self, parent=None):
        super(Wind, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)

        butt_hide = QtGui.QPushButton('Закрыть модальное окно')
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(butt_hide)
        self.setLayout(vbox)
        butt_hide.clicked.connect(self.close)

    def contain(self):
        wid = QtGui.QWidget(self)
        wid.setMaximumSize(1000, 700)
        self.setCentralWidget(wid)

        lab_name = QtGui.QLabel('  Имя:  ')
        lab_name.setObjectName('lab_name')
        lab_surname = QtGui.QLabel('  Фамилия:  ')
        lab_surname.setObjectName('lab_surname')
        lab_patr = QtGui.QLabel('  Отчество:  ')
        lab_patr.setObjectName('lab_patr')
        lab_post = QtGui.QLabel('  Должность:  ')
        lab_post.setObjectName('lab_post')
        lab_right = QtGui.QLabel('  Права:  ')
        lab_right.setObjectName('lab_right')



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = Wind()
    window_main.show()
    sys.exit(app.exec_())