import gtk
from dynamic import Dynamic
from pointer import Pointer
from static import Static


class General(gtk.Window):
    
    mode = None
    
    sg_elements = {'Process name': gtk.Entry(),
                   'Process call': gtk.Entry(),
                   'Absolute path': gtk.Entry(),
                   'Params': gtk.Entry()
                   }
    
    gs_elements = {'Mem file': gtk.Entry(),
                'Use GBT': gtk.CheckButton(),
                'Macro name': gtk.Entry()
                }
    
    def draw_gui(self):
        super(General, self).__init__()
        
        # Set window settings
        self.set_title("UGTrain - General")
        self.set_size_request(320, 370)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(10)

        # Manu for main window
        main_menu = gtk.MenuBar()
        file_menu = gtk.Menu()
        setting_menu = gtk.Menu()
        
        m_file = gtk.MenuItem("File")
        m_new = gtk.MenuItem("New")
        m_open = gtk.MenuItem("Open")
        m_save = gtk.MenuItem("Save")
        m_exit = gtk.MenuItem("Exit")
        m_setting = gtk.MenuItem("Settings")
        m_static = gtk.MenuItem("Static")
        m_dynamic = gtk.MenuItem("Dynamic")
        m_pointer = gtk.MenuItem("Pointer")
        
        m_file.set_submenu(file_menu)
        m_setting.set_submenu(setting_menu)
        
        file_menu.append(m_new)
        file_menu.append(m_open)
        file_menu.append(m_save)
        file_menu.append(m_exit)
        
        setting_menu.append(m_static)
        setting_menu.append(m_dynamic)
        setting_menu.append(m_pointer)
        
        main_menu.append(m_file)
        main_menu.append(m_setting)

        # Table for main window
        main_table = gtk.Table(2, 1, False)
        main_table.set_row_spacings(10)
        self.sg_table = gtk.Table(4, 2, False)
        self.gs_table = gtk.Table(3, 2, False)

        # Frame for start game and general settings
        sg = gtk.Frame("Start game")
        gs = gtk.Frame("General settings")
        sg_box = gtk.HBox()
        gs_box = gtk.HBox()
        body_box = gtk.VBox(False, 2)
        
        # Connect items
        sg_box.pack_start(self.sg_table, padding=10)
        gs_box.pack_start(self.gs_table, padding=10)
        sg.add(sg_box)
        gs.add(gs_box)
        main_table.attach(sg, 0, 1, 0, 1)
        main_table.attach(gs, 0, 1, 1, 2)
        self.draw_start_game()
        self.draw_general_settings()
        
        body_box.pack_start(main_menu, False, False, 0)
        body_box.pack_end(main_table)
        self.add(body_box)

        self.connect("destroy", gtk.main_quit)
        m_exit.connect("activate", gtk.main_quit)
        m_static.connect("activate", self.draw_static_form)
        m_dynamic.connect("activate", self.draw_dynamic_form)
        m_pointer.connect("activate", self.draw_pointer_form)
        m_save.connect("activate", self.save_config_form)
        self.show_all()
        
    def draw_start_game(self):
        i = 0
        for label, element in self.sg_elements.items():
            self.sg_table.attach(gtk.Label(label), 0, 1, i, i+1)
            self.sg_table.attach(element, 1, 2, i, i+1)
            i+=1
            
    def draw_general_settings(self):
        i = 0
        for label, element in self.gs_elements.items():
            self.gs_table.attach(gtk.Label(label), 0, 1, i, i+1)
            self.gs_table.attach(element, 1, 2, i, i+1)
            i+=1
            
    def draw_static_form(self, widget):
        self.mode = Static()
    
    def draw_dynamic_form(self, widget):
        self.mode = Dynamic()
        
    def draw_pointer_form(self, widget):
        self.mode = Pointer()
            
    def save_config_form(self, widget):
        if self.mode:
            print self.mode.config_file_content
        else:
            print 'there is no config file! choice your config type.'