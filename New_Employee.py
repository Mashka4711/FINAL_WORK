from PyQt4 import QtCore, QtGui
from Common_odj import Common


class Wind(Common):
    def __init__(self, parent=None):
        super(Wind, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)

        self.rw_name = QtGui.QLineEdit()
        self.rw_surname = QtGui.QLineEdit()
        self.rw_patr = QtGui.QLineEdit()
        self.rw_post = QtGui.QLineEdit()
        self.rw_right = QtGui.QLineEdit()
        self.rw_age = QtGui.QLineEdit()
        self.rw_education = QtGui.QLineEdit()
        self.rw_login_new = QtGui.QLineEdit()
        self.rw_pass_new = QtGui.QLineEdit()
        self.button_new = QtGui.QPushButton('   Добавить   ')

        self.contain()

# Содержимое формы сохранения нового сотрудника

    def contain(self):
        lab_name = QtGui.QLabel(' *  Имя:  ')
        lab_name.setObjectName('lab_name')
        lab_surname = QtGui.QLabel(' *  Фамилия:  ')
        lab_surname.setObjectName('lab_surname')
        lab_patr = QtGui.QLabel('     Отчество:  ')
        lab_patr.setObjectName('lab_patr')
        lab_post = QtGui.QLabel(' *  Должность:  ')
        lab_post.setObjectName('lab_post')
        lab_right = QtGui.QLabel(' *  Права:  ')
        lab_right.setObjectName('lab_right')
        lab_age = QtGui.QLabel('     Возраст:  ')
        lab_age.setObjectName('lab_age')
        lab_education = QtGui.QLabel('     Образование:  ')
        lab_education.setObjectName('lab_education')
        lab_login_new = QtGui.QLabel(' *  Логин:  ')
        lab_login_new.setObjectName('lab_login_new')
        lab_pass_new = QtGui.QLabel(' *  Пароль:  ')
        lab_pass_new.setObjectName('lab_pass_new')

        grid_left = QtGui.QGridLayout()
        grid_left.setSpacing(10)

        grid_right = QtGui.QGridLayout()
        grid_right.setSpacing(10)

        grid_left.addWidget(lab_name, 1, 0)
        grid_left.addWidget(self.rw_name, 1, 1)
        grid_left.addWidget(lab_surname, 2, 0)
        grid_left.addWidget(self.rw_surname, 2, 1)
        grid_left.addWidget(lab_patr, 3, 0)
        grid_left.addWidget(self.rw_patr, 3, 1)
        grid_left.addWidget(lab_age, 4, 0)
        grid_left.addWidget(self.rw_age, 4, 1)
        grid_left.addWidget(lab_education, 5, 0)
        grid_left.addWidget(self.rw_education, 5, 1)

        grid_right.addWidget(lab_post, 1, 0)
        grid_right.addWidget(self.rw_post, 1, 1)
        grid_right.addWidget(lab_right, 2, 0)
        grid_right.addWidget(self.rw_right, 2, 1)
        grid_right.addWidget(lab_login_new, 3, 0)
        grid_right.addWidget(self.rw_login_new, 3, 1)
        grid_right.addWidget(lab_pass_new, 4, 0)
        grid_right.addWidget(self.rw_pass_new, 4, 1)

        frame_left = QtGui.QFrame()
        frame_left.setFrameShape(6)
        frame_left.setLayout(grid_left)
        frame_left.setMaximumSize(450, 500)

        frame_right = QtGui.QFrame()
        frame_right.setFrameShape(6)
        frame_right.setLayout(grid_right)
        frame_right.setMaximumSize(450, 250)

        lab_intro = QtGui.QLabel('Для того, чтобы добавить сотрудника, заполните следующие поля.'
                                 '\nПоля, отмеченные * , обязательны к заполнению!')
        lab_intro.setObjectName('lab_intro')
        self.button_new.clicked.connect(self.save_new_emp)
        self.button_new.setObjectName('button_new')

        layout_button = QtGui.QHBoxLayout()
        layout_button.addStretch(1)
        layout_button.addWidget(self.button_new)
        layout_button.addStretch(1)

        layout_horizontal = QtGui.QHBoxLayout()
        layout_horizontal.addWidget(frame_left)
        layout_horizontal.addWidget(frame_right)

        layout_vertical = QtGui.QVBoxLayout()
        layout_vertical.addStretch(1)
        layout_vertical.addWidget(lab_intro)
        layout_vertical.addStretch(1)
        layout_vertical.addLayout(layout_horizontal)
        layout_vertical.addStretch(2)
        layout_vertical.addLayout(layout_button)
        layout_vertical.addStretch(1)

        self.setLayout(layout_vertical)
        self.setStyleSheet('QLabel#lab_name, #lab_surname, #lab_patr, #lab_age, #lab_post, #lab_education,'
                           '#lab_right, #lab_login_new, #lab_pass_new, #lab_intro'
                           ' {color: white; font-size: 20px; font-family: Proggy}'
                           'QLineEdit {font-size: 20px}'
                           'QPushButton#button_new {font-size: 20px; font-family: Proggy; border: 2px;'
                           'border-radius: 6px; background-color: white; min-height: 30px;}'
                           'QPushButton#button_new:hover {background-color: #87cefa}')

# Обработка кнопки сохранения

    def save_new_emp(self):
        if (len(self.rw_name.text()) == 0 or
                len(self.rw_surname.text()) == 0 or
                len(self.rw_post.text()) == 0 or
                len(self.rw_right.text()) == 0 or
                len(self.rw_login_new.text()) == 0 or
                len(self.rw_pass_new.text()) == 0):
            self.warning()

# Предупреждение

    def warning(self):
        message = QtGui.QMessageBox(self)
        message.setIcon(QtGui.QMessageBox.Warning)
        message.setWindowTitle("Предупреждение")
        message.setText("Заполните все поля со * !")
        message.setStandardButtons(QtGui.QMessageBox.Ok)
        message.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = Wind()
    window_main.show()
    sys.exit(app.exec_())