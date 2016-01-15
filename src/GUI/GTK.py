"""
Implement GUI abstract class.
"""
from BaseClass import BaseClass
import gtk


class GTK(BaseClass):
    
    _window = None
    _buttons = {}
    
    def create_window(self, width, height, title):
        self._window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self._window.set_size_request(width, height)
        self._window.set_position(gtk.WIN_POS_CENTER)
        self._window.set_title(title)
        self._window.connect("destroy", lambda a: gtk.main_quit())
        
    def create_layout(self):
        pass
    
    def create_input(self):
        pass
    
    def create_button(self, name, label, width=0, height=0, x=0, y=0):
        if not self._window:
            return False
        
        btn = gtk.Button(label)
        if width and height:
            btn.set_size_request(width, height)
            
        self._buttons.update({name:btn})
        
        fixed = gtk.Fixed()
        fixed.put(btn, x, y)
        self._window.add(fixed)
    
    def create_table(self, row, cell):
        pass
    
    def set_value(self, value):
        pass
    
    def get_value(self):
        pass
    
    def show_window(self):
        self._window.show_all()
        gtk.main()
        
    def set_event(self, element_name, event, action):
        element = self._buttons.get(element_name)
        if not element:
            return False
        element.connect(event, action, None)
        