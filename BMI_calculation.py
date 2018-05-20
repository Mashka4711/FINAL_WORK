from PyQt4 import QtCore, QtGui
from Common_odj import Common
import db_file
from New_dossier import NewDossier


class BMI(Common):
    def __init__(self, id_emp, parent=None):
        super(BMI, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setFixedSize(800, 500)

        self.calculate = QtGui.QPushButton(' Рассчитать ')
        self.write = QtGui.QPushButton('  Записать в базу  ')
        self.new_dossier = QtGui.QPushButton('  Новое дело  ')
        self.rw_weight = QtGui.QLineEdit()
        self.rw_height = QtGui.QLineEdit()
        self.lab_result_text = QtGui.QLabel()
        self.result_bmi = QtGui.QLabel()
        self.dossier_choice = QtGui.QComboBox()
        self.bmi = float
        self.write.setEnabled(False)
        self.category = 'Определение ИМТ'

        self.calculate.clicked.connect(self.invalid_input)
        self.new_dossier.clicked.connect(self.open_win_for_new_dossier)
        self.write.clicked.connect(lambda: self.save_new_data(id_emp))

        self.contain()

    # Содержимое формы

    def contain(self):
        lab_title = QtGui.QLabel('Расчет индекса массы тела')
        lab_title.setObjectName('lab_title')
        lab_weight = QtGui.QLabel('Масса тела, кг: ')
        lab_weight.setObjectName('lab_weight')
        lab_height = QtGui.QLabel('Рост, см: ')
        lab_height.setObjectName('lab_height')
        self.calculate.setObjectName('calculate')
        self.new_dossier.setObjectName('new_dossier')
        self.write.setObjectName('write')
        lab_result = QtGui.QLabel('Результаты')
        lab_result.setObjectName('lab_result')
        lab_dossier = QtGui.QLabel('Выберите дело: ')
        lab_dossier.setObjectName('lab_dossier')
        self.result_bmi.setObjectName('result_bmi')
        self.lab_result_text.setObjectName('result_text')

        # Левая часть
        grid_left = QtGui.QGridLayout()
        grid_left.addWidget(lab_weight, 0, 0)
        grid_left.addWidget(self.rw_weight, 0, 1)
        grid_left.addWidget(lab_height, 1, 0)
        grid_left.addWidget(self.rw_height, 1, 1)
        grid_left.addWidget(self.calculate, 2, 0)

        frame_left = QtGui.QFrame()
        frame_left.setMaximumSize(350, 200)
        frame_left.setFrameShape(6)
        frame_left.setLayout(grid_left)

        vertical_left = QtGui.QVBoxLayout()
        vertical_left.addWidget(frame_left)

        # Заголовок
        title_lay = QtGui.QHBoxLayout()
        title_lay.addWidget(lab_title)
        lab_title.setAlignment(QtCore.Qt.AlignCenter)

        # Правая часть
        result_lay = QtGui.QVBoxLayout()
        result_lay.addWidget(lab_result)
        result_lay.addWidget(self.result_bmi)
        result_lay.addWidget(self.lab_result_text)
        self.result_bmi.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_result_text.setAlignment(QtCore.Qt.AlignCenter)

        frame_result = QtGui.QFrame()
        frame_result.setMaximumSize(500, 150)
        frame_result.setFrameShape(6)
        frame_result.setLayout(result_lay)

        self.dossier_choice.addItems(db_file.load_dossier_to_alcohol_combobox())

        dossier_lay = QtGui.QGridLayout()
        dossier_lay.addWidget(lab_dossier, 0, 0, 1, 1)
        dossier_lay.addWidget(self.dossier_choice, 1, 0, 1, 3)
        dossier_lay.addWidget(QtGui.QLabel(''), 2, 1)
        dossier_lay.addWidget(self.new_dossier, 3, 0, 1, 1)

        frame_data = QtGui.QFrame()
        frame_data.setMaximumSize(500, 200)
        frame_data.setFrameShape(6)
        frame_data.setLayout(dossier_lay)

        button_lay = QtGui.QHBoxLayout()
        button_lay.addWidget(self.write)

        frame_button_write = QtGui.QFrame()
        frame_button_write.setMaximumSize(300, 55)
        frame_button_write.setLayout(button_lay)

        vertical_right = QtGui.QVBoxLayout()
        vertical_right.addWidget(frame_data)
        vertical_right.addWidget(frame_result)
        vertical_right.addWidget(frame_button_write)

        horizontal = QtGui.QHBoxLayout()
        horizontal.addLayout(vertical_left)
        horizontal.addLayout(vertical_right)

        vertical_all = QtGui.QVBoxLayout()
        spacer = QtGui.QSpacerItem(0, 30)
        spacer_1 = QtGui.QSpacerItem(0, 30)
        spacer_2 = QtGui.QSpacerItem(0, 30)
        vertical_all.addSpacerItem(spacer)
        vertical_all.addLayout(title_lay, 0)
        vertical_all.addSpacerItem(spacer_1)
        vertical_all.addLayout(horizontal, 1)
        vertical_all.addSpacerItem(spacer_2)

        self.setLayout(vertical_all)
        self.setStyleSheet('QLabel#lab_weight, #lab_height, #lab_result, #result_text,#result_bmi, #lab_dossier'
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

    # Расчет

    def calculation(self):
        coefficient = int(self.rw_height.text()) / 100
        denominator = coefficient ** 2
        self.bmi = round(float(self.rw_weight.text()) / denominator, 1)
        self.result_bmi.setText(str(self.bmi))
        self.result_output()

    # Вывод результата

    def result_output(self):
        if self.bmi < 16.5:
            self.lab_result_text.setText('Выраженный дефицит массы')
        elif (self.bmi >= 16.5) and (self.bmi < 18.49):
            self.lab_result_text.setText('Недостаточная масса тела')
        elif (self.bmi >= 18.5) and (self.bmi < 24.99):
            self.lab_result_text.setText('Норма')
        elif (self.bmi >= 25) and (self.bmi < 29.99):
            self.lab_result_text.setText('Избыточная масса тела')
        elif (self.bmi >= 30) and (self.bmi < 34.99):
            self.lab_result_text.setText('Ожирение первой степени')
        elif (self.bmi >= 35) and (self.bmi < 39.99):
            self.lab_result_text.setText('Ожирение второй степени')
        elif self.bmi >= 40:
            self.lab_result_text.setText('Ожирение третьей степени')

    # Открытие окна создания нового дела

    def open_win_for_new_dossier(self):
        win = NewDossier(self)
        win.show()

    # Отслеживание ввода

    def invalid_input(self):
        if len(self.rw_weight.text()) == 0 or len(self.rw_height.text()) == 0:
            self.warning('Заполните все поля!')
        else:
            if (int(self.rw_weight.text()) > 150) or (int(self.rw_weight.text()) < 40):
                self.warning('Масса должна лежать\nв пределах от 40 до 150 кг')
            elif (int(self.rw_height.text()) > 200) or (int(self.rw_height.text()) < 120):
                self.warning('Рост должен лежать\nв пределах от 120 до 200 см')
            else:
                self.calculation()
                self.write.setEnabled(True)

    # Запись параметров экспертизы в базу

    def save_new_data(self, id_emp):
        db_file.getConnection()
        parse_str = self.dossier_choice.currentText().split('#')
        dossier_num = parse_str[0]
        db_file.save_bmi_calculation(self.get_data(self), self.rw_weight.text(), self.rw_height.text(), self.bmi,
                                     self.lab_result_text.text(), dossier_num, id_emp, self.category)
        self.inform('Данные сохранены!')


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     window_main = BMI(2)
#     window_main.show()
#     sys.exit(app.exec_())
