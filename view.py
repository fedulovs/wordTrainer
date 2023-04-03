import random
import re
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi

from data import words

word_set = None
word = None
answer = None
true_set = []


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("layouts/main_menu.ui", self)

        self.months.clicked.connect(lambda: self.prepare_trainer(words.months))
        self.seasons.clicked.connect(lambda: self.prepare_trainer(words.seasons))
        self.week_days.clicked.connect(lambda: self.prepare_trainer(words.days_of_week))
        self.colors.clicked.connect(lambda: self.prepare_trainer(words.colors))
        self.food.clicked.connect(lambda: self.prepare_trainer(words.food))
        self.family.clicked.connect(lambda: self.prepare_trainer(words.family))
        self.adjectives.clicked.connect(lambda: self.prepare_trainer(words.adjectives))

    def prepare_trainer(self, topic):
        global word_set
        word_set = topic
        self.open_trainer()

    def open_trainer(self):
        trainer_window = TrainerWindow()
        widget.addWidget(trainer_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class TrainerWindow(QMainWindow):
    def __init__(self):
        super(TrainerWindow, self).__init__()
        loadUi("layouts/word_trainer.ui", self)

        self.generate.clicked.connect(lambda: self.change_word(true_set))
        self.show_answer_btn.clicked.connect(lambda: self.show_answer())

        self.back_button.setIcon(QIcon('icons/arrow-left.svg'))
        self.back_button.clicked.connect(lambda: self.go_back())

        self.get_words('questions.txt')

    def get_words(self, file):
        global true_set
        with open(file, encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = re.sub(r"[\n\t]*", "", line)
                line = line.split('-')
                true_set.append(line)
        print(true_set)

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
