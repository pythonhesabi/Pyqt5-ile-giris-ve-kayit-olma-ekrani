
from pyqt5_projeleri.giris_kayit_ekrani.giris import *
from PyQt5.QtWidgets import *
from pyqt5_projeleri.giris_kayit_ekrani.ui_kayit_ol import Ui_Form
import sys


class kayitOl_sinifi(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_Kayit_ol.clicked.connect(self.kayit_kontrol)
        self.pushButton_Geri_git.clicked.connect(self.giris_fonk)

    def kayit_kontrol(self):
        kayit_isim = self.lineEdit_isim
        kayit_soyisim = self.lineEdit_soyisim
        kayit_dogum_tarihi = self.lineEdit_dogum_tarihi
        kayit_dogum_yeri = self.lineEdit_dogum_yeri
        kayit_tc_no = self.lineEdit_tc_no
        kayit_tel_no = self.lineEdit_tel_no
        kayit_erkek = self.radioButton_erkek
        kayit_kadin = self.radioButton_kadin
        kayit_sifre = self.lineEdit_kayit_sifre



    def giris_fonk(self):
        self.hide()
        self.giris_degiskeni=giris_sinifi()
        self.giris_degiskeni.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ekran = kayitOl_sinifi()
    ekran.show()

    sys.exit(app.exec_())
