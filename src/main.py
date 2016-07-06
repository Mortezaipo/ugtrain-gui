#!/usr/bin/env python
import gtk
from general import General


class Main:
    
    def __init__(self):
        self.general = General()
        self.general.draw_gui()
        

if __name__ == "__main__":
    Main()
    gtk.main()
