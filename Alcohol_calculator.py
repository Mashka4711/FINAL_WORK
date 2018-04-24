from PyQt4 import QtCore, QtGui
from Common_odj import Common


class Calculator(Common):
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)

        self.radio_man = QtGui.QRadioButton('мужской')
        self.radio_woman = QtGui.QRadioButton('женский')
        self.full = QtGui.QRadioButton('полный')
        self.less = QtGui.QRadioButton('пустой')
        self.weight = QtGui.QLineEdit()
        self.alc_cont = QtGui.QLineEdit()
        self.amount = QtGui.QLineEdit()

        # self.radio_man.toggled.connect(lambda: self.calculation())
        self.contain()
    def center(self):
        offset = 25
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2 + offset, (screen.height() - size.height()) / 2 + offset)

    def contain(self):
        lab_title = QtGui.QLabel('Расчет максимальной концентрации алкоголя в крови человека в промилле (‰)')
        lab_title.setObjectName('lab_title')
        lab_sex = QtGui.QLabel('Пол: ')
        lab_sex.setObjectName('lab_sex')
        lab_weight = QtGui.QLabel('Масса тела, кг: ')
        lab_weight.setObjectName('lab_weight')
        lab_drink = QtGui.QLabel('Напиток: ')
        lab_drink.setObjectName('lab_drink')
        lab_alc_cont = QtGui.QLabel('Содержание\nспирта %: ')
        lab_amount = QtGui.QLabel('Количество\nвыпитого, мл: ')
        lab_fullness = QtGui.QLabel('Наполненность: ')

        grid_top = QtGui.QGridLayout()
        grid_mid = QtGui.QGridLayout()
        grid_bot = QtGui.QGridLayout()

        grid_top.addWidget(lab_sex, 0, 0)
        grid_top.addWidget(lab_weight, 2, 0)
        grid_top.addWidget(self.radio_man, 0, 1)
        grid_top.addWidget(self.radio_woman, 1, 1)
        grid_top.addWidget(self.weight, 2, 1)

        grid_mid.addWidget(lab_drink, 1, 0)
        grid_mid.addWidget(lab_alc_cont, 0, 1)
        grid_mid.addWidget(lab_amount, 0, 2)
        grid_mid.addWidget(self.alc_cont, 1, 1)
        grid_mid.addWidget(self.amount, 1, 2)

        grid_bot.addWidget(lab_fullness, 0, 0)
        grid_bot.addWidget(self.less, 0, 2)
        grid_bot.addWidget(self.full, 0, 3)

        separator = QtGui.QFrame()
        separator.setFrameStyle(QtGui.QFrame.HLine | QtGui.QFrame.Raised)
        separator.setMaximumSize(400, 3)

        separator1 = QtGui.QFrame()
        separator1.setFrameStyle(QtGui.QFrame.HLine | QtGui.QFrame.Raised)
        separator1.setMaximumSize(400, 3)

        frame_top = QtGui.QFrame()
        frame_top.setMaximumSize(400, 200)
        frame_top.setLayout(grid_top)

        frame_mid = QtGui.QFrame()
        frame_mid.setMaximumSize(400, 150)
        frame_mid.setLayout(grid_mid)

        frame_bot = QtGui.QFrame()
        frame_bot.setMaximumSize(400, 100)
        frame_bot.setLayout(grid_bot)

        vertical = QtGui.QVBoxLayout()
        vertical.addWidget(lab_title)
        vertical.addWidget(frame_top)
        vertical.addWidget(separator)
        vertical.addWidget(frame_mid)
        vertical.addWidget(separator1)
        vertical.addWidget(frame_bot)


        self.setLayout(vertical)
        self.setStyleSheet('QLabel {color: white; font-size: 20px; font-family: Proggy}'
                           'QLineEdit {font-size: 20px}'
                           'QRadioButton {color: white; font-size: 20px}'
                           'QPushButton#button_new {font-size: 20px; font-family: Proggy; border: 2px;'
                           'border-radius: 6px; background-color: white; min-height: 30px;}'
                           'QPushButton#button_new:hover {background-color: #87cefa}')

    def calculation(self):
        if self.radio_man.isChecked():
            print('yuhuuu')



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = Calculator()
    window_main.show()
    sys.exit(app.exec_())
