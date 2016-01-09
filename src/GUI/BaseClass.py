"""
Abstract class for Graphical user interface classes. #(under dev)
"""
from abc import ABCMeta, abstractmethod

class BaseClass(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_window(self):
        pass

    @abstractmethod
    def create_layout(self):
        pass

    @abstractmethod
    def create_input(self):
        pass

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def set_value(self):
        pass

    @abstractmethod
    def get_value(self):
        pass
