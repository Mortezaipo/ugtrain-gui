"""
Abstract class for File I/O classes. #(under dev)
"""

from abc import ABCMeta, abstractmethod

class BaseClass(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def check_existance(self):
        pass

    @abstractmethod
    def check_permission(self):
        pass

    @abstractmethod
    def read_line(self):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def write_all(self):
        pass

    @abstractmethod
    def update_line(self):
        pass

    @abstractmethod
    def rename_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass

    @abstractmethod
    def create_file(self):
        pass
