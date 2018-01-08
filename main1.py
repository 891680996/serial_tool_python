# -*- coding: utf-8 -*-
import Ui_optical_communication
import sys
import struct
import serial
import time
import threading
import binascii
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import *
import matplotlib
matplotlib.use("Qt5Agg")

# data bit
SERIAL_DATABIT_ARRAY = (serial.EIGHTBITS, serial.SEVENBITS,
                        serial.SIXBITS, serial.FIVEBITS)
# stop bit
SERIAL_STOPBIT_ARRAY = (serial.STOPBITS_ONE,
                        serial.STOPBITS_ONE_POINT_FIVE, serial.STOPBITS_TWO)
# parity
SERIAL_CHECKBIT_ARRAY = (serial.PARITY_NONE, serial.PARITY_EVEN,
                         serial.PARITY_ODD, serial.PARITY_MARK,
                         serial.PARITY_SPACE)

# matplot画图类


class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.fig.subplots_adjust(left=0.08, right=0.99, top=0.9, bottom=0.2)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(
            self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.databuflimit = 200
        self.line1, = self.ax.plot([], [], color='blue', drawstyle='steps')
        self.plotdatabuf = []
        self.ax.grid()
        self.ax.hold(False)

    def matplot_updatabuf(self, newdata):
        if len(self.plotdatabuf) >= self.databuflimit:
            del self.plotdatabuf[0]
            try:
                self.plotdatabuf[self.databuflimit] = newdata
            except:
                self.plotdatabuf.append(newdata)
        else:
            self.plotdatabuf.append(newdata)


class CKZS(Ui_optical_communication.Ui_Form):
    # initialize
    def __init__(self, Ui_Form):
        super(Ui_optical_communication.Ui_Form, self).__init__()
        self.__index = 0
        self.setupUi(MainWindow)  # 显示主窗口

        self.portstatus_flag = False  # 端口使能标志
        self._serial = serial.Serial()  # i初始化串口

        self.start_button.clicked.connect(self.start_button_Clicked)  # 打开串口操作
        self.clear_rx_button.clicked.connect(self.clear_rx_button_Clicked)
        self.clear_tx_button.clicked.connect(self.clear_tx_button_Clicked)
        self.sent_data_button.clicked.connect(self.SendData)  # 打开串口操作

        # 用来实现波形的显示，画图
        #self.matplot = MplCanvas()
        self.matplot_r = MplCanvas()
        self.rx_sig_plot.addWidget(self.matplot_r)  # received signal
        self.matplot_t = MplCanvas()
        self.tx_sig_plot.addWidget(self.matplot_t)  # transmitted signal

        self.recstr = str     # 串口接收字符串
        self.senstr = str     # 串口发送字符串

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.ReadData)

    def start_button_Clicked(self):
        clickstatus = self.start_button.isChecked()  # 串口开关状态检查
        if clickstatus:  # 如果开关为打开状态
            # 获得串口参数
            # 端口号，计算机端口都是从0开始算的，所以减去1
            comread = self.set_ports_box.currentText()
            bandrate = int(self.set_baud_rate_box.currentText())  # 波特率
            databit = 7
            stopbit = 1
            # databit = SERIAL_DATABIT_ARRAY[self.set_data_bit_box.currentIndex()]
            # stopbit = SERIAL_STOPBIT_ARRAY[self.set_stop_bit_box.currentIndex()]
            checkbit = SERIAL_CHECKBIT_ARRAY[self.set_parity_box.currentIndex()]

            # 打开串口
            try:
                self._serial.port = "com" + comread
                self._serial.baudrate = bandrate
                self._serial.bytesize = databit
                self._serial.parity = checkbit
                self._serial.stopbits = stopbit
                self._serial.open()
            except (OSError, serial.SerialException):  # 错误信息
                QtWidgets.QMessageBox.warning(
                    None, 'Error', "Invalid Serial Port", QtWidgets.QMessageBox.Ok)

            if self._serial.isOpen():
                self.timer.start(30)    # 定时器30ms刷新一次界面
                self.start_button.setText("Stop")  # 串口打开成功之后，按钮由“打开”变为“关闭”
                self.set_baud_rate_box.setEnabled(False)  # 波特率
                self.set_parity_box.setEnabled(False)  # 校验位
                self.set_data_bit_box.setEnabled(False)  # 数据位
                self.set_stop_bit_box.setEnabled(False)  # 停止位
                self.set_ports_box.setEnabled(False)  # 端口
                self.portstatus_flag = True
            else:
                self.start_button.setChecked(False)  # 如果串口没有打开成果，按钮回复为未打开状态
        else:    # 关闭串口、使能各个窗口
            self._serial.close()
            self.timer.stop()
            self.start_button.setText("Start")
            self.set_baud_rate_box.setEnabled(True)  # 波特率
            self.set_parity_box.setEnabled(True)  # 校验位
            self.set_data_bit_box.setEnabled(True)  # 数据位
            self.set_stop_bit_box.setEnabled(True)  # 停止位
            self.set_ports_box.setEnabled(True)  # 端口
            self.portstatus_flag = False

    def clear_rx_button_Clicked(self):  # 接收窗口清楚数据
        self.output_window.clear()
        #self.matplot_r.ax.clf()

    def clear_tx_button_Clicked(self):  # 接收窗口清楚数据
        self.input_window.clear()

    def SendData(self):
        if self.portstatus_flag is True:
            self._serial.write(self.input_window.toPlainText().encode())  # 读取串口数据
            self.senstr = self.input_window.toPlainText().encode()
            self.WinReFresh_t()  # 根据选择，来判断数据在那个窗口刷新
        else:
            QtWidgets.QMessageBox.warning(
                None, 'Error', "Please Open The Serial",
                QtWidgets.QMessageBox.Ok)

    def WinReFresh_t(self):
        self.HexMatplotDisplay_t(self.senstr)

    # 数据接收
    def ReadData(self):  # deal sci data
        if self.portstatus_flag is True:
            try:
                bytesToRead = self._serial.inWaiting()  # 读取缓冲区有多少数据
            except:
                self.start_button.setChecked(False)  # 出现异常，则关闭串口
                self.start_button_Click()
                bytesToRead = 0

            if bytesToRead > 0:  # 大于0 ，则取出数据
                self.recstr = self._serial.read(bytesToRead)  # 读取串口数据
                # print(self.recstr)
                self.WinReFresh_r()  # 根据选择，来判断数据在那个窗口刷新

    def WinReFresh_r(self):
        self.output_window.appendPlainText(self.recstr.decode("utf-8"))
        self.HexMatplotDisplay_r(self.recstr)

        if self.output_window.toPlainText().__len__() > 500:
            self.output_window.clear()

    def HexMatplotDisplay_r(self, p_str):
        for num1 in p_str:
            num2 = bin(num1).replace('0b','')
            for num in num2:
                self.matplot_r.matplot_updatabuf(num)
            # print(num)
        self.Multiplot_Refresh()

    def HexMatplotDisplay_t(self, p_str):
        for num1 in p_str:
            num2 = bin(num1).replace('0b','')
            for num in num2:
                self.matplot_t.matplot_updatabuf(num)
            # print(num)
        self.Multiplot_Refresh()

    def Multiplot_Refresh(self):
        if len(self.matplot_r.plotdatabuf) < self.matplot_r.databuflimit:
            self.matplot_r.line1.set_xdata(
                np.arange(len(self.matplot_r.plotdatabuf)))
            self.matplot_r.line1.set_ydata(self.matplot_r.plotdatabuf)
        else:
            self.matplot_r.line1.set_xdata(
                np.arange(self.matplot_r.databuflimit))
            self.matplot_r.line1.set_ydata(self.matplot_r.plotdatabuf[
                :self.matplot_r.databuflimit])
        if len(self.matplot_t.plotdatabuf) < self.matplot_t.databuflimit:
            self.matplot_t.line1.set_xdata(
                np.arange(len(self.matplot_t.plotdatabuf)))
            self.matplot_t.line1.set_ydata(self.matplot_t.plotdatabuf)
        else:
            self.matplot_t.line1.set_xdata(
                np.arange(self.matplot_t.databuflimit))
            self.matplot_t.line1.set_ydata(self.matplot_t.plotdatabuf[
                :self.matplot_t.databuflimit])
        # 更新数据后去刷新matplot界面
        self.matplot_r.ax.relim()
        self.matplot_r.ax.autoscale_view()
        self.matplot_r.draw()

        # 更新数据后去刷新matplot界面
        self.matplot_t.ax.relim()
        self.matplot_t.ax.autoscale_view()
        self.matplot_t.draw()


if __name__ == "__main__":
    # import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = CKZS(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
