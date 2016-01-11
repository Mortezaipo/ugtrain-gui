"""
Implement Directory abstract class.
"""
from BaseClass import BaseClass
import os


class Unix(BaseClass):

    def check_directory(self, path): #FIXME
        if os.path.exists(path):
            return True
        return False

    def create_directory(self, path): #FIXME
        if self.check_directory(path):
            os.mkdir(path)
            return True
        return False

    def crawl_directory(self, path): #FIXME
        if self.check_directory(path):
            return os.listdir(path)
        return False

    def delete_directory(self, path): #FIXME
        if self.check_directory(path):
            os.rmdir(path)
            return True
        return False

    def rename_directory(self, path, new_name): #FIXME
        if self.check_directory(path):
            os.rename(path, new_name)
            return True
        return False
