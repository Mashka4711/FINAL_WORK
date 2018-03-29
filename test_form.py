from PyQt4 import QtCore, QtGui
#from Start_form import

'''class TestWind(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TestWind, self).__init__(parent)
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

        self.contain()

    #def contain(self):
        #wid = QtGui.QWidget(self)
        #wid.setMaximumSize(1000, 700)
        #self.setCentralWidget(wid)
        #self.but_return = QtGui.QPushButton('Назад', self)
        #self.but_return.clicked.connect(self.on_show)'''