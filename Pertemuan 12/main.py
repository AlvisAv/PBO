import sys
from PyQt5 import QtWidgets
from skor import Ui_MainWindow

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.tambah_skor_a)
        self.pushButton_2.clicked.connect(self.tambah_skor_b)
        self.pushButton_3.clicked.connect(self.cek_skor)
        self.pushButton_4.clicked.connect(self.reset_skor)

    def tambah_skor_a(self):
        skor_a = int(self.label.text())
        skor_a+=1
        self.label.setText(str(skor_a))

    def tambah_skor_b(self):
        skor_b = int(self.label_2.text())
        skor_b+=1
        self.label_2.setText(str(skor_b))

    def cek_skor(self):
        skor_a = int(self.label.text())
        skor_b = int(self.label_2.text())
        if skor_a > skor_b:
            self.label_3.setText('Tim A menang')
        elif skor_b > skor_a:
            self.label_3.setText('Tim B menang')
        else:
            self.label_3.setText('Seri')

    def reset_skor(self):
        self.label.setText('0')
        self.label_2.setText('0')
        self.label_3.setText('')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
