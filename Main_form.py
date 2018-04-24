from PyQt4 import QtCore, QtGui
import sys


class ModalWind(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ModalWind, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setWindowTitle("Криминалистическая лаборатория")
        self.setFixedSize(1000, 700)

        pal_1 = self.palette()
        pal_1.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                       QtGui.QColor("#1b006b"))
        self.setPalette(pal_1)

        butt_hide = QtGui.QPushButton('Закрыть модальное окно')
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(butt_hide)
        self.setLayout(vbox)
        butt_hide.clicked.connect(self.close)
