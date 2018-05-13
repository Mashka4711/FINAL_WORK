from PyQt4 import QtCore, QtGui


class Common(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Common, self).__init__(parent)
        self.setFixedSize(1000, 700)
        self.setWindowTitle("Криминалистическая лаборатория")
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowIcon(QtGui.QIcon('icons/icons8-find-user-male-50.png'))
        self.center()
        self.fond()

# Смещение окна относительно главного для эффекта каскадного расположения окон

    def center(self):
        offset = 25
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2 + offset, (screen.height() - size.height()) / 2 + offset)

# Фон

    def fond(self):
        back = self.palette()
        back.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                      QtGui.QBrush(QtGui.QPixmap('icons/ubuntism_ru_abstract_35.png')))
        back.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window,
                      QtGui.QBrush(QtGui.QPixmap('icons/ubuntism_ru_abstract_35.png')))
        self.setPalette(back)

# Предупреждение

    def warning(self, text):
        message = QtGui.QMessageBox(self)
        message.setIcon(QtGui.QMessageBox.Warning)
        message.setWindowTitle("Предупреждение")
        message.setText(text)
        message.setStandardButtons(QtGui.QMessageBox.Ok)
        message.show()

    # Информирование

    def inform(self, text):
        message = QtGui.QMessageBox(self)
        message.setIcon(QtGui.QMessageBox.Information)
        message.setWindowTitle("Информация")
        message.setText(text)
        message.setStandardButtons(QtGui.QMessageBox.Ok)
        message.show()