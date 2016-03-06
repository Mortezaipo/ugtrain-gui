#!/usr/bin/env python

import gtk
import sys
from signals import Signals


class UG(gtk.Window):
    
    _vbox = {}
    _hbox = {}
    _btns = {}
    _entr = {}
    _lbls = {}
    
    def __init__(self):
        super(UG, self).__init__()
        
        # General Settings
        self.set_title("UGTrain GUI")
        self.set_size_request(600, 300)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(10)
        self.set_resizable(False)
        
        # Define Layouts
        self._hbox.update({'main_win': gtk.HBox(True, 0)})
        self._vbox.update({'main_win': gtk.VBox(True, 0)})
        game_table = gtk.Table(4, 2, True)
        settings_table = gtk.Table(3, 2, True)
        
        # Define Elements
        self.create_entries()
        self.create_buttons()
        self.create_checkboxes()
        self.create_labels()
        
        # Start The Game
        game_table.attach(self._lbls['Process name'], 0, 1, 0, 1)
        game_table.attach(self._entr['game_process_name'], 1, 2, 0, 1)
        game_table.attach(self._lbls['Process call'], 0, 1, 1, 2)
        game_table.attach(self._entr['game_process_call'], 1, 2, 1, 2)
        game_table.attach(self._lbls['Absolute path'], 0, 1, 2, 3)
        game_table.attach(self._entr['game_absolute_path'], 1, 2, 2, 3)
        game_table.attach(self._lbls['Params'], 0, 1, 3, 4)
        game_table.attach(self._entr['game_params'], 1, 2, 3, 4)
        
        # General Settings
        settings_table.attach(gtk.Label("Dynamic memory file:"), 0, 1, 0, 1)
        settings_table.attach(self._entr['dynamic_memory_file'], 1, 2, 0, 1)
        settings_table.attach(gtk.Label("Use GBT"), 0, 1, 1, 2)
        settings_table.attach(self._entr['use_gbt'], 1, 2, 1, 2)
        settings_table.attach(gtk.Label("Macro name"), 0, 1, 2, 3)
        settings_table.attach(self._entr['macro_name'], 1, 2, 2, 3)        
        
        # Join Layouts And Elements
        self._hbox['main_win'].pack_start(game_table, True, True, 0)
        self._hbox['main_win'].pack_end(settings_table, True, True, 0)
        self._vbox['main_win'].pack_start(self._hbox['main_win'], True, True, 0)
        self._vbox['main_win'].pack_end(self._btns['advanced'], False, False, 0)
        self.add(self._vbox['main_win'])
        
        # Signal
        self.connect("destroy", gtk.main_quit)
        
        self.show_all()
        gtk.main()
    
    def create_labels(self):
        list = ['Process name', 'Process call', 'Absolute path', 'Params']
        for i in list:
            l = gtk.Label(i)
            l.set_alignment(xalign=0, yalign=0)
            self._lbls.update({i:l})
        
    def create_buttons(self):
        list = [('advanced', 'Advanced Settings', self.show_mode_prompt),]
        for i,j,k in list:
            b = gtk.Button(j)
            b.connect("clicked", k)
            self._btns.update({i: b})
    
    def create_checkboxes(self):
        list = ['use_gbt',]
        for i in list:
            self._entr.update({i: gtk.CheckButton()})
        
    def create_entries(self):
        list = ['game_process_name', 'game_process_call', 'game_absolute_path', 'game_params', 'dynamic_memory_file', 'macro_name']
        for i in list:
            self._entr.update({i: gtk.Entry()})
        
    
    def show_mode_prompt(self, widget):
        win = gtk.Window()
        win.set_title("Select Type")
        win.set_size_request(300,100)
        win.show_all()
        win.connect("desctroy", gtk.main_quit)
        gtk.main()
        
UG()
