from PyQt4 import QtCore, QtGui
from Common_odj import Common
import db_file


class NewDossier(Common):
    def __init__(self, parent=None):
        super(NewDossier, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setFixedSize(500, 500)

        self.rw_name = QtGui.QLineEdit()
        self.rw_surname = QtGui.QLineEdit()
        self.rw_birthday = QtGui.QLineEdit()

        self.save_dossier = QtGui.QPushButton(' Сохранить ')
        self.save_dossier.clicked.connect(self.saving_new_dossier)

        self.contain()

    # Содержимое окна

    def contain(self):
        lab_name = QtGui.QLabel(' Имя:   ')
        lab_name.setObjectName('lab_name')
        lab_surname = QtGui.QLabel(' Фамилия:  ')
        lab_surname.setObjectName('lab_surname')
        lab_birthday = QtGui.QLabel(' * Дата рождения: ')
        lab_birthday.setObjectName('lab_birthday')
        lab_note = QtGui.QLabel(' Примечание *\n\n Формат ввода даты: гггг.мм.дд ')
        lab_note.setObjectName('lab_note')
        lab_title = QtGui.QLabel(' Заполните следующие поля: ')
        lab_title.setObjectName('lab_title')

        self.rw_name.setObjectName('rw_name')
        self.rw_surname.setObjectName('rw_surname')
        self.rw_birthday.setObjectName('rw_birthday')
        self.save_dossier.setObjectName('save_dossier')

        frame = QtGui.QFrame()
        frame.setMaximumSize(480, 560)
        frame.setFrameShape(6)

        frame_in = QtGui.QFrame()
        frame_in_down = QtGui.QFrame()
        frame_in.setMaximumSize(460, 500)
        frame_in_down.setMaximumSize(460, 200)

        grid = QtGui.QGridLayout()
        grid_down = QtGui.QGridLayout()
        grid.addWidget(lab_name, 0, 0)
        grid.addWidget(self.rw_name, 0, 1)
        grid.addWidget(lab_surname, 1, 0)
        grid.addWidget(self.rw_surname, 1, 1)
        grid.addWidget(lab_birthday, 2, 0)
        grid.addWidget(self.rw_birthday, 2, 1)

        grid_down.addWidget(lab_note, 0, 0, 1, 3)
        grid_down.addWidget(QtGui.QLabel(''), 1, 0)
        grid_down.addWidget(QtGui.QLabel(''), 2, 0)
        grid_down.addWidget(self.save_dossier, 3, 1, 1, 1)

        frame_in.setLayout(grid)
        frame_in_down.setLayout(grid_down)

        separator = QtGui.QFrame()
        separator.setFrameStyle(QtGui.QFrame.HLine | QtGui.QFrame.Raised)
        separator.setMaximumSize(460, 3)

        vertical = QtGui.QVBoxLayout()
        vertical.addStretch(1)
        vertical.addWidget(lab_title)
        vertical.addStretch(1)
        vertical.addWidget(frame_in)
        vertical.addWidget(separator)
        vertical.addWidget(frame_in_down)
        vertical.addStretch(2)
        frame.setLayout(vertical)

        layout_all = QtGui.QVBoxLayout()
        layout_all.addWidget(frame)

        self.setLayout(layout_all)
        self.setStyleSheet('QLabel#lab_name, #lab_surname, #lab_birthday, #lab_title, #lab_note {color: white;'
                           'font-size: 20px; font-family: Proggy}'
                           'QLineEdit {font-size: 20px}'
                           'QPushButton#save_dossier {font-size: 20px; font-family: Proggy; border: 2px;'
                           'border-radius: 6px; background-color: white; min-height: 30px;}'
                           'QPushButton#save_dossier:hover {background-color: #87cefa}')

    # Сохранение нового дела

    def saving_new_dossier(self):
        if (len(self.rw_name.text()) == 0 or
                len(self.rw_surname.text()) == 0 or
                len(self.rw_birthday.text()) == 0):
            self.warning("Заполните все поля!")
        else:
            parse_date_str = self.rw_birthday.text().split('.')
            date_year = parse_date_str[0]
            if len(date_year) != 4 or len(self.rw_birthday.text()) != 10:
                self.warning("Неправильно введена дата!\nВведите: гггг.мм.дд")
            db_file.getConnection()
            db_file.new_dossier(self.rw_name.text(), self.rw_surname.text(), self.rw_birthday.text())
            self.inform('Дело успешно добавлено!')


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = NewDossier()
    window_main.show()
    sys.exit(app.exec_())