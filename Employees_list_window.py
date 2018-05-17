from PyQt4 import QtCore, QtGui
from Common_odj import Common
from New_Employee import Wind
import db_file


class EmployeesListWindow(Common):
    def __init__(self, parent=None):
        super(EmployeesListWindow, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)

        self.employees_list = QtGui.QListWidget()

        window_size = self.geometry()
        self.employees_list.setMinimumHeight(0.65 * window_size.height())

        self.button_del = QtGui.QPushButton('   Удалить   ')
        self.button_edit = QtGui.QPushButton('   Изменить   ')

        self.contain()

    # Содержимое формы для отоборажения списка сотрудников

    def contain(self):
        lab_intro = QtGui.QLabel('Список сотрудников лаборатории:')
        lab_intro.setObjectName('lab_intro')

        self.get_data_from_db()

        self.button_del.clicked.connect(self.delete_emp)
        self.button_del.setObjectName('button_del')
        self.button_edit.clicked.connect(self.edit_emp)
        self.button_edit.setObjectName('button_edit')

        layout_button = QtGui.QHBoxLayout()
        layout_button.addStretch(1)
        layout_button.addWidget(self.button_edit)
        layout_button.addWidget(self.button_del)
        layout_button.addStretch(1)

        layout_vertical = QtGui.QVBoxLayout()
        layout_vertical.addStretch(1)
        layout_vertical.addWidget(lab_intro)
        layout_vertical.addStretch(1)
        layout_vertical.addWidget(self.employees_list)
        layout_vertical.addStretch(1)
        layout_vertical.addLayout(layout_button)
        layout_vertical.addStretch(1)

        self.setLayout(layout_vertical)
        self.setStyleSheet('QLabel#lab_name, #lab_surname, #lab_patr, #lab_age, #lab_post, #lab_education,'
                           '#lab_right, #lab_login_new, #lab_pass_new, #lab_intro'
                           ' {color: white; font-size: 20px; font-family: Proggy}'
                           'QLineEdit {font-size: 20px}'
                           'QComboBox {font-size: 20px}'
                           'QPushButton#button_edit, #button_del {font-size: 20px; font-family: Proggy; border: 2px;'
                           'border-radius: 6px; background-color: white; min-height: 30px;}'
                           'QPushButton#button_edit:hover {background-color: #87cefa}'
                           'QPushButton#button_del:hover {background-color: #87cefa}')

    # Получение записей для списка сотрудников из БД

    def get_data_from_db(self):
        db_file.getConnection()
        entries = db_file.load_emp_notes()
        for entry in entries:
            self.make_item(entry)

    # Создание виджета - элемента списка

    def make_item(self, entry):
        label_pic = QtGui.QLabel()
        label_pic.setMaximumSize(100, 90)
        # if entry[8] is None:
        if (entry[8] == '') or (entry[8] is None):
            entry[8] = 'icons/unknown.png'
        label_pic.setPixmap(QtGui.QPixmap(entry[8]))
        label_name = QtGui.QLabel(entry[1])
        label_age = QtGui.QLabel("Возраст: " + entry[2])
        label_education = QtGui.QLabel("Образование: " + entry[3])
        label_post = QtGui.QLabel("Должность: " + entry[4])
        label_rights = QtGui.QLabel("Права: " + entry[5])
        label_login = QtGui.QLabel("Логин: " + entry[6])
        label_pass = QtGui.QLabel("Пароль: " + entry[7])
        label_empty = QtGui.QLabel("")
        label_empty.setMaximumSize(100, 90)

        local_widget_layout = QtGui.QGridLayout()

        local_widget_layout.addWidget(label_pic, 0, 0, 4, 2)
        local_widget_layout.addWidget(label_name, 0, 1, 1, 3)
        local_widget_layout.addWidget(label_age, 0, 3, 1, 1)
        local_widget_layout.addWidget(label_education, 1, 1, 1, 4)
        local_widget_layout.addWidget(label_post, 2, 1, 1, 2)
        local_widget_layout.addWidget(label_login, 2, 3, 1, 2)
        local_widget_layout.addWidget(label_rights, 3, 1, 1, 2)
        local_widget_layout.addWidget(label_pass, 3, 3, 1, 2)

        local_widget = QtGui.QWidget()
        local_widget.setLayout(local_widget_layout)
        local_widget.setStyleSheet('QLabel {font-size: 15px; font-family: Proggy}')

        item = QtGui.QListWidgetItem(self.employees_list)
        item.setBackgroundColor(QtGui.QColor("#bed2f7"))
        item.setForeground(QtGui.QBrush(QtGui.QColor("#bed2f7")))
        item.setSizeHint(local_widget.sizeHint())
        item.setText(str(entry[0]))

        self.employees_list.setItemWidget(item, local_widget)

    # Сообщение о подтверждении действия

    def question(self):
        answer = QtGui.QMessageBox.question(self, 'Сообщение', "Вы точно хотите удалить сотрудника?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if answer == QtGui.QMessageBox.Yes:
            return True

    # Обработка кнопки удаления

    def delete_emp(self):
        db_file.getConnection()
        if self.employees_list.currentItem().isSelected():
            answer = self.question()
            if answer:
                note_id = self.employees_list.currentItem().text()
                db_file.del_emp(note_id)

    # Обработка кнопки редактирования

    def edit_emp(self):
        if self.employees_list.currentItem().isSelected():
            note_id = self.employees_list.currentItem().text()
            win = Wind(1, note_id)
            win.show()


# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     window_main = EmployeesListWindow()
#     window_main.show()
#     sys.exit(app.exec_())