"""
Abstract class for Directory classes. #(under dev)
"""

from abc import ABCMeta, abstractmethod

class BaseClass(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_directory(self):
        pass

    @abstractmethod
    def crawl_directory(self):
        pass

    @abstractmethod
    def delete_directory(self):
        pass

    @abstractmethod
    def rename_directory(self):
        pass
