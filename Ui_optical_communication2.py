# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hui\Desktop\wangml\我的坚果云\workspace_office\python\reic6\sci_tool-master\aaaa.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(430, 337)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.set_window_layout = QtWidgets.QVBoxLayout()
        self.set_window_layout.setSpacing(2)
        self.set_window_layout.setObjectName("set_window_layout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.set_ports_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.set_ports_label.sizePolicy().hasHeightForWidth())
        self.set_ports_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.set_ports_label.setFont(font)
        self.set_ports_label.setTextFormat(QtCore.Qt.AutoText)
        self.set_ports_label.setScaledContents(False)
        self.set_ports_label.setAlignment(QtCore.Qt.AlignCenter)
        self.set_ports_label.setObjectName("set_ports_label")
        self.horizontalLayout_14.addWidget(self.set_ports_label)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.set_ports_box = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.set_ports_box.sizePolicy().hasHeightForWidth())
        self.set_ports_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.set_ports_box.setFont(font)
        self.set_ports_box.setObjectName("set_ports_box")
        self.set_ports_box.addItem("")
        self.set_ports_box.addItem("")
        self.set_ports_box.addItem("")
        self.set_ports_box.addItem("")
        self.set_ports_box.addItem("")
        self.set_ports_box.addItem("")
        self.set_ports_box.addItem("")
        self.set_ports_box.addItem("")
        self.set_ports_box.addItem("")
        self.horizontalLayout_13.addWidget(self.set_ports_box)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_12)
        self.set_window_layout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.set_baud_rate_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.set_baud_rate_label.sizePolicy().hasHeightForWidth())
        self.set_baud_rate_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.set_baud_rate_label.setFont(font)
        self.set_baud_rate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.set_baud_rate_label.setObjectName("set_baud_rate_label")
        self.horizontalLayout_15.addWidget(self.set_baud_rate_label)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.set_baud_rate_box = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.set_baud_rate_box.sizePolicy().hasHeightForWidth())
        self.set_baud_rate_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.set_baud_rate_box.setFont(font)
        self.set_baud_rate_box.setObjectName("set_baud_rate_box")
        self.set_baud_rate_box.addItem("")
        self.set_baud_rate_box.addItem("")
        self.set_baud_rate_box.addItem("")
        self.set_baud_rate_box.addItem("")
        self.set_baud_rate_box.addItem("")
        self.set_baud_rate_box.addItem("")
        self.set_baud_rate_box.addItem("")
        self.set_baud_rate_box.addItem("")
        self.set_baud_rate_box.addItem("")
        self.set_baud_rate_box.addItem("")
        self.horizontalLayout_16.addWidget(self.set_baud_rate_box)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_16)
        self.set_window_layout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.set_parity_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.set_parity_label.sizePolicy().hasHeightForWidth())
        self.set_parity_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.set_parity_label.setFont(font)
        self.set_parity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.set_parity_label.setObjectName("set_parity_label")
        self.horizontalLayout_17.addWidget(self.set_parity_label)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.set_parity_box = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.set_parity_box.sizePolicy().hasHeightForWidth())
        self.set_parity_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.set_parity_box.setFont(font)
        self.set_parity_box.setObjectName("set_parity_box")
        self.set_parity_box.addItem("")
        self.set_parity_box.addItem("")
        self.set_parity_box.addItem("")
        self.set_parity_box.addItem("")
        self.set_parity_box.addItem("")
        self.horizontalLayout_18.addWidget(self.set_parity_box)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_18)
        self.set_window_layout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_4.addLayout(self.set_window_layout)
        self.input_output_layout = QtWidgets.QGridLayout()
        self.input_output_layout.setObjectName("input_output_layout")
        self.input_output_tabWidget = QtWidgets.QTabWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_output_tabWidget.setFont(font)
        self.input_output_tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.input_output_tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.input_output_tabWidget.setObjectName("input_output_tabWidget")
        self.input_window_q = QtWidgets.QWidget()
        self.input_window_q.setObjectName("input_window_q")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.input_window_q)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_window = QtWidgets.QPlainTextEdit(self.input_window_q)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_window.setFont(font)
        self.input_window.setObjectName("input_window")
        self.horizontalLayout.addWidget(self.input_window)
        self.input_output_tabWidget.addTab(self.input_window_q, "")
        self.output_window_q = QtWidgets.QWidget()
        self.output_window_q.setObjectName("output_window_q")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.output_window_q)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.output_window = QtWidgets.QPlainTextEdit(self.output_window_q)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output_window.setFont(font)
        self.output_window.setObjectName("output_window")
        self.horizontalLayout_3.addWidget(self.output_window)
        self.input_output_tabWidget.addTab(self.output_window_q, "")
        self.input_output_layout.addWidget(
            self.input_output_tabWidget, 0, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.input_output_layout)
        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 13)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.start_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setAcceptDrops(False)
        self.start_button.setCheckable(True)
        self.start_button.setAutoRepeat(False)
        self.start_button.setAutoExclusive(False)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout_5.addWidget(self.start_button)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sent_data_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sent_data_button.sizePolicy().hasHeightForWidth())
        self.sent_data_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.sent_data_button.setFont(font)
        self.sent_data_button.setObjectName("sent_data_button")
        self.horizontalLayout_2.addWidget(self.sent_data_button)
        self.clear_tx_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clear_tx_button.sizePolicy().hasHeightForWidth())
        self.clear_tx_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.clear_tx_button.setFont(font)
        self.clear_tx_button.setObjectName("clear_tx_button")
        self.horizontalLayout_2.addWidget(self.clear_tx_button)
        self.clear_rx_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clear_rx_button.sizePolicy().hasHeightForWidth())
        self.clear_rx_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.clear_rx_button.setFont(font)
        self.clear_rx_button.setObjectName("clear_rx_button")
        self.horizontalLayout_2.addWidget(self.clear_rx_button)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.setStretch(0, 4)
        self.horizontalLayout_6.setStretch(1, 13)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.gridLayout_2.setRowStretch(0, 7)
        self.gridLayout_2.setRowStretch(1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.plot_input_output_layout = QtWidgets.QVBoxLayout()
        self.plot_input_output_layout.setSpacing(0)
        self.plot_input_output_layout.setObjectName("plot_input_output_layout")
        self.plot_table = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.plot_table.sizePolicy().hasHeightForWidth())
        self.plot_table.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.plot_table.setFont(font)
        self.plot_table.setTabPosition(QtWidgets.QTabWidget.North)
        self.plot_table.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.plot_table.setIconSize(QtCore.QSize(16, 10))
        self.plot_table.setElideMode(QtCore.Qt.ElideMiddle)
        self.plot_table.setUsesScrollButtons(True)
        self.plot_table.setDocumentMode(False)
        self.plot_table.setTabsClosable(False)
        self.plot_table.setMovable(False)
        self.plot_table.setObjectName("plot_table")
        self.RX_Sig_Wave = QtWidgets.QWidget()
        self.RX_Sig_Wave.setObjectName("RX_Sig_Wave")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.RX_Sig_Wave)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.rx_sig_plot = QtWidgets.QVBoxLayout()
        self.rx_sig_plot.setSpacing(0)
        self.rx_sig_plot.setObjectName("rx_sig_plot")
        self.verticalLayout_8.addLayout(self.rx_sig_plot)
        self.plot_table.addTab(self.RX_Sig_Wave, "")
        self.TX_Sig_wave = QtWidgets.QWidget()
        self.TX_Sig_wave.setObjectName("TX_Sig_wave")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.TX_Sig_wave)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tx_sig_plot = QtWidgets.QVBoxLayout()
        self.tx_sig_plot.setSpacing(0)
        self.tx_sig_plot.setObjectName("tx_sig_plot")
        self.verticalLayout_4.addLayout(self.tx_sig_plot)
        self.plot_table.addTab(self.TX_Sig_wave, "")
        self.plot_input_output_layout.addWidget(self.plot_table)
        self.verticalLayout_5.addLayout(self.plot_input_output_layout)
        self.verticalLayout_5.setStretch(0, 3)
        self.verticalLayout_5.setStretch(1, 2)
        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.retranslateUi(Form)
        self.input_output_tabWidget.setCurrentIndex(1)
        self.plot_table.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.set_ports_label.setText(_translate("Form", "Ports"))
        self.set_ports_box.setItemText(0, _translate("Form", "1"))
        self.set_ports_box.setItemText(1, _translate("Form", "2"))
        self.set_ports_box.setItemText(2, _translate("Form", "3"))
        self.set_ports_box.setItemText(3, _translate("Form", "4"))
        self.set_ports_box.setItemText(4, _translate("Form", "5"))
        self.set_ports_box.setItemText(5, _translate("Form", "6"))
        self.set_ports_box.setItemText(6, _translate("Form", "7"))
        self.set_ports_box.setItemText(7, _translate("Form", "8"))
        self.set_ports_box.setItemText(8, _translate("Form", "9"))
        self.set_baud_rate_label.setText(_translate("Form", "Brate"))
        self.set_baud_rate_box.setItemText(0, _translate("Form", "300"))
        self.set_baud_rate_box.setItemText(1, _translate("Form", "600"))
        self.set_baud_rate_box.setItemText(2, _translate("Form", "1200"))
        self.set_baud_rate_box.setItemText(3, _translate("Form", "2400"))
        self.set_baud_rate_box.setItemText(4, _translate("Form", "4800"))
        self.set_baud_rate_box.setItemText(5, _translate("Form", "9600"))
        self.set_baud_rate_box.setItemText(6, _translate("Form", "19200"))
        self.set_baud_rate_box.setItemText(7, _translate("Form", "38400"))
        self.set_baud_rate_box.setItemText(8, _translate("Form", "57600"))
        self.set_baud_rate_box.setItemText(9, _translate("Form", "115200"))
        self.set_parity_label.setText(_translate("Form", "Parity"))
        self.set_parity_box.setItemText(0, _translate("Form", "Odd"))
        self.set_parity_box.setItemText(1, _translate("Form", "None"))
        self.set_parity_box.setItemText(2, _translate("Form", "Even"))
        self.set_parity_box.setItemText(3, _translate("Form", "Mark"))
        self.set_parity_box.setItemText(4, _translate("Form", "Space"))
        self.input_output_tabWidget.setTabText(self.input_output_tabWidget.indexOf(
            self.input_window_q), _translate("Form", "input_tab"))
        self.input_output_tabWidget.setTabText(self.input_output_tabWidget.indexOf(
            self.output_window_q), _translate("Form", "output_tab"))
        self.start_button.setText(_translate("Form", "Start"))
        self.sent_data_button.setText(_translate("Form", "Sent Data"))
        self.clear_tx_button.setText(_translate("Form", "Clear TX"))
        self.clear_rx_button.setText(_translate("Form", "Clear RX"))
        self.plot_table.setTabText(self.plot_table.indexOf(
            self.RX_Sig_Wave), _translate("Form", "rx_sig"))
        self.plot_table.setTabText(self.plot_table.indexOf(
            self.TX_Sig_wave), _translate("Form", "tx_sig"))
