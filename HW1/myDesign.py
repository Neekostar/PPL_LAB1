# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(763, 765)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #ff6427")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.showGraphic = QtWidgets.QPushButton(self.centralwidget)
        self.showGraphic.setGeometry(QtCore.QRect(500, 270, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.showGraphic.setFont(font)
        self.showGraphic.setStyleSheet("background-color: #4ff1ff")
        self.showGraphic.setObjectName("showGraphic")
        self.btnShowData = QtWidgets.QPushButton(self.centralwidget)
        self.btnShowData.setGeometry(QtCore.QRect(510, 670, 231, 51))
        self.btnShowData.setMinimumSize(QtCore.QSize(231, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnShowData.setFont(font)
        self.btnShowData.setStyleSheet("background-color: #4ff1ff")
        self.btnShowData.setObjectName("btnShowData")
        self.txtBrowserInfo = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtBrowserInfo.setGeometry(QtCore.QRect(510, 440, 231, 211))
        self.txtBrowserInfo.setStyleSheet("background-color: #FFFFFF")
        self.txtBrowserInfo.setObjectName("txtBrowserInfo")
        self.lblEmotions = QtWidgets.QLabel(self.centralwidget)
        self.lblEmotions.setGeometry(QtCore.QRect(260, 400, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lblEmotions.setFont(font)
        self.lblEmotions.setStyleSheet("color: blue")
        self.lblEmotions.setObjectName("lblEmotions")
        self.lblPicture = QtWidgets.QLabel(self.centralwidget)
        self.lblPicture.setGeometry(QtCore.QRect(190, 450, 261, 261))
        self.lblPicture.setStyleSheet("background-color: #ffffff")
        self.lblPicture.setText("")

        self.lblPicture.setObjectName("lblPicture")
        self.lblChoice = QtWidgets.QLabel(self.centralwidget)
        self.lblChoice.setGeometry(QtCore.QRect(30, 720, 281, 16))
        self.lblChoice.setStyleSheet("color: red")
        self.lblChoice.setText("")
        self.lblChoice.setObjectName("lblChoice")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 701, 241))
        self.widget.setStyleSheet("background-color: #FFFFFF\n"
                                  "")
        self.widget.setObjectName("widget")
        self.pushButton_happy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_happy.setGeometry(QtCore.QRect(50, 540, 93, 28))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(187, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(187, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(187, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 100, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_happy.setPalette(palette)
        self.pushButton_happy.setObjectName("pushButton_happy")
        self.pushButton_sad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sad.setGeometry(QtCore.QRect(50, 570, 93, 28))
        self.pushButton_sad.setObjectName("pushButton_sad")
        self.pushButton_angry = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_angry.setGeometry(QtCore.QRect(50, 600, 93, 28))
        self.pushButton_angry.setObjectName("pushButton_angry")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My homework"))
        self.showGraphic.setText(_translate("MainWindow", "Запустить график"))
        self.btnShowData.setText(_translate("MainWindow", "Данные"))
        self.lblEmotions.setText(_translate("MainWindow", "Эмоции"))
        self.pushButton_happy.setText(_translate("MainWindow", "Веселый"))
        self.pushButton_sad.setText(_translate("MainWindow", "Грустный "))
        self.pushButton_angry.setText(_translate("MainWindow", "Злой"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
