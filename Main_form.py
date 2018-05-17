from PyQt4 import QtCore, QtGui
import sys
from Common_odj import Common
from Alcohol_calculator import Calculator
from Excretion_of_alcohol import AlcoholExcretion
from Body_weight_determination import BodyWeight
from BMI_calculation import BMI
from Changes_in_the_kidneys import BioAgeKidneys
from Dip_in_the_plane import DipPlane


# class ModalWind(QtGui.QWidget):
#     def __init__(self, parent=None):
#         super(ModalWind, self).__init__(parent)
#         self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
#         self.setWindowModality(QtCore.Qt.WindowModal)
#         self.setWindowTitle("Криминалистическая лаборатория")
#         self.setFixedSize(1000, 700)
#
#         pal_1 = self.palette()
#         pal_1.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
#                        QtGui.QColor("#1b006b"))
#         self.setPalette(pal_1)
#
#         butt_hide = QtGui.QPushButton('Закрыть модальное окно')
#         vbox = QtGui.QVBoxLayout()
#         vbox.addWidget(butt_hide)
#         self.setLayout(vbox)
#         butt_hide.clicked.connect(self.close)


def main_window_contain(wind, id_emp):
    wid = QtGui.QWidget(wind)
    wid.setMaximumSize(1000, 700)
    wind.setCentralWidget(wid)
    pal_1 = wind.palette()
    pal_1.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                   QtGui.QColor("#1b006b"))
    wind.setPalette(pal_1)

    butt_hide = QtGui.QPushButton('Закрыть модальное окно')
    vbox = QtGui.QVBoxLayout()
    # vbox.addWidget(butt_hide)

    wid.setStyleSheet('QLabel {color: white; font-size: 20px; font-family: Proggy}'
                      'QLineEdit {font-size: 20px}'
                      'QPushButton {color: white; font-size: 20px; font-family: Proggy; border: 2px;'
                      'border-radius: 6px; background-color: transparent; min-height: 30px; text-align: left}'
                      'QPushButton:hover {background-color: #87cefa}')

    # блок 1
    frame1 = QtGui.QFrame()
    # frame1.setFrameShape(6)
    separator1 = QtGui.QFrame()
    separator1.setFrameStyle(QtGui.QFrame.HLine | QtGui.QFrame.Raised)
    separator1.setMaximumSize(400, 3)
    button1_1 = QtGui.QPushButton("Расчет максимальной концентрации\nалкоголя в крови")
    button1_1.setMaximumWidth(400)
    button1_1.clicked.connect(lambda: run_expertise(wind, 11, id_emp))
    button1_2 = QtGui.QPushButton("Расчет времени выведения алкоголя\nиз организма")
    button1_2.setMaximumWidth(400)
    button1_2.clicked.connect(lambda: run_expertise(wind, 12, id_emp))

    layout1 = QtGui.QVBoxLayout()
    layout1.addWidget(QtGui.QLabel("Токсикология"))
    layout1.addWidget(separator1)
    # layout1.addSpacerItem(QtGui.QSpacerItem(0, 999))
    layout1.addWidget(button1_1)
    layout1.addWidget(button1_2)
    layout1.addWidget(QtGui.QPushButton())
    frame1.setLayout(layout1)

    # блок 2
    frame2 = QtGui.QFrame()
    # frame2.setFrameShape(6)
    separator2 = QtGui.QFrame()
    separator2.setFrameStyle(QtGui.QFrame.HLine | QtGui.QFrame.Raised)
    separator2.setMaximumSize(400, 3)
    button2_1 = QtGui.QPushButton("Определение массы тела по\nметрическим параметрам")
    button2_1.setMaximumWidth(400)
    button2_1.clicked.connect(lambda: run_expertise(wind, 21, id_emp))

    layout2 = QtGui.QVBoxLayout()
    layout2.addWidget(QtGui.QLabel("Определение времени и ДНС"))
    layout2.addWidget(separator2)
    # layout1.addSpacerItem(QtGui.QSpacerItem(0, 999))
    layout2.addWidget(button2_1)
    layout2.addWidget(QtGui.QPushButton("\n"))
    layout2.addWidget(QtGui.QPushButton())
    frame2.setLayout(layout2)

    # блок 3
    frame3 = QtGui.QFrame()
    # frame3.setFrameShape(6)
    separator3 = QtGui.QFrame()
    separator3.setFrameStyle(QtGui.QFrame.HLine | QtGui.QFrame.Raised)
    separator3.setMaximumSize(400, 3)
    button3_1 = QtGui.QPushButton("Расчет индекса массы тела")
    button3_1.setMaximumWidth(400)
    button3_1.clicked.connect(lambda: run_expertise(wind, 31, id_emp))

    layout3 = QtGui.QVBoxLayout()
    layout3.addWidget(QtGui.QLabel("Антропометрические инструменты"))
    layout3.addWidget(separator3)
    # layout1.addSpacerItem(QtGui.QSpacerItem(0, 999))
    layout3.addWidget(button3_1)
    layout3.addWidget(QtGui.QPushButton("\n"))
    frame3.setLayout(layout3)

    # блок 4
    frame4 = QtGui.QFrame()
    # frame4.setFrameShape(6)
    separator4 = QtGui.QFrame()
    separator4.setFrameStyle(QtGui.QFrame.HLine | QtGui.QFrame.Raised)
    separator4.setMaximumSize(400, 3)
    button4_1 = QtGui.QPushButton("Расчет биологического возраста\nпо состоянию структуры печени")
    button4_1.setMaximumWidth(400)
    button4_1.clicked.connect(lambda: run_expertise(wind, 41, id_emp))

    layout4 = QtGui.QVBoxLayout()
    layout4.addWidget(QtGui.QLabel("Определение биологического возраста"))
    layout4.addWidget(separator4)
    # layout1.addSpacerItem(QtGui.QSpacerItem(0, 999))
    layout4.addWidget(button4_1)
    layout4.addWidget(QtGui.QPushButton())
    frame4.setLayout(layout4)

    # блок 5
    frame5 = QtGui.QFrame()
    # frame5.setFrameShape(6)
    separator5 = QtGui.QFrame()
    separator5.setFrameStyle(QtGui.QFrame.HLine | QtGui.QFrame.Raised)
    separator5.setMaximumSize(400, 3)
    button5_1 = QtGui.QPushButton("Определение силы удара головой\nпри падении человека на плоскости")
    button5_1.setMaximumWidth(400)
    button5_1.clicked.connect(lambda: run_expertise(wind, 51, id_emp))

    layout5 = QtGui.QVBoxLayout()
    layout5.addWidget(QtGui.QLabel("Судебно-медицинская травматология"))
    layout5.addWidget(separator5)
    # layout1.addSpacerItem(QtGui.QSpacerItem(0, 999))
    layout5.addWidget(button5_1)
    # layout5.addWidget(QtGui.QPushButton())
    frame5.setLayout(layout5)

    # компоновка главного виджета
    main_layout = QtGui.QGridLayout()
    main_layout.addWidget(frame1, 0, 0)
    main_layout.addWidget(frame2, 0, 1)
    main_layout.addWidget(frame3, 1, 0)
    main_layout.addWidget(frame4, 1, 1)
    main_layout.addWidget(frame5, 2, 0)

    vbox.addLayout(main_layout)
    vbox.addSpacerItem(QtGui.QSpacerItem(0, 200))
    # butt_hide.clicked.connect(wind.close)
    # wid.setLayout(main_layout)
    wid.setLayout(vbox)


def run_expertise(wind, exp_id, emp_id):
    win = QtGui.QWidget()
    if exp_id == 11:
        win = Calculator(emp_id)
    elif exp_id == 12:
        win = AlcoholExcretion(emp_id)
    elif exp_id == 21:
        win = BodyWeight(emp_id)
    elif exp_id == 31:
        win = BMI(emp_id)
    elif exp_id == 41:
        win = BioAgeKidneys(emp_id)
    elif exp_id == 51:
        win = DipPlane(emp_id)
    win.show()
