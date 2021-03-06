# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'battery1control.ui'
#
# Created: Tue Mar 24 23:30:33 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_battery1Control(object):
    def setupUi(self, battery1Control):
        battery1Control.setObjectName("battery1Control")
        battery1Control.resize(380, 480)
        battery1Control.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_title = QtWidgets.QLabel(battery1Control)
        self.label_title.setGeometry(QtCore.QRect(0, 10, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_title.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_op_state = QtWidgets.QLabel(battery1Control)
        self.label_op_state.setGeometry(QtCore.QRect(40, 120, 192, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_op_state.setFont(font)
        self.label_op_state.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label_op_state.setObjectName("label_op_state")
        self.spinBox = QtWidgets.QSpinBox(battery1Control)
        self.spinBox.setGeometry(QtCore.QRect(140, 360, 20, 61))
        self.spinBox.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.spinBox.setMinimum(-3000)
        self.spinBox.setMaximum(3000)
        self.spinBox.setObjectName("spinBox")
        self.batt1_control_mode = QtWidgets.QLabel(battery1Control)
        self.batt1_control_mode.setGeometry(QtCore.QRect(210, 290, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.batt1_control_mode.setFont(font)
        self.batt1_control_mode.setStyleSheet("color: rgb(255, 170, 0);")
        self.batt1_control_mode.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.batt1_control_mode.setObjectName("batt1_control_mode")
        self.batt1_apply_current_pb = QtWidgets.QPushButton(battery1Control)
        self.batt1_apply_current_pb.setGeometry(QtCore.QRect(60, 430, 71, 31))
        self.batt1_apply_current_pb.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 0);")
        self.batt1_apply_current_pb.setObjectName("batt1_apply_current_pb")
        self.dial = QtWidgets.QDial(battery1Control)
        self.dial.setGeometry(QtCore.QRect(50, 353, 91, 81))
        self.dial.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.dial.setMinimum(-3000)
        self.dial.setMaximum(3000)
        self.dial.setObjectName("dial")
        self.label_control = QtWidgets.QLabel(battery1Control)
        self.label_control.setGeometry(QtCore.QRect(40, 220, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_control.setFont(font)
        self.label_control.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_control.setObjectName("label_control")
        self.batt1_operating_state = QtWidgets.QLabel(battery1Control)
        self.batt1_operating_state.setGeometry(QtCore.QRect(220, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.batt1_operating_state.setFont(font)
        self.batt1_operating_state.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.batt1_operating_state.setAlignment(QtCore.Qt.AlignCenter)
        self.batt1_operating_state.setObjectName("batt1_operating_state")
        self.batt1_set_ref_voltage = QtWidgets.QLabel(battery1Control)
        self.batt1_set_ref_voltage.setGeometry(QtCore.QRect(265, 340, 31, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.batt1_set_ref_voltage.setFont(font)
        self.batt1_set_ref_voltage.setStyleSheet("color: rgb(255, 170, 0);")
        self.batt1_set_ref_voltage.setObjectName("batt1_set_ref_voltage")
        self.spinBox_2 = QtWidgets.QSpinBox(battery1Control)
        self.spinBox_2.setGeometry(QtCore.QRect(320, 360, 20, 61))
        self.spinBox_2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.spinBox_2.setMaximum(400)
        self.spinBox_2.setObjectName("spinBox_2")
        self.batt1_ref_voltage = QtWidgets.QLabel(battery1Control)
        self.batt1_ref_voltage.setGeometry(QtCore.QRect(270, 180, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.batt1_ref_voltage.setFont(font)
        self.batt1_ref_voltage.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.batt1_ref_voltage.setAlignment(QtCore.Qt.AlignCenter)
        self.batt1_ref_voltage.setObjectName("batt1_ref_voltage")
        self.batt1_apply_voltage_pb = QtWidgets.QPushButton(battery1Control)
        self.batt1_apply_voltage_pb.setGeometry(QtCore.QRect(240, 430, 71, 31))
        self.batt1_apply_voltage_pb.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 0);")
        self.batt1_apply_voltage_pb.setObjectName("batt1_apply_voltage_pb")
        self.batt1_set_ref_current = QtWidgets.QLabel(battery1Control)
        self.batt1_set_ref_current.setGeometry(QtCore.QRect(80, 340, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.batt1_set_ref_current.setFont(font)
        self.batt1_set_ref_current.setStyleSheet("color: rgb(255, 170, 0);")
        self.batt1_set_ref_current.setObjectName("batt1_set_ref_current")
        self.batt1_switch_control_mode_pb = QtWidgets.QPushButton(battery1Control)
        self.batt1_switch_control_mode_pb.setGeometry(QtCore.QRect(230, 250, 101, 41))
        self.batt1_switch_control_mode_pb.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 0);")
        self.batt1_switch_control_mode_pb.setObjectName("batt1_switch_control_mode_pb")
        self.label_ref_current = QtWidgets.QLabel(battery1Control)
        self.label_ref_current.setGeometry(QtCore.QRect(40, 149, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_ref_current.setFont(font)
        self.label_ref_current.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label_ref_current.setObjectName("label_ref_current")
        self.batt1_ref_current = QtWidgets.QLabel(battery1Control)
        self.batt1_ref_current.setGeometry(QtCore.QRect(270, 150, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.batt1_ref_current.setFont(font)
        self.batt1_ref_current.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.batt1_ref_current.setAlignment(QtCore.Qt.AlignCenter)
        self.batt1_ref_current.setObjectName("batt1_ref_current")
        self.label_status_2 = QtWidgets.QLabel(battery1Control)
        self.label_status_2.setGeometry(QtCore.QRect(70, 80, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_status_2.setFont(font)
        self.label_status_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label_status_2.setObjectName("label_status_2")
        self.label_ref_voltage = QtWidgets.QLabel(battery1Control)
        self.label_ref_voltage.setGeometry(QtCore.QRect(40, 179, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_ref_voltage.setFont(font)
        self.label_ref_voltage.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label_ref_voltage.setObjectName("label_ref_voltage")
        self.label_set_ref_voltage = QtWidgets.QLabel(battery1Control)
        self.label_set_ref_voltage.setGeometry(QtCore.QRect(230, 320, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_set_ref_voltage.setFont(font)
        self.label_set_ref_voltage.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_set_ref_voltage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_set_ref_voltage.setObjectName("label_set_ref_voltage")
        self.dial_2 = QtWidgets.QDial(battery1Control)
        self.dial_2.setGeometry(QtCore.QRect(230, 353, 91, 81))
        self.dial_2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.dial_2.setMaximum(400)
        self.dial_2.setProperty("value", 380)
        self.dial_2.setTracking(True)
        self.dial_2.setObjectName("dial_2")
        self.batt1_on_off_indicator = QtWidgets.QLabel(battery1Control)
        self.batt1_on_off_indicator.setGeometry(QtCore.QRect(220, 90, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.batt1_on_off_indicator.setFont(font)
        self.batt1_on_off_indicator.setStyleSheet("color: rgb(0, 0, 0);")
        self.batt1_on_off_indicator.setAlignment(QtCore.Qt.AlignCenter)
        self.batt1_on_off_indicator.setObjectName("batt1_on_off_indicator")
        self.label_set_ref_current = QtWidgets.QLabel(battery1Control)
        self.label_set_ref_current.setGeometry(QtCore.QRect(50, 320, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_set_ref_current.setFont(font)
        self.label_set_ref_current.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_set_ref_current.setObjectName("label_set_ref_current")
        self.batt1_on_off_pb = QtWidgets.QPushButton(battery1Control)
        self.batt1_on_off_pb.setGeometry(QtCore.QRect(60, 250, 91, 41))
        self.batt1_on_off_pb.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 0);")
        self.batt1_on_off_pb.setObjectName("batt1_on_off_pb")

        self.retranslateUi(battery1Control)
        self.dial_2.valueChanged['int'].connect(self.batt1_set_ref_voltage.setNum)
        self.dial_2.valueChanged['int'].connect(self.spinBox_2.setValue)
        self.spinBox_2.valueChanged['int'].connect(self.batt1_set_ref_voltage.setNum)
        self.dial.valueChanged['int'].connect(self.batt1_set_ref_current.setNum)
        self.dial.valueChanged['int'].connect(self.spinBox.setValue)
        self.spinBox.valueChanged['int'].connect(self.batt1_set_ref_current.setNum)
        QtCore.QMetaObject.connectSlotsByName(battery1Control)

    def retranslateUi(self, battery1Control):
        _translate = QtCore.QCoreApplication.translate
        battery1Control.setWindowTitle(_translate("battery1Control", "battery1Control"))
        self.label_title.setText(_translate("battery1Control", "BATTERY CONTROL"))
        self.label_op_state.setText(_translate("battery1Control", "Operating Mode:"))
        self.batt1_control_mode.setText(_translate("battery1Control", "Monitor Bus"))
        self.batt1_apply_current_pb.setText(_translate("battery1Control", "Apply"))
        self.label_control.setText(_translate("battery1Control", "Control"))
        self.batt1_operating_state.setText(_translate("battery1Control", "-"))
        self.batt1_set_ref_voltage.setText(_translate("battery1Control", "380"))
        self.batt1_ref_voltage.setText(_translate("battery1Control", "-"))
        self.batt1_apply_voltage_pb.setText(_translate("battery1Control", "Apply"))
        self.batt1_set_ref_current.setText(_translate("battery1Control", "0"))
        self.batt1_switch_control_mode_pb.setText(_translate("battery1Control", "Switch\n"
" Control Mode"))
        self.label_ref_current.setText(_translate("battery1Control", "Reference Current (mA): "))
        self.batt1_ref_current.setText(_translate("battery1Control", "-"))
        self.label_status_2.setText(_translate("battery1Control", "Status:"))
        self.label_ref_voltage.setText(_translate("battery1Control", "Reference Voltage (V): "))
        self.label_set_ref_voltage.setText(_translate("battery1Control", "Set Ref Voltage:"))
        self.batt1_on_off_indicator.setText(_translate("battery1Control", "OFF"))
        self.label_set_ref_current.setText(_translate("battery1Control", "Set Ref Current:"))
        self.batt1_on_off_pb.setText(_translate("battery1Control", "On/Off"))

