# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Source\miniprojects\part1\studyThread\threadApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        self.btnStart = QtWidgets.QPushButton(Form)
        self.btnStart.setGeometry(QtCore.QRect(30, 10, 81, 31))
        self.btnStart.setObjectName("btnStart")
        self.txbLog = QtWidgets.QTextBrowser(Form)
        self.txbLog.setGeometry(QtCore.QRect(30, 50, 271, 171))
        self.txbLog.setObjectName("txbLog")
        self.pgbTask = QtWidgets.QProgressBar(Form)
        self.pgbTask.setGeometry(QtCore.QRect(50, 230, 271, 23))
        self.pgbTask.setProperty("value", 24)
        self.pgbTask.setObjectName("pgbTask")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "thread test"))
        self.btnStart.setText(_translate("Form", "PushButton"))
