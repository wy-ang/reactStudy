# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reactStudy.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReactStudy(object):
    def setupUi(self, ReactStudy):
        ReactStudy.setObjectName("ReactStudy")
        ReactStudy.resize(391, 363)
        ReactStudy.setMinimumSize(QtCore.QSize(391, 363))
        ReactStudy.setMaximumSize(QtCore.QSize(391, 363))
        ReactStudy.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stateGroupBox = QtWidgets.QGroupBox(ReactStudy)
        self.stateGroupBox.setGeometry(QtCore.QRect(10, 10, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.stateGroupBox.setFont(font)
        self.stateGroupBox.setObjectName("stateGroupBox")
        self.stateText = QtWidgets.QLabel(self.stateGroupBox)
        self.stateText.setGeometry(QtCore.QRect(20, 25, 54, 20))
        self.stateText.setMinimumSize(QtCore.QSize(0, 20))
        self.stateText.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.stateText.setFont(font)
        self.stateText.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.stateText.setWordWrap(False)
        self.stateText.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.stateText.setObjectName("stateText")
        self.stateColor = QtWidgets.QLabel(self.stateGroupBox)
        self.stateColor.setGeometry(QtCore.QRect(80, 25, 20, 20))
        self.stateColor.setMinimumSize(QtCore.QSize(20, 20))
        self.stateColor.setMaximumSize(QtCore.QSize(20, 20))
        self.stateColor.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.stateColor.setText("")
        self.stateColor.setObjectName("stateColor")
        self.aggGroupBox = QtWidgets.QGroupBox(ReactStudy)
        self.aggGroupBox.setGeometry(QtCore.QRect(230, 80, 151, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.aggGroupBox.setFont(font)
        self.aggGroupBox.setObjectName("aggGroupBox")
        self.updateBtn = QtWidgets.QPushButton(self.aggGroupBox)
        self.updateBtn.setGeometry(QtCore.QRect(10, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.updateBtn.setFont(font)
        self.updateBtn.setObjectName("updateBtn")
        self.buildBtn = QtWidgets.QPushButton(self.aggGroupBox)
        self.buildBtn.setGeometry(QtCore.QRect(80, 30, 61, 31))
        self.buildBtn.setObjectName("buildBtn")
        self.switchGroupBox = QtWidgets.QGroupBox(ReactStudy)
        self.switchGroupBox.setGeometry(QtCore.QRect(130, 10, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.switchGroupBox.setFont(font)
        self.switchGroupBox.setObjectName("switchGroupBox")
        self.startBtn = QtWidgets.QPushButton(self.switchGroupBox)
        self.startBtn.setEnabled(True)
        self.startBtn.setGeometry(QtCore.QRect(10, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.startBtn.setFont(font)
        self.startBtn.setToolTip("")
        self.startBtn.setWhatsThis("")
        self.startBtn.setStyleSheet("")
        self.startBtn.setFlat(False)
        self.startBtn.setObjectName("startBtn")
        self.stopBtn = QtWidgets.QPushButton(self.switchGroupBox)
        self.stopBtn.setGeometry(QtCore.QRect(90, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.stopBtn.setFont(font)
        self.stopBtn.setObjectName("stopBtn")
        self.restartBtn = QtWidgets.QPushButton(self.switchGroupBox)
        self.restartBtn.setGeometry(QtCore.QRect(170, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.restartBtn.setFont(font)
        self.restartBtn.setObjectName("restartBtn")
        self.infoGroupBox = QtWidgets.QGroupBox(ReactStudy)
        self.infoGroupBox.setEnabled(True)
        self.infoGroupBox.setGeometry(QtCore.QRect(10, 80, 211, 271))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.infoGroupBox.setFont(font)
        self.infoGroupBox.setObjectName("infoGroupBox")
        self.msgView = QtWidgets.QTextEdit(self.infoGroupBox)
        self.msgView.setEnabled(True)
        self.msgView.setGeometry(QtCore.QRect(10, 20, 191, 241))
        self.msgView.setUndoRedoEnabled(True)
        self.msgView.setReadOnly(True)
        self.msgView.setObjectName("msgView")
        self.groupBox = QtWidgets.QGroupBox(ReactStudy)
        self.groupBox.setGeometry(QtCore.QRect(230, 170, 151, 121))
        self.groupBox.setObjectName("groupBox")
        self.pathConfigBtn = QtWidgets.QPushButton(self.groupBox)
        self.pathConfigBtn.setGeometry(QtCore.QRect(10, 30, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.pathConfigBtn.setFont(font)
        self.pathConfigBtn.setObjectName("pathConfigBtn")
        self.portBtn = QtWidgets.QPushButton(self.groupBox)
        self.portBtn.setGeometry(QtCore.QRect(10, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.portBtn.setFont(font)
        self.portBtn.setObjectName("portBtn")

        self.retranslateUi(ReactStudy)
        self.startBtn.clicked.connect(ReactStudy.clickStartBtn)
        self.stopBtn.clicked.connect(ReactStudy.clickStopBtn)
        self.restartBtn.clicked.connect(ReactStudy.clickRestartBtn)
        self.buildBtn.clicked.connect(ReactStudy.clickBuildBtn)
        self.updateBtn.clicked.connect(ReactStudy.clickUpdateBtn)
        self.pathConfigBtn.clicked.connect(ReactStudy.clickPathConfigBtn)
        QtCore.QMetaObject.connectSlotsByName(ReactStudy)
        ReactStudy.setTabOrder(self.startBtn, self.stopBtn)
        ReactStudy.setTabOrder(self.stopBtn, self.restartBtn)
        ReactStudy.setTabOrder(self.restartBtn, self.updateBtn)
        ReactStudy.setTabOrder(self.updateBtn, self.buildBtn)

    def retranslateUi(self, ReactStudy):
        _translate = QtCore.QCoreApplication.translate
        ReactStudy.setWindowTitle(_translate("ReactStudy", "reactStudy 1.0"))
        self.stateGroupBox.setTitle(_translate("ReactStudy", "运行状态"))
        self.stateText.setText(_translate("ReactStudy", "note:"))
        self.aggGroupBox.setTitle(_translate("ReactStudy", "更新/构建"))
        self.updateBtn.setText(_translate("ReactStudy", "更新"))
        self.buildBtn.setText(_translate("ReactStudy", "构建"))
        self.switchGroupBox.setTitle(_translate("ReactStudy", "react 启停"))
        self.startBtn.setText(_translate("ReactStudy", "启动"))
        self.stopBtn.setText(_translate("ReactStudy", "停止"))
        self.restartBtn.setText(_translate("ReactStudy", "重启"))
        self.infoGroupBox.setTitle(_translate("ReactStudy", "提示信息"))
        self.msgView.setHtml(_translate("ReactStudy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.groupBox.setTitle(_translate("ReactStudy", "配置路径"))
        self.pathConfigBtn.setText(_translate("ReactStudy", "路径配置"))
        self.portBtn.setText(_translate("ReactStudy", "端口配置"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReactStudy = QtWidgets.QWidget()
    ui = Ui_ReactStudy()
    ui.setupUi(ReactStudy)
    ReactStudy.show()
    sys.exit(app.exec_())