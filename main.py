import random
import sys

import data
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("word_trainer.ui", self)

        self.generate_day.clicked.connect(lambda: self.change_day())
        self.generate_month.clicked.connect(lambda: self.change_month())
        self.generate_season.clicked.connect(lambda: self.change_season())
        self.generate_number.clicked.connect(lambda: self.change_number())

    def change_day(self):
        word = random.choice(data.days_of_week)
        self.weekday.setText(word)

    def change_month(self):
        word = random.choice(data.months)
        self.month.setText(word)

    def change_season(self):
        word = random.choice(data.seasons)
        self.season.setText(word)

    def change_number(self):
        word = random.choice(list)
        self.number.setText(word)


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QMainWindow()
mainwindow.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
