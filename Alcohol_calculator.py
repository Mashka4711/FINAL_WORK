from PyQt4 import QtCore, QtGui
from Common_odj import Common
import datetime
import db_file
from New_dossier import NewDossier


class Calculator(Common):
    def __init__(self, id_emp, parent=None):
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
        self.sex = float

        self.dossier_choice = QtGui.QComboBox()
        self.deficiency = int
        self.lab_concentration = QtGui.QLabel()
        self.lab_rate = QtGui.QLabel()
        self.concentration = float

        self.calculate = QtGui.QPushButton('  Рассчитать  ')
        self.write = QtGui.QPushButton('  Записать в базу  ')
        self.write.setEnabled(False)
        self.write.clicked.connect(lambda: self.save_new_data(id_emp))
        self.new_dossier = QtGui.QPushButton('  Новое дело  ')
        self.new_dossier.clicked.connect(self.open_win_for_new_dossier)

        self.contain()

    # Содержимое формы калькулятора

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
        lab_alc_cont.setObjectName('lab_alc_cont')
        lab_amount = QtGui.QLabel('Количество\nвыпитого, мл: ')
        lab_amount.setObjectName('lab_amount')
        lab_fullness = QtGui.QLabel('Наполненность: ')
        lab_fullness.setObjectName('lab_fullness')
        self.calculate.setObjectName('calculate')
        self.write.setObjectName('write')
        lab_result = QtGui.QLabel('Результаты')
        lab_result.setObjectName('lab_result')
        lab_res_text = QtGui.QLabel('Максимальная концентрация этанола\nв крови в промилле достигает:')
        lab_res_text.setObjectName('lab_res_text')
        self.lab_concentration.setObjectName('lab_concentration')
        self.lab_rate.setObjectName('lab_rate')
        lab_dossier = QtGui.QLabel('Выберите дело: ')
        lab_dossier.setObjectName('lab_dossier')
        self.new_dossier.setObjectName('new_dossier')

        self.dossier_choice.addItems(db_file.load_dossier_to_alcohol_combobox())

        #lab_title.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)

        self.calculate.clicked.connect(self.invalid_input)
        # self.calculate.clicked.connect(self.get_data)

        self.radio_man.clicked.connect(lambda: self.reduction_ratio(0.7))
        self.radio_woman.clicked.connect(lambda: self.reduction_ratio(0.6))
        self.less.clicked.connect(lambda: self.resorption_def(10))
        self.full.clicked.connect(lambda: self.resorption_def(30))

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
        grid_bot.addWidget(self.calculate)

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

        dossier_lay = QtGui.QGridLayout()
        dossier_lay.addWidget(lab_dossier, 0, 0, 1, 1)
        dossier_lay.addWidget(self.dossier_choice, 1, 0, 1, 3)
        dossier_lay.addWidget(QtGui.QLabel(''), 2, 1)
        dossier_lay.addWidget(self.new_dossier, 3, 0, 1, 1)

        frame_data = QtGui.QFrame()
        frame_data.setMaximumSize(400, 200)
        frame_data.setFrameShape(6)
        frame_data.setLayout(dossier_lay)

        result_lay = QtGui.QVBoxLayout()
        result_lay.addWidget(lab_result)
        result_lay.addWidget(lab_res_text)
        result_lay.addWidget(self.lab_concentration)
        result_lay.addWidget(self.lab_rate)
        self.lab_concentration.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_rate.setAlignment(QtCore.Qt.AlignCenter)

        frame_result = QtGui.QFrame()
        frame_result.setMaximumSize(400, 200)
        frame_result.setFrameShape(6)
        frame_result.setLayout(result_lay)

        button_lay = QtGui.QHBoxLayout()
        button_lay.addWidget(self.write)
        frame_button = QtGui.QFrame()
        frame_button.setMaximumSize(400,55)
        frame_button.setLayout(button_lay)

        vertical_left = QtGui.QVBoxLayout()
        # vertical_left.addWidget(lab_title)
        vertical_left.addWidget(frame_top)
        vertical_left.addWidget(separator)
        vertical_left.addWidget(frame_mid)
        vertical_left.addWidget(separator1)
        vertical_left.addWidget(frame_bot)

        vertical_right = QtGui.QVBoxLayout()
        vertical_right.addWidget(frame_data)
        vertical_right.addWidget(frame_result)
        vertical_right.addWidget(frame_button)

        horizontal = QtGui.QHBoxLayout()
        horizontal.addLayout(vertical_left)
        horizontal.addLayout(vertical_right)

        horiz_top = QtGui.QHBoxLayout()
        horiz_top.addWidget(lab_title)
        lab_title.setAlignment(QtCore.Qt.AlignCenter)

        # horiz_top.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)

        vertical_all = QtGui.QVBoxLayout()
        # vertical_all.addStretch(1)
        vertical_all.addLayout(horiz_top, 0)
        # vertical_all.addStretch(2)
        vertical_all.addLayout(horizontal, 1)
        # vertical_all.addStretch(1)
        spacer = QtGui.QSpacerItem(0, 80)
        vertical_all.addSpacerItem(spacer)

        self.setLayout(vertical_all)
        self.setStyleSheet('QLabel#lab_sex, #lab_drink, #lab_weight, #lab_amount, #lab_alc_cont, #lab_dossier,'
                           '#lab_fullness, #lab_result, #lab_concentration, #lab_res_text, #lab_rate'
                           '{color: white; font-size: 20px; font-family: Proggy}'
                           'QLabel#lab_title {color: white; font-size: 22px; font-family: Proggy}'
                           'QLineEdit {font-size: 20px}'
                           'QLabel#lab_result {text-decoration: underline}'
                           'QRadioButton {color: white; font-size: 20px}'
                           'QPushButton#calculate, #write, #new_dossier'
                           '{font-size: 20px; font-family: Proggy; border: 2px;'
                           'border-radius: 6px; background-color: white; min-height: 30px;}'
                           'QPushButton#calculate:hover {background-color: #87cefa}'
                           'QPushButton#write:hover {background-color: #87cefa}'
                           'QPushButton#new_dossier:hover {background-color: #87cefa}'
                           'QComboBox {font-size: 20px}')

    # Коэффициент редукции

    def reduction_ratio(self, value):
        self.sex = value

    # Отслеживание ввода

    def invalid_input(self):
        if (len(self.weight.text()) == 0 or
                len(self.amount.text()) == 0 or
                len(self.alc_cont.text()) == 0 or
                ((self.radio_man.isChecked() is False) and (self.radio_woman.isChecked() is False)) or
                ((self.full.isChecked() is False) and (self.less.isChecked() is False))):
            self.warning('Заполните все поля!')
        else:
            if (int(self.weight.text()) > 150) or (int(self.weight.text()) < 40):
                self.warning('Масса должна лежать\nв пределах от 40 до 150 кг')
            elif (int(self.amount.text()) > 5000) or (int(self.amount.text()) < 10):
                self.warning('Количество выпитого должно лежать\nв пределах от 10 до 5000 мл')
            else:
                self.calculation()
                self.write.setEnabled(True)

    # Дефицит резорбции

    def resorption_def(self, value):
        self.deficiency = value

    # Рассчет

    def calculation(self):
        denominator = round(self.sex * float(self.weight.text()))
        pure_alcohol = int(self.amount.text()) * int(self.alc_cont.text()) / 100 * 0.79
        deficiency = pure_alcohol / self.deficiency
        numerator = pure_alcohol - deficiency
        self.concentration = round(numerator / denominator, 2)
        self.lab_concentration.setText(str(self.concentration))
        self.rate_choice()

    # Выбор степени опьянения

    def rate_choice(self):
        if self.concentration < 0.5:
            self.lab_rate.setText('Отсутствие влияния алкоголя')
        elif (self.concentration >= 0.5) and (self.concentration < 1.5):
            self.lab_rate.setText('Легкая степень опьянения')
        elif (self.concentration >= 1.5) and (self.concentration < 2.0):
            self.lab_rate.setText('Средняя степень опьянения')
        elif (self.concentration >= 2.0) and (self.concentration < 3.0):
            self.lab_rate.setText('Сильная степень опьянения')
        elif (self.concentration >= 3.0) and (self.concentration < 5.0):
            self.lab_rate.setText('Тяжелое отравление')
        elif self.concentration >= 5.0:
            self.lab_rate.setText('Смертельное отравление')

    # Запись параметров экспертизы в базу

    def save_new_data(self, id_emp):
        db_file.getConnection()
        parse_str = self.dossier_choice.currentText().split('#')
        dossier_num = parse_str[0]
        # print("Номер дела: " + dossier_num)
        db_file.save_alcohol_calculation(self.get_data(self), str(self.sex), self.weight.text(), self.alc_cont.text(),
                                         self.amount.text(), str(self.deficiency), str(self.concentration),
                                         self.lab_rate.text(), dossier_num, id_emp)

    # Открытие окна создания нового дела

    def open_win_for_new_dossier(self):
        win = NewDossier(self)
        win.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = Calculator(2)
    window_main.show()
    sys.exit(app.exec_())

