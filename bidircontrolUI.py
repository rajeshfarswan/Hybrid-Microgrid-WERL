# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bidircontrol.ui'
#
# Created: Sat Apr 11 13:30:06 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bidirControl(object):
    def setupUi(self, bidirControl):
        bidirControl.setObjectName("bidirControl")
        bidirControl.resize(380, 480)
        bidirControl.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.bidir_start_pb = QtWidgets.QPushButton(bidirControl)
        self.bidir_start_pb.setEnabled(False)
        self.bidir_start_pb.setGeometry(QtCore.QRect(220, 250, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bidir_start_pb.setFont(font)
        self.bidir_start_pb.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 0);")
        self.bidir_start_pb.setObjectName("bidir_start_pb")
        self.bidir_apply_pb = QtWidgets.QPushButton(bidirControl)
        self.bidir_apply_pb.setGeometry(QtCore.QRect(100, 250, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bidir_apply_pb.setFont(font)
        self.bidir_apply_pb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bidir_apply_pb.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 0);")
        self.bidir_apply_pb.setObjectName("bidir_apply_pb")
        self.tabWidget = QtWidgets.QTabWidget(bidirControl)
        self.tabWidget.setGeometry(QtCore.QRect(5, 320, 371, 151))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_bus = QtWidgets.QWidget()
        self.tab_bus.setObjectName("tab_bus")
        self.label_35 = QtWidgets.QLabel(self.tab_bus)
        self.label_35.setGeometry(QtCore.QRect(290, 20, 20, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_25 = QtWidgets.QLabel(self.tab_bus)
        self.label_25.setGeometry(QtCore.QRect(40, 100, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_28 = QtWidgets.QLabel(self.tab_bus)
        self.label_28.setGeometry(QtCore.QRect(100, 100, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.dial_4 = QtWidgets.QDial(self.tab_bus)
        self.dial_4.setGeometry(QtCore.QRect(40, 30, 91, 81))
        self.dial_4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.dial_4.setMinimum(300)
        self.dial_4.setMaximum(400)
        self.dial_4.setProperty("value", 380)
        self.dial_4.setObjectName("dial_4")
        self.label_36 = QtWidgets.QLabel(self.tab_bus)
        self.label_36.setGeometry(QtCore.QRect(240, 0, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.spinBox_4 = QtWidgets.QSpinBox(self.tab_bus)
        self.spinBox_4.setGeometry(QtCore.QRect(310, 40, 20, 61))
        self.spinBox_4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.spinBox_4.setMinimum(-10)
        self.spinBox_4.setMaximum(10)
        self.spinBox_4.setObjectName("spinBox_4")
        self.vdc_ref_bus = QtWidgets.QLabel(self.tab_bus)
        self.vdc_ref_bus.setGeometry(QtCore.QRect(70, 20, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vdc_ref_bus.setFont(font)
        self.vdc_ref_bus.setAlignment(QtCore.Qt.AlignCenter)
        self.vdc_ref_bus.setObjectName("vdc_ref_bus")
        self.dial_3 = QtWidgets.QDial(self.tab_bus)
        self.dial_3.setGeometry(QtCore.QRect(220, 30, 91, 81))
        self.dial_3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.dial_3.setMinimum(-10)
        self.dial_3.setMaximum(10)
        self.dial_3.setProperty("value", 0)
        self.dial_3.setTracking(True)
        self.dial_3.setObjectName("dial_3")
        self.label_27 = QtWidgets.QLabel(self.tab_bus)
        self.label_27.setGeometry(QtCore.QRect(280, 100, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_bus)
        self.spinBox_3.setGeometry(QtCore.QRect(130, 40, 20, 61))
        self.spinBox_3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.spinBox_3.setMinimum(300)
        self.spinBox_3.setMaximum(400)
        self.spinBox_3.setProperty("value", 380)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_33 = QtWidgets.QLabel(self.tab_bus)
        self.label_33.setGeometry(QtCore.QRect(40, 0, 110, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_26 = QtWidgets.QLabel(self.tab_bus)
        self.label_26.setGeometry(QtCore.QRect(220, 100, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_41 = QtWidgets.QLabel(self.tab_bus)
        self.label_41.setGeometry(QtCore.QRect(110, 20, 20, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.iq_ref_bus = QtWidgets.QLabel(self.tab_bus)
        self.iq_ref_bus.setGeometry(QtCore.QRect(250, 20, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.iq_ref_bus.setFont(font)
        self.iq_ref_bus.setAlignment(QtCore.Qt.AlignCenter)
        self.iq_ref_bus.setObjectName("iq_ref_bus")
        self.tabWidget.addTab(self.tab_bus, "")
        self.tab_pow = QtWidgets.QWidget()
        self.tab_pow.setObjectName("tab_pow")
        self.label_29 = QtWidgets.QLabel(self.tab_pow)
        self.label_29.setGeometry(QtCore.QRect(100, 100, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.dial_id_ref_pow = QtWidgets.QDial(self.tab_pow)
        self.dial_id_ref_pow.setGeometry(QtCore.QRect(40, 30, 91, 81))
        self.dial_id_ref_pow.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.dial_id_ref_pow.setMinimum(-10)
        self.dial_id_ref_pow.setMaximum(10)
        self.dial_id_ref_pow.setObjectName("dial_id_ref_pow")
        self.label_37 = QtWidgets.QLabel(self.tab_pow)
        self.label_37.setGeometry(QtCore.QRect(280, 100, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.id_ref_pow = QtWidgets.QLabel(self.tab_pow)
        self.id_ref_pow.setGeometry(QtCore.QRect(70, 20, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.id_ref_pow.setFont(font)
        self.id_ref_pow.setAlignment(QtCore.Qt.AlignCenter)
        self.id_ref_pow.setObjectName("id_ref_pow")
        self.dial_iq_ref_pow = QtWidgets.QDial(self.tab_pow)
        self.dial_iq_ref_pow.setGeometry(QtCore.QRect(220, 30, 91, 81))
        self.dial_iq_ref_pow.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.dial_iq_ref_pow.setMinimum(-10)
        self.dial_iq_ref_pow.setMaximum(10)
        self.dial_iq_ref_pow.setProperty("value", 10)
        self.dial_iq_ref_pow.setTracking(True)
        self.dial_iq_ref_pow.setObjectName("dial_iq_ref_pow")
        self.label_30 = QtWidgets.QLabel(self.tab_pow)
        self.label_30.setGeometry(QtCore.QRect(40, 100, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_39 = QtWidgets.QLabel(self.tab_pow)
        self.label_39.setGeometry(QtCore.QRect(50, 0, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.tab_pow)
        self.label_40.setGeometry(QtCore.QRect(240, 0, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.spinBox = QtWidgets.QSpinBox(self.tab_pow)
        self.spinBox.setGeometry(QtCore.QRect(130, 40, 20, 61))
        self.spinBox.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.spinBox.setMinimum(-10)
        self.spinBox.setMaximum(10)
        self.spinBox.setSingleStep(1)
        self.spinBox.setObjectName("spinBox")
        self.iq_ref_pow = QtWidgets.QLabel(self.tab_pow)
        self.iq_ref_pow.setGeometry(QtCore.QRect(250, 20, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.iq_ref_pow.setFont(font)
        self.iq_ref_pow.setAlignment(QtCore.Qt.AlignCenter)
        self.iq_ref_pow.setObjectName("iq_ref_pow")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_pow)
        self.spinBox_2.setGeometry(QtCore.QRect(310, 40, 20, 61))
        self.spinBox_2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.spinBox_2.setMinimum(-10)
        self.spinBox_2.setMaximum(10)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_34 = QtWidgets.QLabel(self.tab_pow)
        self.label_34.setGeometry(QtCore.QRect(220, 100, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_38 = QtWidgets.QLabel(self.tab_pow)
        self.label_38.setGeometry(QtCore.QRect(100, 20, 20, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.label_42 = QtWidgets.QLabel(self.tab_pow)
        self.label_42.setGeometry(QtCore.QRect(290, 20, 20, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.tabWidget.addTab(self.tab_pow, "")
        self.label_title = QtWidgets.QLabel(bidirControl)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 381, 31))
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
        self.label_control = QtWidgets.QLabel(bidirControl)
        self.label_control.setGeometry(QtCore.QRect(1, 240, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_control.setFont(font)
        self.label_control.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_control.setObjectName("label_control")
        self.label_13 = QtWidgets.QLabel(bidirControl)
        self.label_13.setGeometry(QtCore.QRect(190, 210, 104, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_8 = QtWidgets.QLabel(bidirControl)
        self.label_8.setGeometry(QtCore.QRect(0, 210, 104, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.bidir_voltage_c = QtWidgets.QLabel(bidirControl)
        self.bidir_voltage_c.setGeometry(QtCore.QRect(300, 207, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bidir_voltage_c.setFont(font)
        self.bidir_voltage_c.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.bidir_voltage_c.setAlignment(QtCore.Qt.AlignCenter)
        self.bidir_voltage_c.setObjectName("bidir_voltage_c")
        self.label_11 = QtWidgets.QLabel(bidirControl)
        self.label_11.setGeometry(QtCore.QRect(190, 180, 104, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.bidir_current_b = QtWidgets.QLabel(bidirControl)
        self.bidir_current_b.setGeometry(QtCore.QRect(110, 179, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bidir_current_b.setFont(font)
        self.bidir_current_b.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.bidir_current_b.setAlignment(QtCore.Qt.AlignCenter)
        self.bidir_current_b.setObjectName("bidir_current_b")
        self.label_7 = QtWidgets.QLabel(bidirControl)
        self.label_7.setGeometry(QtCore.QRect(0, 150, 104, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.bidir_voltage_a = QtWidgets.QLabel(bidirControl)
        self.bidir_voltage_a.setGeometry(QtCore.QRect(300, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bidir_voltage_a.setFont(font)
        self.bidir_voltage_a.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.bidir_voltage_a.setAlignment(QtCore.Qt.AlignCenter)
        self.bidir_voltage_a.setObjectName("bidir_voltage_a")
        self.bidir_current_c = QtWidgets.QLabel(bidirControl)
        self.bidir_current_c.setGeometry(QtCore.QRect(110, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bidir_current_c.setFont(font)
        self.bidir_current_c.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.bidir_current_c.setAlignment(QtCore.Qt.AlignCenter)
        self.bidir_current_c.setObjectName("bidir_current_c")
        self.bidir_current_a = QtWidgets.QLabel(bidirControl)
        self.bidir_current_a.setGeometry(QtCore.QRect(110, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bidir_current_a.setFont(font)
        self.bidir_current_a.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.bidir_current_a.setAlignment(QtCore.Qt.AlignCenter)
        self.bidir_current_a.setObjectName("bidir_current_a")
        self.label_10 = QtWidgets.QLabel(bidirControl)
        self.label_10.setGeometry(QtCore.QRect(190, 150, 104, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(bidirControl)
        self.label_5.setGeometry(QtCore.QRect(0, 180, 104, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.bidir_voltage_b = QtWidgets.QLabel(bidirControl)
        self.bidir_voltage_b.setGeometry(QtCore.QRect(300, 180, 71, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bidir_voltage_b.setFont(font)
        self.bidir_voltage_b.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.bidir_voltage_b.setAlignment(QtCore.Qt.AlignCenter)
        self.bidir_voltage_b.setObjectName("bidir_voltage_b")
        self.bidir_reactive_power = QtWidgets.QLabel(bidirControl)
        self.bidir_reactive_power.setGeometry(QtCore.QRect(230, 120, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bidir_reactive_power.setFont(font)
        self.bidir_reactive_power.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.bidir_reactive_power.setAlignment(QtCore.Qt.AlignCenter)
        self.bidir_reactive_power.setObjectName("bidir_reactive_power")
        self.label_12 = QtWidgets.QLabel(bidirControl)
        self.label_12.setGeometry(QtCore.QRect(130, 38, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.bidir_frequency = QtWidgets.QLabel(bidirControl)
        self.bidir_frequency.setGeometry(QtCore.QRect(230, 65, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bidir_frequency.setFont(font)
        self.bidir_frequency.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.bidir_frequency.setAlignment(QtCore.Qt.AlignCenter)
        self.bidir_frequency.setObjectName("bidir_frequency")
        self.label_6 = QtWidgets.QLabel(bidirControl)
        self.label_6.setGeometry(QtCore.QRect(60, 120, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.bidir_real_power = QtWidgets.QLabel(bidirControl)
        self.bidir_real_power.setGeometry(QtCore.QRect(230, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bidir_real_power.setFont(font)
        self.bidir_real_power.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.bidir_real_power.setAlignment(QtCore.Qt.AlignCenter)
        self.bidir_real_power.setObjectName("bidir_real_power")
        self.bidir_vdc = QtWidgets.QLabel(bidirControl)
        self.bidir_vdc.setGeometry(QtCore.QRect(230, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bidir_vdc.setFont(font)
        self.bidir_vdc.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.bidir_vdc.setAlignment(QtCore.Qt.AlignCenter)
        self.bidir_vdc.setObjectName("bidir_vdc")
        self.label_3 = QtWidgets.QLabel(bidirControl)
        self.label_3.setGeometry(QtCore.QRect(120, 65, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(bidirControl)
        self.label_4.setGeometry(QtCore.QRect(100, 90, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(bidirControl)
        self.tabWidget.setCurrentIndex(0)
        self.dial_id_ref_pow.valueChanged['int'].connect(self.id_ref_pow.setNum)
        self.dial_id_ref_pow.valueChanged['int'].connect(self.spinBox.setValue)
        self.spinBox.valueChanged['int'].connect(self.id_ref_pow.setNum)
        self.dial_iq_ref_pow.valueChanged['int'].connect(self.iq_ref_pow.setNum)
        self.dial_iq_ref_pow.valueChanged['int'].connect(self.spinBox_2.setValue)
        self.spinBox_2.valueChanged['int'].connect(self.iq_ref_pow.setNum)
        self.dial_4.valueChanged['int'].connect(self.vdc_ref_bus.setNum)
        self.dial_4.valueChanged['int'].connect(self.spinBox_3.setValue)
        self.spinBox_3.valueChanged['int'].connect(self.vdc_ref_bus.setNum)
        self.dial_3.valueChanged['int'].connect(self.iq_ref_bus.setNum)
        self.dial_3.valueChanged['int'].connect(self.spinBox_4.setValue)
        self.spinBox_4.valueChanged['int'].connect(self.iq_ref_bus.setNum)
        QtCore.QMetaObject.connectSlotsByName(bidirControl)

    def retranslateUi(self, bidirControl):
        _translate = QtCore.QCoreApplication.translate
        bidirControl.setWindowTitle(_translate("bidirControl", "bidirControl"))
        self.bidir_start_pb.setText(_translate("bidirControl", "Start"))
        self.bidir_apply_pb.setText(_translate("bidirControl", "Apply"))
        self.label_35.setText(_translate("bidirControl", "A"))
        self.label_25.setText(_translate("bidirControl", "300 V"))
        self.label_28.setText(_translate("bidirControl", "400 V"))
        self.label_36.setText(_translate("bidirControl", "Iq Reference:"))
        self.vdc_ref_bus.setText(_translate("bidirControl", "380"))
        self.label_27.setText(_translate("bidirControl", "10 A"))
        self.label_33.setText(_translate("bidirControl", "Vdc Reference:"))
        self.label_26.setText(_translate("bidirControl", "-10 A"))
        self.label_41.setText(_translate("bidirControl", "V"))
        self.iq_ref_bus.setText(_translate("bidirControl", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_bus), _translate("bidirControl", "Bus Monitoring Mode"))
        self.label_29.setText(_translate("bidirControl", "10 A"))
        self.label_37.setText(_translate("bidirControl", "10 A"))
        self.id_ref_pow.setText(_translate("bidirControl", "0"))
        self.label_30.setText(_translate("bidirControl", "-10 A"))
        self.label_39.setText(_translate("bidirControl", "Id Reference:"))
        self.label_40.setText(_translate("bidirControl", "Iq Reference:"))
        self.iq_ref_pow.setText(_translate("bidirControl", "0"))
        self.label_34.setText(_translate("bidirControl", "-10 A"))
        self.label_38.setText(_translate("bidirControl", "A"))
        self.label_42.setText(_translate("bidirControl", "A"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_pow), _translate("bidirControl", "Power Dispatching Mode"))
        self.label_title.setText(_translate("bidirControl", "BIDIRECTIONAL CONTROL"))
        self.label_control.setText(_translate("bidirControl", "Control"))
        self.label_13.setText(_translate("bidirControl", "Voltage C(V):"))
        self.label_8.setText(_translate("bidirControl", "Current C(A):"))
        self.bidir_voltage_c.setText(_translate("bidirControl", "-"))
        self.label_11.setText(_translate("bidirControl", "Voltage B(V):"))
        self.bidir_current_b.setText(_translate("bidirControl", "-"))
        self.label_7.setText(_translate("bidirControl", "Current A(A):"))
        self.bidir_voltage_a.setText(_translate("bidirControl", "-"))
        self.bidir_current_c.setText(_translate("bidirControl", "-"))
        self.bidir_current_a.setText(_translate("bidirControl", "-"))
        self.label_10.setText(_translate("bidirControl", "Voltage A(V):"))
        self.label_5.setText(_translate("bidirControl", "Current B(A):"))
        self.bidir_voltage_b.setText(_translate("bidirControl", "-"))
        self.bidir_reactive_power.setText(_translate("bidirControl", "-"))
        self.label_12.setText(_translate("bidirControl", "Vdc(V):"))
        self.bidir_frequency.setText(_translate("bidirControl", "-"))
        self.label_6.setStyleSheet(_translate("bidirControl", "color: rgb(255, 255, 255);"))
        self.label_6.setText(_translate("bidirControl", "Reactive Power(Var):"))
        self.bidir_real_power.setText(_translate("bidirControl", "-"))
        self.bidir_vdc.setText(_translate("bidirControl", "-"))
        self.label_3.setStyleSheet(_translate("bidirControl", "color: rgb(255, 255, 255);"))
        self.label_3.setText(_translate("bidirControl", "Frequency:"))
        self.label_4.setStyleSheet(_translate("bidirControl", "color: rgb(255, 255, 255);"))
        self.label_4.setText(_translate("bidirControl", "Real Power(W):"))
