from PyQt4 import QtCore, QtGui
from Common_odj import Common
import db_file
from New_dossier import NewDossier
import cmath


class DipPlane(Common):
    def __init__(self, id_emp, parent=None):
        super(DipPlane, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)

        self.rw_weight = QtGui.QLineEdit()
        self.rw_height = QtGui.QLineEdit()
        self.rw_rigid = QtGui.QRadioButton('Жесткая')
        self.rw_semi_rigid = QtGui.QRadioButton('Полужесткая')
        self.rw_non_rigid = QtGui.QRadioButton('Нежесткая')
        self.calculate = QtGui.QPushButton(' Рассчитать ')
        self.surface = float
        self.write = QtGui.QPushButton('  Записать в базу  ')
        self.write.setEnabled(False)
        self.power = float
        self.lab_result_text = QtGui.QLabel('')
        self.rigidity = ''
        self.result_power = QtGui.QLabel()
        self.new_dossier = QtGui.QPushButton('  Новое дело  ')
        self.dossier_choice = QtGui.QComboBox()
        self.category = "Расчет силы удара"

        self.calculate.clicked.connect(self.invalid_input)
        self.write.clicked.connect(lambda: self.save_new_data(id_emp))
        self.new_dossier.clicked.connect(self.open_win_for_new_dossier)

        self.contain()

    # Содержимое формы

    def contain(self):
        lab_weight = QtGui.QLabel('Масса тела, кг: ')
        lab_weight.setObjectName('lab_weight')
        lab_height = QtGui.QLabel('Рост, см: ')
        lab_height.setObjectName('lab_height')
        lab_surface = QtGui.QLabel('Характер поверхности * :')
        lab_surface.setObjectName('lab_surface')
        lab_title = QtGui.QLabel('Определение силы удара головой при падении человека на плоскости')
        lab_title.setObjectName('lab_title')
        lab_note = QtGui.QLabel('Примечание * :\nжесткая поверхность (бетон, кафель и т.п.)\nполужесткая поверхность'
                                ' (асфальт, дерево и т.п.)\nнежесткая поверхность (линолеум, земля)')
        lab_note.setObjectName('lab_note')
        self.calculate.setObjectName('calculate')
        self.write.setObjectName('write')
        lab_result = QtGui.QLabel('Результаты')
        lab_result.setObjectName('lab_result')
        self.lab_result_text.setObjectName('lab_result_text')
        self.result_power.setObjectName('result_power')
        lab_dossier = QtGui.QLabel('Выберите дело: ')
        lab_dossier.setObjectName('lab_dossier')
        self.new_dossier.setObjectName('new_dossier')

        self.rw_rigid.clicked.connect(lambda: self.coefficient_of_recovery(7.7, 'жесткую'))
        self.rw_semi_rigid.clicked.connect(lambda: self.coefficient_of_recovery(5.6, 'полужесткую'))
        self.rw_non_rigid.clicked.connect(lambda: self.coefficient_of_recovery(1.6, 'нежесткую'))

        horizontal_top = QtGui.QHBoxLayout()
        horizontal_top.addWidget(lab_title)
        lab_title.setAlignment(QtCore.Qt.AlignCenter)

        grid_top = QtGui.QGridLayout()
        grid_bot = QtGui.QGridLayout()

        grid_top.addWidget(lab_weight, 0, 0)
        grid_top.addWidget(lab_height, 1, 0)
        grid_top.addWidget(lab_surface, 2, 0)
        grid_top.addWidget(self.rw_weight, 0, 1)
        grid_top.addWidget(self.rw_height, 1, 1)
        grid_top.addWidget(self.rw_rigid, 2, 1)
        grid_top.addWidget(self.rw_semi_rigid, 3, 1)
        grid_top.addWidget(self.rw_non_rigid, 4, 1)

        grid_bot.addWidget(lab_note, 0, 0)

        grid_button = QtGui.QGridLayout()
        grid_button.addWidget(QtGui.QLabel(''), 0, 0)
        grid_button.addWidget(self.calculate, 1, 0)
        grid_button.addWidget(QtGui.QLabel(''), 1, 1)

        frame_left_top = QtGui.QFrame()
        frame_left_top.setMaximumSize(500, 200)
        frame_left_top.setLayout(grid_top)

        frame_left_bot = QtGui.QFrame()
        frame_left_bot.setMaximumSize(500, 200)
        frame_left_bot.setLayout(grid_bot)

        frame_button = QtGui.QFrame()
        frame_button.setMaximumSize(500,100)
        frame_button.setLayout(grid_button)

        separator = QtGui.QFrame()
        separator.setFrameStyle(QtGui.QFrame.HLine | QtGui.QFrame.Raised)
        separator.setMaximumSize(500, 3)

        vertical_left = QtGui.QVBoxLayout()
        vertical_left.addWidget(frame_left_top)
        vertical_left.addWidget(separator)
        vertical_left.addWidget(frame_left_bot)
        vertical_left.addWidget(frame_button)

        result_lay = QtGui.QVBoxLayout()
        result_lay.addWidget(lab_result)
        result_lay.addWidget(self.lab_result_text)
        result_lay.addWidget(self.result_power)
        self.result_power.setAlignment(QtCore.Qt.AlignCenter)

        frame_result = QtGui.QFrame()
        frame_result.setMaximumSize(400, 300)
        frame_result.setFrameShape(6)
        frame_result.setLayout(result_lay)

        self.dossier_choice.addItems(db_file.load_dossier_to_alcohol_combobox())

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
        spacer = QtGui.QSpacerItem(0, 60)
        spacer_1 = QtGui.QSpacerItem(0, 60)
        spacer_2 = QtGui.QSpacerItem(0, 60)
        vertical_all.addSpacerItem(spacer)
        vertical_all.addLayout(horizontal_top, 0)
        vertical_all.addSpacerItem(spacer_1)
        vertical_all.addLayout(horizontal, 1)
        vertical_all.addSpacerItem(spacer_2)

        self.setLayout(vertical_all)
        self.setStyleSheet('QLabel#lab_weight, #lab_height, #lab_surface, #lab_note, #lab_result, #lab_result_text,'
                           '#result_power, #lab_dossier {color: white; font-size: 20px; font-family: Proggy}'
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

    # Коэффициент восстановления

    def coefficient_of_recovery(self, value, text):
        self.surface = value
        self.rigidity = text

    # Расчет
    #
    def calculation(self):
        first = round(self.surface * float(self.rw_weight.text()))
        second = cmath.sqrt(float(self.rw_height.text()))
        self.power = round(first * second.real)
        self.result_power.setText('\n' + str(self.power) + ' Ньютон')
        self.result_output()

    # Вывод результата

    def result_output(self):
        text = str('Сила удара головой при падении на\n' + str(self.rigidity) + ' плоскость человека' + '\nростом ' +
                   self.rw_height.text() + ' см и массой тела ' + self.rw_weight.text() + ' кг\nсоставляет примерно:')
        self.lab_result_text.setText(text)

    # Отслеживание ввода

    def invalid_input(self):
        if (len(self.rw_weight.text()) == 0 or
                len(self.rw_height.text()) == 0 or
                ((self.rw_rigid.isChecked() is False) and (self.rw_semi_rigid.isChecked() is False) and
                    (self.rw_non_rigid.isChecked() is False))):
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
        db_file.save_dip_plane_calculation(self.get_data(self), self.rw_weight.text(), self.rw_height.text(),
                                           self.surface, dossier_num, id_emp, self.power, self.lab_result_text.text(),
                                           self.category)
        self.inform('Данные сохранены!')

    # Открытие окна создания нового дела

    def open_win_for_new_dossier(self):
        win = NewDossier(self)
        win.show()


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     window_main = DipPlane(2)
#     window_main.show()
#     sys.exit(app.exec_())
