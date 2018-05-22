from PyQt4 import QtCore, QtGui
import db_file
from Main_form import main_window_contain
from New_Employee import Wind
from Employees_list_window import EmployeesListWindow
from Common_odj import Common
from Directory import TermList
from Alcohol_calculator import Calculator
from BMI_calculation import BMI


class MainWind(QtGui.QMainWindow, Common):
    def __init__(self, parent=None):
        super(MainWind, self).__init__(parent)

        self.current_emp_id = int

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
        self.param = True

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
        self.show_directory = QtGui.QAction(QtGui.QIcon('png/QampatykB (48).png'), 'Справочник', self)

        self.menu()
        self.start_contain()

    # Стартовое заполнение

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

    # Открытие формы авторизации

    def show_on(self):
        self.button_legend.hide()
        self.vlay_start.deleteLater()
        self.contain()

    # Содержимое формы авторизации

    def contain(self):
        self.file.setEnabled(True)
        self.new_worker.setEnabled(False)
        self.workers_list.setEnabled(False)

        wid = QtGui.QWidget(self)
        wid.setMaximumSize(1000,700)
        self.setCentralWidget(wid)
        self.but_enter = QtGui.QPushButton('Войти', self)
        self.but_enter.clicked.connect(self.on_show)

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
        self.frame_full.setMaximumSize(450, 250)
        self.fr_empty.setMaximumSize(450, 250)
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

    # Центровка

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    # Открытие основного окна

    def on_show(self):
        db_file.getConnection()
        entry_condition = db_file.entering(self.rw_login.text(), self.rw_pass.text())
        if entry_condition > 0:
            self.current_emp_id = entry_condition
            right = db_file.rights_check(self.rw_login.text())
            if right:
                self.new_worker.setEnabled(True)
                self.workers_list.setEnabled(True)
                self.param = True
            else:
                self.new_worker.setEnabled(False)
                self.workers_list.setEnabled(False)
                self.param = False
            self.layout_3.deleteLater()
            # lay_window1(self)
            main_window_contain(self, self.current_emp_id)
            #win = ModalWind(self)
            # #win.show()
            #self.setCentralWidget(win)
        else:
            self.warning("Неверный логин или пароль!"
                         "\nПовторите ввод!")

    # Открытие окна добавления нового сотрудника

    def open_new_emp(self):
        win = Wind(0, -1)
        win.show()

    # Открытие окна со списком сотрудников

    def open_emp_list(self):
        win = EmployeesListWindow(self)
        win.show()

    # Открытие справочника

    def open_directory(self):
        win = TermList(self.param)
        win.show()

    # Открытие экспертизы 1

    def open_alcohol_calculator(self):
        win = Calculator(self.current_emp_id)
        win.show()

    def open_bmi_calculator(self):
        win = BMI(self.current_emp_id)
        win.show()

    # Описание меню

    def menu(self):
        ext = QtGui.QAction(QtGui.QIcon('png/QampatykB (75).png'), 'Закрыть приложение', self)
        ext.setShortcut('Ctrl+Q')
        ext.setStatusTip('Exit')
        self.connect(ext, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.new_worker.setStatusTip('New employee')

        self.connect(self.new_worker, QtCore.SIGNAL('triggered()'), self.open_new_emp)
        self.connect(self.workers_list, QtCore.SIGNAL('triggered()'), self.open_emp_list)
        self.connect(self.show_directory, QtCore.SIGNAL('triggered()'), self.open_directory)

        #daughter_1 = QtGui.QAction(u'Дочка 1', self)
        #self.connect(daughter_1, QtCore.SIGNAL('triggered()'), self.on_show)
        #file.addAction(daughter_1)

        self.file.addAction(self.new_worker)
        self.file.addAction(self.workers_list)
        self.file.addAction(self.show_directory)
        self.file.addAction(ext)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = MainWind()
    # window_main.show()
    # main_window_contain(window_main, 2)
    window_main.show()
    sys.exit(app.exec_())
