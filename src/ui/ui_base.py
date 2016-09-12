"""User interface abstract class.
"""
from abc import ABCMeta, abstractmethod


class UIBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def new_win(self, title=""):
        pass

    @abstractmethod
    def new_textbox(self):
        pass

    @abstractmethod
    def new_label(self):
        pass

    @abstractmethod
    def new_checkbox(self):
        pass

    @abstractmethod
    def new_radiobox(self):
        pass

    @abstractmethod
    def show(self):
        pass
