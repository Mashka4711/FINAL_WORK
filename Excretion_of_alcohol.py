from PyQt4 import QtCore, QtGui
from Common_odj import Common
import db_file
from New_dossier import NewDossier


class AlcoholExcretion(Common):
    def __init__(self, id_emp, parent=None):
        super(AlcoholExcretion, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setFixedSize(800, 550)

        self.rw_weight = QtGui.QLineEdit()
        self.rw_amount = QtGui.QLineEdit()
        self.rw_alc_cont = QtGui.QLineEdit()
        self.calculate = QtGui.QPushButton(' Рассчитать ')
        self.new_dossier = QtGui.QPushButton('  Новое дело  ')
        self.write = QtGui.QPushButton('  Записать в базу  ')
        self.write.setEnabled(False)
        self.lab_result_text = QtGui.QLabel()
        self.result_time = QtGui.QLabel()
        self.dossier_choice = QtGui.QComboBox()
        self.category = "Расчет времени выведения алкоголя"

        self.calculate.clicked.connect(self.invalid_input)
        self.new_dossier.clicked.connect(self.open_win_for_new_dossier)
        self.write.clicked.connect(lambda: self.save_new_data(id_emp))

        self.contain()

    # Содержимое формы

    def contain(self):
        lab_title = QtGui.QLabel('Расчет времени выведения алкоголя из организма')
        lab_title.setObjectName('lab_title')
        lab_weight = QtGui.QLabel('Масса, кг: ')
        lab_weight.setObjectName('lab_weight')
        lab_amount = QtGui.QLabel('Количество\nвыпитого, мл: ')
        lab_amount.setObjectName('lab_amount')
        lab_alc_cont = QtGui.QLabel('Содержание\nспирта, %: ')
        lab_alc_cont.setObjectName('lab_alc_cont')
        lab_result = QtGui.QLabel('Результаты')
        lab_result.setObjectName('lab_result')
        lab_dossier = QtGui.QLabel('Выберите дело: ')
        lab_dossier.setObjectName('lab_dossier')
        self.lab_result_text.setObjectName('lab_result_text')
        self.result_time.setObjectName('result_time')
        self.calculate.setObjectName('calculate')
        self.write.setObjectName('write')
        self.new_dossier.setObjectName('new_dossier')
        self.dossier_choice.addItems(db_file.load_dossier_to_alcohol_combobox())

        # Левая часть
        title_lay = QtGui.QHBoxLayout()
        title_lay.addWidget(lab_title)
        lab_title.setAlignment(QtCore.Qt.AlignCenter)

        grid_top = QtGui.QGridLayout()
        grid_top.addWidget(lab_weight, 0, 0)
        grid_top.addWidget(self.rw_weight, 0, 1)
        grid_top.addWidget(lab_amount, 1, 0)
        grid_top.addWidget(self.rw_amount, 1, 1)
        grid_top.addWidget(lab_alc_cont, 2, 0)
        grid_top.addWidget(self.rw_alc_cont, 2, 1)
        grid_top.addWidget(self.calculate, 3, 0)

        frame_left_top = QtGui.QFrame()
        frame_left_top.setMaximumSize(400, 250)
        frame_left_top.setLayout(grid_top)

        vertical_left = QtGui.QVBoxLayout()
        vertical_left.addWidget(frame_left_top)

        # Правая часть
        result_lay = QtGui.QVBoxLayout()
        result_lay.addWidget(lab_result)
        result_lay.addWidget(self.lab_result_text)
        result_lay.addWidget(self.result_time)
        self.result_time.setAlignment(QtCore.Qt.AlignCenter)

        frame_result = QtGui.QFrame()
        frame_result.setMaximumSize(400, 200)
        frame_result.setFrameShape(6)
        frame_result.setLayout(result_lay)

        dossier_lay = QtGui.QGridLayout()
        dossier_lay.addWidget(lab_dossier, 0, 0, 1, 1)
        dossier_lay.addWidget(self.dossier_choice, 1, 0, 1, 3)
        dossier_lay.addWidget(QtGui.QLabel(''), 2, 1)
        dossier_lay.addWidget(self.new_dossier, 3, 0, 1, 1)

        frame_data = QtGui.QFrame()
        frame_data.setMaximumSize(400, 300)
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
        spacer_1 = QtGui.QSpacerItem(0, 40)
        spacer_2 = QtGui.QSpacerItem(0, 40)
        vertical_all.addSpacerItem(spacer)
        vertical_all.addLayout(title_lay, 0)
        vertical_all.addSpacerItem(spacer_1)
        vertical_all.addLayout(horizontal, 1)
        vertical_all.addSpacerItem(spacer_2)

        self.setLayout(vertical_all)
        self.setStyleSheet('QLabel#lab_weight, #lab_result, #lab_result_text, #lab_amount, #lab_alc_cont, #result_time,'
                           '#lab_dossier {color: white; font-size: 20px; font-family: Proggy}'
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

    # Отслеживание ввода

    def invalid_input(self):
        if len(self.rw_weight.text()) == 0 or len(self.rw_amount.text()) == 0 or len(self.rw_alc_cont.text()) == 0:
            self.warning('Заполните все поля!')
        else:
            if (int(self.rw_weight.text()) > 150) or (int(self.rw_weight.text()) < 40):
                self.warning('Масса должна лежать\nв пределах от 40 до 150 кг')
            elif (int(self.rw_amount.text()) > 5000) or (int(self.rw_amount.text()) < 10):
                self.warning('Количество выпитого должно лежать\nв пределах от 10 до 5000 мл')
            else:
                self.calculation()
                self.write.setEnabled(True)

    # Расчет

    def calculation(self):
        pure_alcohol = int(self.rw_alc_cont.text()) / 100
        alcohol = pure_alcohol * int(self.rw_amount.text()) * 0.79
        denominator = int(self.rw_weight.text()) * 0.15
        time = round(alcohol / denominator, 2)
        self.result_time.setText(str(time) + ' часа')
        self.lab_result_text.setText('Cреднее время выведения\nалкоголя из организма:')

    # Открытие окна создания нового дела

    def open_win_for_new_dossier(self):
        win = NewDossier(self)
        win.show()

    # Запись параметров экспертизы в базу

    def save_new_data(self, id_emp):
        db_file.getConnection()
        parse_str = self.dossier_choice.currentText().split('#')
        dossier_num = parse_str[0]
        db_file.save_alcohol_excretion(self.get_data(self), self.rw_weight.text(), self.rw_amount.text(),
                                       self.rw_alc_cont.text(), self.result_time.text(), dossier_num, id_emp,
                                       self.category)
        self.inform('Данные сохранены!')


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     window_main = AlcoholExcretion(2)
#     window_main.show()
#     sys.exit(app.exec_())