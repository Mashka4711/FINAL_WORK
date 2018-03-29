from PyQt4 import QtCore, QtGui
import sys
from Main_form import ModalWind


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


class MainWind(QtGui.QMainWindow, Common):
    def __init__(self, parent=None):
        super(MainWind, self).__init__(parent)
        self.menu()
        self.layout = QtGui.QVBoxLayout()
        self.frame_full = QtGui.QFrame()
        self.fr_empty = QtGui.QFrame()
        self.layout_2 = QtGui.QVBoxLayout()
        self.layout_3 = QtGui.QHBoxLayout()
        self.lab_quote = QtGui.QLabel('«Человек может постареть, болезни и возраст '
                                      '\nизменят его лицо и фигуру, '
                                      '\nно пальцевые узоры останутся все теми же»  ')
        self.pic = QtGui.QLabel()
        self.start_contain()

    def start_contain(self):
        wnd = QtGui.QWidget(self)
        wnd.setMaximumSize(1000,700)
        self.setCentralWidget(wnd)
        self.button_legend = QtGui.QPushButton('START', self)
        self.button_legend.setGeometry(10, 10, 60, 35)
        self.lay = QtGui.QVBoxLayout()
        self.lay.addWidget(self.button_legend)
        #self.lay.setAlignment(QtCore.Qt.AlignCenter)
        self.button_legend.clicked.connect(self.show_on)

    def show_on(self):
        self.button_legend.hide()
        self.lay.deleteLater()
        self.contain()

    def contain(self):
        wid = QtGui.QWidget(self)
        wid.setMaximumSize(1000,700)
        self.setCentralWidget(wid)
        self.but_enter = QtGui.QPushButton('Войти', self)
        self.but_enter.clicked.connect(self.on_show)
        #TestWind.butt_hide.clicked.connect(self.on_return) ### my

        lab_login = QtGui.QLabel('  Введите логин:  ')
        lab_login.setObjectName('lab_login')
        lab_pass = QtGui.QLabel('  Введите пароль:  ')
        lab_pass.setObjectName('lab_pass')

        rw_login = QtGui.QLineEdit()
        rw_pass = QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(lab_login, 1, 0)
        grid.addWidget(lab_pass, 2, 0)
        grid.addWidget(rw_login, 1, 1)
        grid.addWidget(rw_pass, 2, 1)
        grid.addWidget(self.but_enter, 3, 1)

        self.frame_full.setFrameShape(6)
        self.frame_full.setLayout(grid)
        self.frame_full.setMaximumSize(450,250)
        self.fr_empty.setMaximumSize(450,250)
        #self.fr_empty.setFrameShape(6) ### my
        self.layout_2.addWidget(self.lab_quote)
        self.layout_2.setStretch(0,1)
        self.layout_2.addWidget(self.frame_full)
        self.layout_2.setStretch(1,3)
        self.layout_2.addWidget(self.fr_empty)
        self.layout_2.setStretch(2,3)

        self.pic.setPixmap(QtGui.QPixmap('icons/5411303_2'))
        #self.layout_2.addLayout(self.layout_3)
        self.layout_3.addLayout(self.layout_2)
        self.layout_3.addWidget(self.pic)

        wid.setLayout(self.layout_3)
        wid.setStyleSheet('QLabel {color: white; font-size: 20px; font-family: Proggy}' 
                          'QLineEdit {font-size: 20px}'
                          'QPushButton {font-size: 20px; font-family: Proggy; border: 2px;'
                          'border-radius: 6px; background-color: white; min-height: 30px;}'
                          'QPushButton:hover {background-color: #87cefa}')

    def on_show(self):
        win = ModalWind(self)
        #self.setCentralWidget(win)
        win.show()
        #win2 = TestWind(self) ### my
        #self.setCentralWidget(win2)
        #win2.show() ### my
        # var = TestWind.butt_hide
        #if (self.fr_empty.isVisible()):
        #    self.fr_empty.hide()
        #else:
        #    self.fr_empty.show()

    def on_return(self):
        self.fr_empty.setFrameShape(6)

    def menu(self):
        ext = QtGui.QAction(QtGui.QIcon('png/QampatykB (75).png'), 'Выйти', self)
        ext.setShortcut('Ctrl+Q')
        ext.setStatusTip('Exit')
        self.connect(ext, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        new_worker = QtGui.QAction(QtGui.QIcon('png/QampatykB (36).png'), 'Добавить сотрудника', self)
        new_worker.setStatusTip('New employee')

        #daughter_1 = QtGui.QAction(u'Дочка 1', self)
        #self.connect(daughter_1, QtCore.SIGNAL('triggered()'), self.on_show)
        menu_bar = self.menuBar()

        file = menu_bar.addMenu('&Меню')
        #file.addAction(daughter_1)
        file.addAction(new_worker)
        file.addAction(ext)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = MainWind()
    window_main.show()
    sys.exit(app.exec_())