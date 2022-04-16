from kaydol import *
from PyQt5.QtWidgets import *
from pyqt5_projeleri.giris_kayit_ekrani.ui_giris import Ui_Form
import sys


class giris_sinifi(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('giris ekrani')
        self.pushButton_giris_yap.clicked.connect(self.kontrol)
        self.pushButton_kaydol.clicked.connect(self.kayit_penceresi)

    def kontrol(self):
        eposta ="ornek"
        sifre="123"
        k_eposta = self.lineEdit_isim.text()
        k_sifre = self.lineEdit_sifre.text()

        if k_eposta == eposta and k_sifre == sifre:
            print("başarili")
        elif k_eposta == "eposta" or k_sifre == "sifre":
            print("ikisiniden biri yanlış")
        else:
            print("hata")

    def kayit_penceresi(self):
        self.hide()
        self.kayit_degiskeni = kayitOl_sinifi()
        self.kayit_degiskeni.show()


if __name__ == '__main__':
    uygulama = QApplication(sys.argv)
    form = giris_sinifi()
    form.show()

    sys.exit(uygulama.exec_())
