from PyQt4 import QtCore, QtGui
from Common_odj import Common
import db_file
from New_dossier import NewDossier


class BioAgeKidneys(Common):
    def __init__(self, id_emp, parent=None):
        super(BioAgeKidneys, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setFixedSize(800, 550)

        self.rw_glomeruli = QtGui.QLineEdit()
        self.rw_arteries = QtGui.QLineEdit()
        self.rw_stroma = QtGui.QLineEdit()
        self.calculate = QtGui.QPushButton(' Рассчитать ')
        self.new_dossier = QtGui.QPushButton('  Новое дело  ')
        self.write = QtGui.QPushButton('  Записать в базу  ')
        self.write.setEnabled(False)
        self.lab_result_text = QtGui.QLabel()
        self.result_age = QtGui.QLabel()
        self.dossier_choice = QtGui.QComboBox()

        self.calculate.clicked.connect(self.invalid_input)
        self.new_dossier.clicked.connect(self.open_win_for_new_dossier)
        self.write.clicked.connect(lambda: self.save_new_data(id_emp))

        self.contain()

    # Содержимое формы

    def contain(self):
        lab_title = QtGui.QLabel('Расчет времени выведения алкоголя из организма')
        lab_title.setObjectName('lab_title')
        lab_glomeruli = QtGui.QLabel('Удельный вес\nнеизмененных клубочков, %: ')
        lab_glomeruli.setObjectName('lab_glomeruli')
        lab_arteries = QtGui.QLabel('Удельный вес\nнеизмененных артерий, %: ')
        lab_arteries.setObjectName('lab_arteries')
        lab_stroma = QtGui.QLabel('Удельный вес\nстромы, %: ')
        lab_stroma.setObjectName('lab_stroma')
        lab_result = QtGui.QLabel('Результаты')
        lab_result.setObjectName('lab_result')
        lab_dossier = QtGui.QLabel('Выберите дело: ')
        lab_dossier.setObjectName('lab_dossier')
        self.lab_result_text.setObjectName('lab_result_text')
        self.result_age.setObjectName('result_age')
        self.calculate.setObjectName('calculate')
        self.write.setObjectName('write')
        self.new_dossier.setObjectName('new_dossier')
        self.dossier_choice.addItems(db_file.load_dossier_to_alcohol_combobox())

        # Левая часть
        title_lay = QtGui.QHBoxLayout()
        title_lay.addWidget(lab_title)
        lab_title.setAlignment(QtCore.Qt.AlignCenter)

        grid_top = QtGui.QGridLayout()
        grid_top.addWidget(lab_glomeruli, 0, 0)
        grid_top.addWidget(self.rw_glomeruli, 0, 1)
        grid_top.addWidget(lab_arteries, 1, 0)
        grid_top.addWidget(self.rw_arteries, 1, 1)
        grid_top.addWidget(lab_stroma, 2, 0)
        grid_top.addWidget(self.rw_stroma, 2, 1)
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
        result_lay.addWidget(self.result_age)
        self.result_age.setAlignment(QtCore.Qt.AlignCenter)

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
        vertical_all.addSpacerItem(spacer)
        vertical_all.addLayout(title_lay, 0)
        vertical_all.addSpacerItem(spacer)
        vertical_all.addLayout(horizontal, 1)
        vertical_all.addSpacerItem(spacer)

        self.setLayout(vertical_all)
        self.setStyleSheet('QLabel#lab_result, #lab_result_text, #lab_glomeruli, #lab_stroma, #lab_arteries,'
                           '#result_age, #lab_dossier {color: white; font-size: 20px; font-family: Proggy}'
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
        if len(self.rw_glomeruli.text()) == 0 or len(self.rw_stroma.text()) == 0 or len(self.rw_arteries.text()) == 0:
            self.warning('Заполните все поля!')
        else:
            if (int(self.rw_glomeruli.text()) > 100) or (int(self.rw_glomeruli.text()) < 0):
                self.warning('Процентное содержание\nдолжно лежать\nв пределах от 0 до 100')
            elif (int(self.rw_arteries.text()) > 100) or (int(self.rw_arteries.text()) < 0):
                self.warning('Процентное содержание\nдолжно лежать\nв пределах от 0 до 100')
            elif (int(self.rw_stroma.text()) > 100) or (int(self.rw_stroma.text()) < 0):
                self.warning('Процентное содержание\nдолжно лежать\nв пределах от 0 до 100')
            else:
                self.calculation()
                self.write.setEnabled(True)

    # Расчет

    def calculation(self):
        first = 0.34 * int(self.rw_glomeruli.text())
        second = 0.15 * int(self.rw_arteries.text())
        third = 0.44 * int(self.rw_stroma.text())
        age = round(50.34 - first - second + third, 2)
        self.result_age.setText(str(age) + ' +- 4.35')
        self.lab_result_text.setText('Биологический возраст составляет\nпримерно:')

    # Открытие окна создания нового дела

    def open_win_for_new_dossier(self):
        win = NewDossier(self)
        win.show()

    # Запись параметров экспертизы в базу

    def save_new_data(self, id_emp):
        db_file.getConnection()
        parse_str = self.dossier_choice.currentText().split('#')
        dossier_num = parse_str[0]
        db_file.save_bio_age(self.get_data(self), self.rw_glomeruli.text(), self.rw_arteries.text(),
                             self.rw_stroma.text(), self.result_age.text(), dossier_num, id_emp)
        self.inform('Данные сохранены!')


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = BioAgeKidneys(2)
    window_main.show()
    sys.exit(app.exec_())
