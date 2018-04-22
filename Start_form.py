from PyQt4 import QtCore, QtGui
import sys
from Main_form import ModalWind
import db_file
from Layouts import lay_window1
from New_Employee import Wind
from Employees_list_window import EmployeesListWindow
from Common_odj import Common


class MainWind(QtGui.QMainWindow, Common):
    def __init__(self, parent=None):
        super(MainWind, self).__init__(parent)
        self.menu_bar = self.menuBar()
        self.file = self.menu_bar.addMenu('&Меню')
        self.layout = QtGui.QVBoxLayout()
        self.frame_full = QtGui.QFrame()
        self.fr_empty = QtGui.QFrame()
        self.layout_2 = QtGui.QVBoxLayout()
        self.layout_3 = QtGui.QHBoxLayout()
        self.lab_quote = QtGui.QLabel('«Человек может постареть, болезни и возраст '
                                      '\nизменят его лицо и фигуру, '
                                      '\nно пальцевые узоры останутся все теми же»  ')
        self.pic = QtGui.QLabel()

        self.grid_start = QtGui.QGridLayout()
        self.frame_start = QtGui.QFrame()
        self.frame_start_empty = QtGui.QFrame()
        self.vlay_start = QtGui.QVBoxLayout()
        self.hlay_start = QtGui.QHBoxLayout()
        self.button_legend = QtGui.QPushButton('Начать работу', self)
        self.label = QtGui.QLabel('Криминалистическая лаборатория')

        self.rw_login = QtGui.QLineEdit()
        self.rw_pass = QtGui.QLineEdit()

        self.new_worker = QtGui.QAction(QtGui.QIcon('png/QampatykB (36).png'), 'Добавить сотрудника', self)
        self.workers_list = QtGui.QAction(QtGui.QIcon('png/QampatykB (37).png'), 'Список сотрудников', self)

        self.menu()
        self.start_contain()

    def start_contain(self):
        wnd = QtGui.QWidget(self)
        wnd.setMaximumSize(1000,700)
        self.setCentralWidget(wnd)
        self.file.setEnabled(False)

        wnd.setStyleSheet('QLabel {color: white; font-size: 30px; font-family: Proggy}'
                          'QPushButton {font-size: 20px; font-family: Proggy}')

        self.frame_start.setMaximumSize(550, 250)
        self.frame_start.setLayout(self.grid_start)

        self.frame_start_empty.setMaximumSize(8, 7)

        self.hlay_start.addLayout(self.vlay_start)
        self.vlay_start.addWidget(self.frame_start)
        self.vlay_start.addWidget(self.frame_start_empty)
        self.grid_start.addWidget(self.label)
        self.grid_start.addWidget(self.button_legend)

        wnd.setLayout(self.hlay_start)

        self.button_legend.clicked.connect(self.show_on)

    def show_on(self):
        self.button_legend.hide()
        self.vlay_start.deleteLater()
        self.contain()

    def contain(self):
        self.file.setEnabled(True)
        self.new_worker.setEnabled(False)
        self.workers_list.setEnabled(False)

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

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(lab_login, 1, 0)
        grid.addWidget(lab_pass, 2, 0)
        grid.addWidget(self.rw_login, 1, 1)
        grid.addWidget(self.rw_pass, 2, 1)
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
        self.layout_3.addLayout(self.layout_2)
        self.layout_3.addWidget(self.pic)

        wid.setLayout(self.layout_3)
        wid.setStyleSheet('QLabel {color: white; font-size: 20px; font-family: Proggy}' 
                          'QLineEdit {font-size: 20px}'
                          'QPushButton {font-size: 20px; font-family: Proggy; border: 2px;'
                          'border-radius: 6px; background-color: white; min-height: 30px;}'
                          'QPushButton:hover {background-color: #87cefa}')

    def show_dialog(self):
        message = QtGui.QMessageBox(self)
        message.setIcon(QtGui.QMessageBox.Warning)
        message.setWindowTitle("Предупреждение")
        message.setText("Неверный логин или пароль!"
                        "\nПовторите ввод!")
        message.setStandardButtons(QtGui.QMessageBox.Ok)
        message.show()

    def on_show(self):
        db_file.getConnection()  # проверить,работает ли без этой строчки !!!!!!!!!!!!!!
        entry_condition = db_file.entering(self.rw_login.text(), self.rw_pass.text())
        if entry_condition:
            right = db_file.rights_check(self.rw_login.text())
            if right:
                self.new_worker.setEnabled(True)
                self.workers_list.setEnabled(True)
            else:
                self.new_worker.setEnabled(False)
                self.workers_list.setEnabled(False)
            self.layout_3.deleteLater()
            lay_window1(self)
            #win = ModalWind(self)
            # #win.show()
            #self.setCentralWidget(win)
        else:
            self.show_dialog()

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

    def open_new_emp(self):
        win = Wind(self)
        win.show()

    def open_emp_list(self):
        win = EmployeesListWindow(self)
        win.show()

    def menu(self):
        ext = QtGui.QAction(QtGui.QIcon('png/QampatykB (75).png'), 'Закрыть приложение', self)
        ext.setShortcut('Ctrl+Q')
        ext.setStatusTip('Exit')
        self.connect(ext, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.new_worker.setStatusTip('New employee')

        self.connect(self.new_worker, QtCore.SIGNAL('triggered()'), self.open_new_emp)
        self.connect(self.workers_list, QtCore.SIGNAL('triggered()'), self.open_emp_list)

        #daughter_1 = QtGui.QAction(u'Дочка 1', self)
        #self.connect(daughter_1, QtCore.SIGNAL('triggered()'), self.on_show)
        #file.addAction(daughter_1)

        self.file.addAction(self.new_worker)
        self.file.addAction(self.workers_list)
        self.file.addAction(ext)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = MainWind()
    window_main.show()
    sys.exit(app.exec_())