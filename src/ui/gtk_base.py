"""GTK Implementation of base class.
"""
from ui_base import UIBase
import gtk  # FIXME: handle not found package.


class GtkBase(UIBase):
    w = None

    def new_win(self, title=""):
        self.w = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.w.set_title(title)
        return self.w

    def new_textbox(self):
        pass

    def new_label(self):
        pass

    def new_checkbox(self):
        pass

    def new_radiobox(self):
        pass

    def show(self):
        self.w.show_all()
        gtk.main()