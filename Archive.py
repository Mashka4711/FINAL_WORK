from PyQt4 import QtCore, QtGui
from Common_odj import Common
import db_file


class Archive(Common):
    def __init__(self, parent=None):
        super(Archive, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.setWindowModality(QtCore.Qt.WindowModal)

        self.expertise_list = QtGui.QListWidget()

        self.describe = QtGui.QLabel("")
        self.describe.setWordWrap(True)
        self.describe.setStyleSheet('font-size: 20px; font-family: Proggy; background-color: #bed2f7;'
                                    'margin-left: 10px; margin-right: 10px; margin-top: 10px; margin-bottom: 10px;')
        self.describe.setMinimumSize(600, 200)
        self.describe.setMaximumSize(1000, 600)

        self.tables = ['expertise_calc', 'alcohol_excretion', 'weight_determination', 'bmi_calc', 'bio_age_kidneys',
                       'dip_plane_calc']
        self.table_names = ['Расчет концентрации алкоголя', 'Расчет времени выведения алкоголя',
                            'Определение массы тела', 'Определение ИМТ', 'Расчет биологического возраста',
                            'Расчет силы удара']
        self.contain()

    # Содержимое формы

    def contain(self):
        lab_intro = QtGui.QLabel('Архив:')
        lab_intro.setObjectName('lab_intro')

        items = db_file.load_archive()
        for item in items:
            parse_item = item.split('#')

            local_widget = QtGui.QLabel(parse_item[1])

            qitem = QtGui.QListWidgetItem(self.expertise_list)
            # qitem.setBackgroundColor(QtGui.QColor("#bed2f7"))
            qitem.setForeground(QtGui.QBrush(QtGui.QColor("#ffffff")))
            # qitem.setText(str(parse_item[0]))
            qitem.setText(str(item))

            self.expertise_list.setItemWidget(qitem, local_widget)

        # self.expertise_list.addItems()
        self.expertise_list.setStyleSheet('font-size: 20px; font-family: Proggy')
        self.expertise_list.setMinimumHeight(350)
        self.expertise_list.itemDoubleClicked.connect(lambda: self.on_qlistwidget_clicked(self.expertise_list.currentRow()))

        vertical = QtGui.QVBoxLayout()
        vertical.addStretch(1)
        vertical.addWidget(lab_intro)
        # vertical.addStretch(1)
        vertical.addWidget(self.expertise_list)
        vertical.addStretch(2)
        vertical.setContentsMargins(100, 0, 100, 0)

        self.setLayout(vertical)
        self.setStyleSheet('QLabel#lab_intro {color: white; font-size: 30px; font-family: Proggy}'
                           'QLineEdit {font-size: 20px}'
                           'QComboBox {font-size: 20px}'
                           'QPushButton#button_edit, #button_del {font-size: 20px; font-family: Proggy; border: 2px;'
                           'border-radius: 6px; background-color: white; min-height: 30px;}'
                           'QPushButton#button_edit:hover {background-color: #87cefa}'
                           'QPushButton#button_del:hover {background-color: #87cefa}'
                           'QListWidget {border: 5px solid #888888}')

    # Обработчик нажатия на пункт списка

    def on_qlistwidget_clicked(self, row):
        parse_str = self.expertise_list.currentItem().text().split(':')
        parse_str_2 = parse_str[0].split('#')
        note_id = parse_str_2[0]
        category = parse_str_2[1]
        table = ""

        if category == self.table_names[0]:
            table = self.tables[0]
        elif category == self.table_names[1]:
            table = self.tables[1]
        elif category == self.table_names[2]:
            table = self.tables[2]
        elif category == self.table_names[3]:
            table = self.tables[3]
        elif category == self.table_names[4]:
            table = self.tables[4]
        elif category == self.table_names[5]:
            table = self.tables[5]

        # self.describe.setText(parse_str_2[1] + " (" + parse_str[1] + " ) - " +
        #                       db_file.load_from_archive(table, note_id))

        points = db_file.load_from_archive(table, note_id)
        if table == self.tables[0]:
            self.describe.setText(parse_str_2[1] + " (" + parse_str[1] + " ) :\n\n" + "Исходные данные:\n" + "Вес: "
                                  + points[5] + " кг" + "\nКоличество выпитого: " + points[1] + " мл    " +
                                  "Содержание спирта: " + points[0] + " %" + "\nКоэффициент редукции: " + points[4] +
                                  "    Дефицит резорбции: " + points[6] + "\n\nРезультаты: " + "\nМаксимальная"
                                                                                               " концентрация: " +
                                  points[3] + " промилле" + "\n" + points[2] + "\n\nРасчеты провел: " + points[7] + " " +
                                  points[8])
        elif table == self.tables[1]:
            self.describe.setText(parse_str_2[1] + " (" + parse_str[1] + " ) :\n\n" + "Исходные данные:\n" + "Вес: "
                                  + points[0] + " кг" + "\nКоличество выпитого: " + points[1] + " мл    " +
                                  "Содержание спирта: " + points[2] + "\n\nРезультаты: " + "\nСреднее время выведения"
                                                                                           " алкоголя из организма: " +
                                  points[3] + "\n\nРасчеты провел: " + points[4] + " " +
                                  points[5])
        elif table == self.tables[2]:
            if points[5] == 'мужской':
                sex = 'нет данных'
            elif points[5] == 'женский':
                sex = points[2]
                self.describe.setText(parse_str_2[1] + " (" + parse_str[1] + " ) :\n\n" + "Исходные данные:\n" +
                                      "Рост: " + points[0] + " см" + "\nДлина окружности грудной клетки: " + points[1] +
                                      " см" + "\nДлина окружности таза: " + points[3] + " см" + "\nДлина окружности "
                                                                                                "бедра: " + sex + " см"
                                      + "\n\nРезультаты: " + "\nМасса тела составляет примерно: " + points[4] +
                                      "\n\nРасчеты провел: " + points[6] + " " + points[7])
        elif table == self.tables[3]:
            self.describe.setText(parse_str_2[1] + " (" + parse_str[1] + " ) :\n\n" + "Исходные данные:\n" + "Вес: "
                                  + points[0] + " кг    " + "Рост: " + points[1] + " см    " + "\n\nРезультаты: " +
                                  "\nИМТ составляет: " + points[2] + "\n" + points[3] + "\n\nРасчеты провел: " +
                                  points[4] + " " + points[5])
        elif table == self.tables[4]:
            self.describe.setText(parse_str_2[1] + " (" + parse_str[1] + " ) :\n\n" + "Исходные данные:\n" +
                                  "Удельный вес неизмененных клубочков: " + points[0] + " %" +
                                  "\nУдельный вес неизмененных артерий: " + points[1] + " %" +
                                  "\nУдельный вес стромы: " + points[2] + " %" + "\n\nРезультаты: " +
                                  "\nБиологиечский возраст составляет примерно: " + points[3] + "\n\nРасчеты провел: " +
                                  points[4] + " " +
                                  points[5])
        elif table == self.tables[5]:
            self.describe.setText(parse_str_2[1] + " (" + parse_str[1] + " ) :\n\n" + "Исходные данные:\n" + "Вес: "
                                  + points[0] + " кг    " + "Рост: " + points[1] + " см" +
                                  "\nКоэффициент восстановления: " + points[2] + "\n\nРезультаты: " + "\n" +
                                  points[3] + " " + points[4] + " Ньютон" + "\n\nРасчеты провел: " + points[5] + " " +
                                  points[6])
        self.describe.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window_main = Archive()
    window_main.show()
    sys.exit(app.exec_())
