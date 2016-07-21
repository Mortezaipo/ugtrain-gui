"""General part for 'Start Game' and 'General Settings'.
"""
import gtk
import settings
import lib
from dynamic import Dynamic
from pointer import Pointer
from static import Static


class General(gtk.Window):
    mode = None
    start_game_elements = (
        ('Process name', gtk.Entry()),
        ('Process call', gtk.Entry()),
        ('Absolute path', gtk.Entry()),
        ('Params', gtk.Entry())
    )
    general_settings_elements = (
        ('Mem file', gtk.Entry()),
        ('Use GBT', gtk.CheckButton()),
        ('Macro name', gtk.Entry())
    )
    
    def draw_gui(self):
        """Draw GUI for General settings part."""
        super(General, self).__init__()
        
        # Set window settings
        self.set_size_request(320, 370)
        self.set_title(settings.window_title.format("General"))
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(settings.window_border)
        self.set_icon_from_file(settings.window_icon)

        # Draw menu for main window
        main_menu = gtk.MenuBar()
        file_menu = gtk.Menu()
        setting_menu = gtk.Menu()
        # Menu list
        menu_file = gtk.MenuItem("File")
        menu_new = gtk.MenuItem("New")
        menu_open = gtk.MenuItem("Open")
        menu_save = gtk.MenuItem("Save")
        menu_exit = gtk.MenuItem("Exit")
        menu_setting = gtk.MenuItem("Settings")
        menu_static = gtk.MenuItem("Static")
        menu_dynamic = gtk.MenuItem("Dynamic")
        menu_pointer = gtk.MenuItem("Pointer")
        # Connect sub menu
        menu_file.set_submenu(file_menu)
        menu_setting.set_submenu(setting_menu)
        # Connect menu with each other
        file_menu.append(menu_new)
        file_menu.append(menu_open)
        file_menu.append(menu_save)
        file_menu.append(menu_exit)
        setting_menu.append(menu_static)
        setting_menu.append(menu_dynamic)
        setting_menu.append(menu_pointer)
        main_menu.append(menu_file)
        main_menu.append(menu_setting)
        # Bind menu to functions
        self.connect("destroy", gtk.main_quit)
        menu_exit.connect("activate", gtk.main_quit)
        menu_static.connect("activate", self.draw_static_form)
        menu_dynamic.connect("activate", self.draw_dynamic_form)
        menu_pointer.connect("activate", self.draw_pointer_form)
        menu_save.connect("activate", self.save_config_form)

        # Table for main window
        main_table = gtk.Table(2, 1, False)
        main_table.set_row_spacings(10)
        self.start_game_table = gtk.Table(4, 2, False)
        self.general_settings_table = gtk.Table(3, 2, False)

        # Frame for start game and general settings
        start_game_frame = gtk.Frame("Start game")
        general_settings_frame = gtk.Frame("General settings")
        start_game_box = gtk.HBox()
        general_settings_box = gtk.HBox()
        body_box = gtk.VBox(False, 2)
        
        # Connect items
        start_game_box.pack_start(self.start_game_table, padding=10)
        general_settings_box.pack_start(self.general_settings_table, padding=10)
        start_game_frame.add(start_game_box)
        general_settings_frame.add(general_settings_box)
        main_table.attach(start_game_frame, 0, 1, 0, 1)
        main_table.attach(general_settings_frame, 0, 1, 1, 2)
        self.draw_start_game()
        self.draw_general_settings()
        body_box.pack_start(main_menu, False, False, 0)
        body_box.pack_end(main_table)
        self.add(body_box)

        self.show_all()
        gtk.main()

    def draw_start_game(self):
        i = 0
        for label, element in self.start_game_elements:
            self.start_game_table.attach(gtk.Label(label), 0, 1, i, i+1)
            self.start_game_table.attach(element, 1, 2, i, i+1)
            i += 1
            
    def draw_general_settings(self):
        i = 0
        for label, element in self.general_settings_elements:
            self.general_settings_table.attach(gtk.Label(label), 0, 1, i, i+1)
            self.general_settings_table.attach(element, 1, 2, i, i+1)
            i += 1
            
    def draw_static_form(self, widget):
        if self.mode:
            user_action = lib.prompt(self, "Are you sure about 'static' type?\nOther type data will be destroy!")
            if user_action:
                # self.mode.destroy() # FIXME
                self.mode = Static()
            return
        self.mode = Static()
    
    def draw_dynamic_form(self, widget):
        if self.mode:
            user_action = lib.prompt(self, "Are you sure about 'dynamic' type?\nOther type data will be destroy!")
            if user_action:
                # self.mode.destroy() # FIXME
                self.mode = Dynamic()
            return
        self.mode = Dynamic()
        
    def draw_pointer_form(self, widget):
        if self.mode:
            user_action = lib.prompt(self, "Are you sure about 'pointer' type?\nOther type data will be destroy!")
            if user_action:
                # self.mode.destroy() # FIXME
                self.mode = Pointer()
            return
        self.mode = Pointer()
            
    def save_config_form(self, widget): # FIXME: this action should be handled by data.py.
        if self.mode:
            print self.mode.config_file_content
        else:
            print 'there is no config file! choice your config type.'