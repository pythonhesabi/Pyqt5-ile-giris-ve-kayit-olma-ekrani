# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lbl_isim = QtWidgets.QLabel(Form)
        self.lbl_isim.setGeometry(QtCore.QRect(80, 70, 71, 31))
        self.lbl_isim.setObjectName("lbl_isim")
        self.lbl_sifre = QtWidgets.QLabel(Form)
        self.lbl_sifre.setGeometry(QtCore.QRect(90, 120, 47, 13))
        self.lbl_sifre.setObjectName("lbl_sifre")
        self.pushButton_giris_yap = QtWidgets.QPushButton(Form)
        self.pushButton_giris_yap.setGeometry(QtCore.QRect(180, 150, 75, 23))
        self.pushButton_giris_yap.setObjectName("pushButton_giris_yap")
        self.pushButton_kaydol = QtWidgets.QPushButton(Form)
        self.pushButton_kaydol.setGeometry(QtCore.QRect(180, 200, 75, 23))
        self.pushButton_kaydol.setObjectName("pushButton_kaydol")
        self.lineEdit_isim = QtWidgets.QLineEdit(Form)
        self.lineEdit_isim.setGeometry(QtCore.QRect(160, 70, 113, 20))
        self.lineEdit_isim.setObjectName("lineEdit_isim")
        self.lineEdit_sifre = QtWidgets.QLineEdit(Form)
        self.lineEdit_sifre.setGeometry(QtCore.QRect(160, 110, 113, 20))
        self.lineEdit_sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_sifre.setObjectName("lineEdit_sifre")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_isim.setText(_translate("Form", "Kullanici Adi"))
        self.lbl_sifre.setText(_translate("Form", "Sifre"))
        self.pushButton_giris_yap.setText(_translate("Form", "Giris Yap"))
        self.pushButton_kaydol.setText(_translate("Form", "Kaydol"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())