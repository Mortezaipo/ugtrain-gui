"""QT Implementation of base class.
"""
from ui_base import UIBase
from PyQt5.QtWidgets import QApplication, QWidget
import sys


class QTBase(UIBase):
    a = None
    w = None

    def new_win(self, title=""):
        self.a = QApplication(sys.argv)
        self.w = QWidget()
        self.w.setWindowTitle(title)
        return self.w

    def new_textbox(self):
        pass

    def new_radiobox(self):
        pass

    def new_label(self):
        pass

    def new_checkbox(self):
        pass

    def show(self):
        self.w.show()
        sys.exit(self.a.exec_())