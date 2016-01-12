"""
Implement File abstract class.
"""
from BaseClass import BaseClass
import os
import stat
import linecache


class File(BaseClass):

    __open_file__ = None

    def check_file(self, path): #FIXME
        if os.path.exists(path):
            return True
        return False

    def open_file(self, path, type): #FIXME
        if type not in ('r', 'w', 'b'):
            raise RuntimeError('Invalid type argument.')
        if not self.check_file(path):
            return False
        try:
            self.__open_file__ = open(path, type)
            return True
        except:
            return False

    def check_existance(self, path): #FIXME
        if os.path.exists(path):
            return True
        return False

    def check_permission(self, path, should_have): #FIXME
        perm = oct(stat.S_IMODE(os.lstat(path).st_mode))[1:]
        if perm == should_have:
            return True
        return False

    def read_line(self, path, line_number): #FIXME
        if not self.check_file(path):
            return False
        line_text = linecache.getline(path, line_number)
        return line_text

    def read_all(self): #FIXME
        if not self.__open_file__:
            return False
        read = self.__open_file__.xreadlines()
        return read

    def write_all(self, path, data): #FIXME
        if not self.check_file(path) and not self.open_file(path, 'w'):
            return False
        self.__open_file__.write(data)
        return True

    def update_line(self, path, line_number, data): #FIXME
        if not self.check_file(path) and not self.open_file(path):
            return False
        lines = self.__open_file__.readlines()
        lines[line_number] = data
        self.__open_file__.close()
        self.open_file(path,'w')
        self.__open_file__.writelines(lines)
        self.__open_file__.close()
        return True

    def rename_file(self, path, new_name): #FIXME
        if not self.check_file(path):
            return False
        try:
            os.rename(path, new_name)
            return True
        except:
            return False

    def delete_file(self, path): #FIXME
        if not check_file(path):
            return False
        try:
            os.unlink(path)
            return True
        except:
            return False

    def create_file(self, path): #FIXME
        if self.check_file(path):
            return False
        try:
            os.mknod(path)
            return True
        except:
            return False
