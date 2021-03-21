# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 186)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.connection = QtWidgets.QLabel(self.centralwidget)
        self.connection.setStyleSheet("color: green;")
        self.connection.setObjectName("connection")
        self.gridLayout.addWidget(self.connection, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setStyleSheet("font-weight: bold;")
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setStyleSheet("font-weight: bold;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 2)
        self.currentSubmode = QtWidgets.QLabel(self.tab_3)
        self.currentSubmode.setObjectName("currentSubmode")
        self.gridLayout_4.addWidget(self.currentSubmode, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setStyleSheet("font-weight: bold;")
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 3)
        self.currentResolution = QtWidgets.QLabel(self.tab_3)
        self.currentResolution.setObjectName("currentResolution")
        self.gridLayout_4.addWidget(self.currentResolution, 2, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setStyleSheet("font-weight: bold;")
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 3, 0, 1, 3)
        self.currentFramerate = QtWidgets.QLabel(self.tab_3)
        self.currentFramerate.setObjectName("currentFramerate")
        self.gridLayout_4.addWidget(self.currentFramerate, 3, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setStyleSheet("font-weight: bold;")
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 4, 0, 1, 1)
        self.videosLeft = QtWidgets.QLabel(self.tab_3)
        self.videosLeft.setObjectName("videosLeft")
        self.gridLayout_4.addWidget(self.videosLeft, 4, 3, 1, 1)
        self.currentMode = QtWidgets.QLabel(self.tab_3)
        self.currentMode.setObjectName("currentMode")
        self.gridLayout_4.addWidget(self.currentMode, 0, 3, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.stream_quality = QtWidgets.QComboBox(self.tab_2)
        self.stream_quality.setObjectName("stream_quality")
        self.stream_quality.addItem("")
        self.stream_quality.addItem("")
        self.stream_quality.addItem("")
        self.gridLayout_3.addWidget(self.stream_quality, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.ip_to_stream_to = QtWidgets.QLineEdit(self.tab_2)
        self.ip_to_stream_to.setObjectName("ip_to_stream_to")
        self.gridLayout_3.addWidget(self.ip_to_stream_to, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.obs_stream = QtWidgets.QPushButton(self.tab_2)
        self.obs_stream.setObjectName("obs_stream")
        self.horizontalLayout.addWidget(self.obs_stream)
        self.stream_button = QtWidgets.QPushButton(self.tab_2)
        self.stream_button.setObjectName("stream_button")
        self.horizontalLayout.addWidget(self.stream_button)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font-weight: bold;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.battery = QtWidgets.QLabel(self.centralwidget)
        self.battery.setStyleSheet("")
        self.battery.setObjectName("battery")
        self.gridLayout.addWidget(self.battery, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.connection.setText(_translate("MainWindow", "Not Connected"))
        self.label_4.setText(_translate("MainWindow", "Current Mode:"))
        self.label_5.setText(_translate("MainWindow", "Current Submode:"))
        self.currentSubmode.setText(_translate("MainWindow", "Value"))
        self.label_6.setText(_translate("MainWindow", "Current Resolution:"))
        self.currentResolution.setText(_translate("MainWindow", "Value"))
        self.label_7.setText(_translate("MainWindow", "Current Framerate:"))
        self.currentFramerate.setText(_translate("MainWindow", "Value"))
        self.label_8.setText(_translate("MainWindow", "Videos Left:"))
        self.videosLeft.setText(_translate("MainWindow", "Value"))
        self.currentMode.setText(_translate("MainWindow", "Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Overview"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Filename"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Size"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Files"))
        self.label_3.setText(_translate("MainWindow", "Quality:"))
        self.stream_quality.setItemText(0, _translate("MainWindow", "High"))
        self.stream_quality.setItemText(1, _translate("MainWindow", "Medium"))
        self.stream_quality.setItemText(2, _translate("MainWindow", "Low"))
        self.label_2.setText(_translate("MainWindow", "IP Address to Stream to:"))
        self.obs_stream.setText(_translate("MainWindow", "OBS Stream"))
        self.stream_button.setText(_translate("MainWindow", "Preview Stream"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Stream"))
        self.label.setText(_translate("MainWindow", "Status:"))
        self.battery.setText(_translate("MainWindow", "Battery %"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
