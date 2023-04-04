import random
import re
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi

word_set = []
word = None
answer = None


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("layouts/main_menu.ui", self)

        self.months.clicked.connect(lambda: self.get_words('topics/months.txt'))
        self.seasons.clicked.connect(lambda: self.get_words('topics/seasons.txt'))
        self.week_days.clicked.connect(lambda: self.get_words('topics/weekdays.txt'))
        self.colors.clicked.connect(lambda: self.get_words('topics/colors.txt'))
        self.food.clicked.connect(lambda: self.get_words('topics/food.txt'))
        self.family.clicked.connect(lambda: self.get_words('topics/family.txt'))
        self.adjectives.clicked.connect(lambda: self.get_words('topics/adjectives.txt'))

    def get_words(self, file):
        global word_set
        word_set.clear()
        with open(file, encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = re.sub(r"[\n\t]*", "", line)
                line = line.split('-')
                word_set.append(line)
        self.open_trainer()

    def open_trainer(self):
        trainer_window = TrainerWindow()
        widget.addWidget(trainer_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class TrainerWindow(QMainWindow):
    def __init__(self):
        super(TrainerWindow, self).__init__()
        loadUi("layouts/word_trainer.ui", self)

        self.generate.clicked.connect(lambda: self.change_word(word_set))
        self.show_answer_btn.clicked.connect(lambda: self.show_answer())

        self.back_button.setIcon(QIcon('icons/arrow-left.svg'))
        self.back_button.clicked.connect(lambda: self.go_back())

    def change_word(self, topic):
        global word, answer
        batch = random.choice(topic)
        word = batch[0]
        answer = batch[1]
        self.word_label.setText(word)

    def show_answer(self):
        self.word_label.setText(answer)

    def go_back(self):
        print("Going back to main menu")
        main_window = MainWindow()
        widget.addWidget(main_window)
        widget.setFixedHeight(800)
        widget.setFixedWidth(1200)
        widget.setCurrentIndex(widget.currentIndex() + 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_menu = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_menu)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
