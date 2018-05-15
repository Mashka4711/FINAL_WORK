from PyQt4 import QtCore, QtGui
from Common_odj import Common
import db_file
from New_dossier import NewDossier


class BodyWeight(Common):
    def __init__(self, id_emp, parent=None):
        super(BodyWeight, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)

        self.rw_height = QtGui.QLineEdit()
        self.radio_man = QtGui.QRadioButton('мужской')
        self.radio_woman = QtGui.QRadioButton('женский')
        self.rw_thorax = QtGui.QLineEdit()
        self.rw_breech = QtGui.QLineEdit()
        self.rw_leg = QtGui.QLineEdit()
        self.calculate = QtGui.QPushButton(' Рассчитать ')
        self.new_dossier = QtGui.QPushButton('  Новое дело  ')
        self.write = QtGui.QPushButton('  Записать в базу  ')
        self.write.setEnabled(False)
        self.rw_leg.setEnabled(False)
        self.result_weight = QtGui.QLabel()
        self.lab_result_text = QtGui.QLabel()
        self.dossier_choice = QtGui.QComboBox()
        self.k = float
        self.k_breech = float
        self.k_height = float
        self.k_thorax = float
        self.k_leg = float
        self.sex = ''

        self.calculate.clicked.connect(self.invalid_input)
        self.new_dossier.clicked.connect(self.open_win_for_new_dossier)
        self.write.clicked.connect(lambda: self.save_new_data(id_emp))

        self.contain()

    # Содержимое формы

    def contain(self):
        lab_title = QtGui.QLabel('Определение массы тела по метрическим параметрам')
        lab_title.setObjectName('lab_title')
        lab_sex = QtGui.QLabel('Пол: ')
        lab_sex.setObjectName('lab_sex')
        lab_height = QtGui.QLabel('Рост, см: ')
        lab_height.setObjectName('lab_height')
        lab_thorax = QtGui.QLabel('Длина окружности\nгрудной клетки, см:')
        lab_thorax.setObjectName('lab_thorax')
        lab_breech = QtGui.QLabel('Длина окружности\nтаза, см: ')
        lab_breech.setObjectName('lab_breech')
        lab_leg = QtGui.QLabel('Длина окружности\nбедра, см: ')
        lab_leg.setObjectName('lab_leg')
        lab_result = QtGui.QLabel('Результаты')
        lab_result.setObjectName('lab_result')
        lab_dossier = QtGui.QLabel('Выберите дело: ')
        lab_dossier.setObjectName('lab_dossier')
        self.calculate.setObjectName('calculate')
        self.write.setObjectName('write')
        self.new_dossier.setObjectName('new_dossier')
        self.result_weight.setObjectName('result_weight')
        self.lab_result_text.setObjectName('lab_result_text')

        self.radio_man.clicked.connect(lambda: self.coefficients(-128.456, 1.074, 0.355, 0.389, False, 0, 'мужской'))
        self.radio_woman.clicked.connect(lambda: self.coefficients(116.379, 0.675, 0.133, 0.450, True, 0.522, 'женский'))
        self.dossier_choice.addItems(db_file.load_dossier_to_alcohol_combobox())

        # Левая часть
        grid_top = QtGui.QGridLayout()
        grid_top.addWidget(lab_sex, 0, 0)
        grid_top.addWidget(self.radio_man, 0, 1)
        grid_top.addWidget(self.radio_woman, 1, 1)
        grid_top.addWidget(lab_height, 2, 0)
        grid_top.addWidget(self.rw_height, 2, 1)

        grid_bot = QtGui.QGridLayout()
        grid_bot.addWidget(lab_thorax, 0, 0)
        grid_bot.addWidget(self.rw_thorax, 0, 1)
        grid_bot.addWidget(lab_breech, 1, 0)
        grid_bot.addWidget(self.rw_breech, 1, 1)
        grid_bot.addWidget(lab_leg, 2, 0)
        grid_bot.addWidget(self.rw_leg, 2, 1)
        grid_bot.addWidget(self.calculate, 3, 0)

        frame_top = QtGui.QFrame()
        frame_top.setMaximumSize(400, 150)
        frame_top.setLayout(grid_top)

        separator = QtGui.QFrame()
        separator.setFrameStyle(QtGui.QFrame.HLine | QtGui.QFrame.Raised)
        separator.setMaximumSize(400, 3)

        frame_bot = QtGui.QFrame()
        frame_bot.setMaximumSize(400, 250)
        frame_bot.setLayout(grid_bot)

        title_lay = QtGui.QHBoxLayout()
        title_lay.addWidget(lab_title)
        lab_title.setAlignment(QtCore.Qt.AlignCenter)

        vertical_left = QtGui.QVBoxLayout()
        vertical_left.addWidget(frame_top)
        vertical_left.addWidget(separator)
        vertical_left.addWidget(frame_bot)

        # Правая часть
        result_lay = QtGui.QVBoxLayout()
        result_lay.addWidget(lab_result)
        result_lay.addWidget(self.lab_result_text)
        result_lay.addWidget(self.result_weight)
        self.result_weight.setAlignment(QtCore.Qt.AlignCenter)

        frame_result = QtGui.QFrame()
        frame_result.setMaximumSize(400, 150)
        frame_result.setFrameShape(6)
        frame_result.setLayout(result_lay)

        dossier_lay = QtGui.QGridLayout()
        dossier_lay.addWidget(lab_dossier, 0, 0, 1, 1)
        dossier_lay.addWidget(self.dossier_choice, 1, 0, 1, 3)
        dossier_lay.addWidget(QtGui.QLabel(''), 2, 1)
        dossier_lay.addWidget(self.new_dossier, 3, 0, 1, 1)

        frame_data = QtGui.QFrame()
        frame_data.setMaximumSize(400, 200)
        frame_data.setFrameShape(6)
        frame_data.setLayout(dossier_lay)

        button_lay = QtGui.QHBoxLayout()
        button_lay.addWidget(self.write)
        frame_button_write = QtGui.QFrame()
        frame_button_write.setMaximumSize(400, 55)
        frame_button_write.setLayout(button_lay)

        vertical_right = QtGui.QVBoxLayout()
        vertical_right.addWidget(frame_data)
        vertical_right.addWidget(frame_result)
        vertical_right.addWidget(frame_button_write)

        horizontal = QtGui.QHBoxLayout()
        horizontal.addLayout(vertical_left)
        horizontal.addLayout(vertical_right)

        vertical_all = QtGui.QVBoxLayout()
        spacer = QtGui.QSpacerItem(0, 40)
        spacer_1 = QtGui.QSpacerItem(0, 80)
        vertical_all.addSpacerItem(spacer)
        vertical_all.addLayout(title_lay, 0)
        vertical_all.addSpacerItem(spacer)
        vertical_all.addLayout(horizontal, 1)
        vertical_all.addSpacerItem(spacer_1)

        self.setLayout(vertical_all)
        self.setStyleSheet('QLabel#lab_height, #lab_result, #lab_result_text, #lab_thorax, #lab_breech, #lab_leg,'
                           '#lab_sex, #result_weight, #lab_dossier {color: white; font-size: 20px; font-family: Proggy}'
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

    # Назначение коэффициентов

    def coefficients(self, val1, val2, val3, val4, enable, val5, val6):
        self.k = val1
        self.k_thorax = val2
        self.k_breech = val3
        self.k_height = val4
        self.k_leg = val5
        self.rw_leg.setEnabled(enable)
        self.sex = val6

    # Отслеживание ввода

    def invalid_input(self):
        if (len(self.rw_thorax.text()) == 0 or
            len(self.rw_height.text()) == 0 or
            len(self.rw_breech.text()) == 0 or
                (len(self.rw_leg.text()) == 0 and self.radio_woman.isChecked() is True) or
                ((self.radio_man.isChecked() is False) and (self.radio_woman.isChecked() is False))):
            self.warning('Заполните все поля!')
        else:
            if (int(self.rw_height.text()) > 200) or (int(self.rw_height.text()) < 120):
                self.warning('Рост должен лежать\nв пределах от 120 до 200 см')
            else:
                self.calculation()
                self.write.setEnabled(True)

    # Расчет

    def calculation(self):
        leg = float
        if self.radio_woman.isChecked():
            leg = self.k_leg * float(self.rw_leg.text())
        elif self.radio_man.isChecked():
            leg = 0
            self.rw_leg.setText(str(leg))
        thorax = self.k_thorax * float(self.rw_thorax.text())
        breech = self.k_breech * float(self.rw_breech.text())
        height = self.k_height * float(self.rw_height.text())
        weight = round(self.k + thorax + breech + height + leg, 2)
        self.result_weight.setText(str(weight) + ' кг')
        self.result_output()

    # Вывод результата

    def result_output(self):
        text = 'Масса тела составляет примерно:'
        self.lab_result_text.setText(text)

    # Открытие окна создания нового дела

    def open_win_for_new_dossier(self):
        win = NewDossier(self)
        win.show()

    # Запись параметров экспертизы в базу

    def save_new_data(self, id_emp):
        db_file.getConnection()
        parse_str = self.dossier_choice.currentText().split('#')
        dossier_num = parse_str[0]
        db_file.save_body_weight_determination(self.get_data(self), self.rw_height.text(), self.rw_thorax.text(),
                                               self.rw_leg.text(), self.rw_breech.text(), self.sex,
                                               self.result_weight.text(), dossier_num, id_emp)
        self.inform('Данные сохранены!')


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = BodyWeight(2)
    window_main.show()
    sys.exit(app.exec_())