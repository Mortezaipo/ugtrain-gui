import gtk


class General(gtk.Window):
    
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

        # Table for main window
        main_table = gtk.Table(3, 1, False)
        self.sg_table = gtk.Table(4, 2, False)
        self.gs_table = gtk.Table(3, 2, False)
        
        self.draw_start_game()
        self.draw_general_settings()
        # Frame for start game and general settings
        sg = gtk.Frame("Start game")
        gs = gtk.Frame("General settings")
        
        # Connect items
        sg.add(self.sg_table)
        gs.add(self.gs_table)
        main_table.attach(sg, 0, 1, 0, 1)
        main_table.attach(gs, 0, 1, 1, 2)
        self.add(main_table)
        
        self.connect("destroy", gtk.main_quit)
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