from PyQt4 import QtCore, QtGui


class Common(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Common, self).__init__(parent)
        self.setFixedSize(1000, 700)
        self.setWindowTitle("Криминалистическая лаборатория")
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowIcon(QtGui.QIcon('icons/icons8-find-user-male-50.png'))
        self.center()
        self.fond()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def fond(self):
        back = self.palette()
        back.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                      QtGui.QBrush(QtGui.QPixmap('icons/ubuntism_ru_abstract_35.png')))
        back.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window,
                      QtGui.QBrush(QtGui.QPixmap('icons/ubuntism_ru_abstract_35.png')))
        self.setPalette(back)
