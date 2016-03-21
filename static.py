import gtk


class Static(gtk.Window):
    def __init__(self):
        super(Static, self).__init__()
        
        # Set window settings
        self.set_size_request(1120, 300)
        self.set_title("UGTrain - Static Form")
        self.set_border_width(10)
        
        # Create layouts
        box = gtk.VBox(False, 5)
        self.setting = gtk.Table(2, 7, False)
        self.setting.set_col_spacings(10)
        
        # Draw elements
        self.draw_elements()
        savebtn = gtk.Button("Save static data")
        addarg = gtk.Button("Add new args")
        fbox = gtk.Fixed()
        
        # Connect element to signals
        addarg.connect("clicked", self.new_data_win)
        
        # Create List Store
        swin = gtk.ScrolledWindow()
        swin.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        self.lstore = gtk.ListStore(str, str, str, str, str, str)
        self.tree = gtk.TreeView(self.lstore)
        self.tree.connect("row-activated", self.edit_list_item)
        for i in range(6):
            row = gtk.CellRendererText()
            cell = gtk.TreeViewColumn("Arg %d" % i, row, text=i)
            self.tree.append_column(cell)
        
        # Connect elements to layouts
        swin.add(self.tree)
        fbox.put(savebtn, 0, 0)
        fbox.put(addarg, 120, 0)
        box.pack_start(self.setting, False, False, 0)
        box.pack_start(swin, True, True, 0)
        box.pack_end(fbox, False, False, 0)
        self.add(box)
        
        self.show_all()
        
    def draw_elements(self):
        elements = (
                    ('Value name', gtk.Entry()),
                    ('Abs Address', gtk.Entry()),
                    ('Data Type', gtk.Entry()),
                    ('Check', gtk.CheckButton()),
                    ('Wish Value', gtk.Entry()),
                    ('Key Binding', gtk.Entry()),
                    ('Act State', gtk.Entry())
                   )
        i = 0
        for label, element in elements:
            self.setting.attach(gtk.Label(label), i, i+1, 0, 1)
            self.setting.attach(element, i, i+1, 1, 2)
            i+= 1
            
            
    def new_data_win(self, widget):
        new_data = gtk.Window()
        new_data.set_size_request(310, 450)
        new_data.set_border_width(10)
        
        # Create layouts
        box = gtk.VBox(False, 2)
        fbox = gtk.Fixed()
        abox = gtk.HBox()
        cbox = gtk.HBox()
        self.arg_table = gtk.Table(5, 2, False)
        self.arg_table.set_row_spacings(5)
        self.check_table = gtk.Table(6, 2, False)
        self.check_table.set_row_spacings(5)
        arg_frame = gtk.Frame('Argument')
        chk_frame = gtk.Frame('Check')
        
        # Create elements
        save_btn = gtk.Button('Add')
        save_btn.connect("clicked", self.add_list_item)
        self.draw_new_data_elements()
        
        # Attach elements to layouts
        abox.pack_start(self.arg_table, padding=10)
        cbox.pack_start(self.check_table, padding=10)
        arg_frame.add(abox)
        chk_frame.add(cbox)
        fbox.put(save_btn, 0, 0)
        box.pack_start(arg_frame)
        box.pack_start(chk_frame)
        box.pack_end(fbox)
        new_data.add(box)
        new_data.show_all()
        
        
    def draw_new_data_elements(self):
        self.arg_elements = (
            ('Val name', gtk.Entry()),
            ('Abs address', gtk.Entry()),
            ('Data type', gtk.Entry()), #FIXME: should change to select box
            ('Check', gtk.CheckButton()),
            ('Watch', gtk.CheckButton()),
        )
        
        i = 0
        for label, element in self.arg_elements:
            self.arg_table.attach(gtk.Label(label), 0, 1, i, i+1)
            self.arg_table.attach(element, 1, 2, i, i+1)
            i += 1
            
            
        c1 = gtk.combo_box_new_text()
        c1.append_text('I')
        c1.append_text('G')
        c1.append_text('E')
        
        c2 = gtk.combo_box_new_text()
        c2.append_text('Futhur')
        c2.append_text('Check')
        
        self.check_elements = (
            ('Check', gtk.CheckButton()),
            ('Abs address', gtk.Entry()),
            ('Data type', gtk.Entry()), #FIXME: should change to select box
            ('', c1),
            ('Check value', gtk.CheckButton()),
            ('', c2),
        )
        
        i = 0
        for label, element in self.check_elements:
            self.check_table.attach(gtk.Label(label), 0, 1, i, i+1)
            self.check_table.attach(element, 1, 2, i, i+1)
            i += 1

    def add_list_item(self, widget):
        self.lstore.append((self.arg_elements[0][1].get_text(),
                            self.arg_elements[1][1].get_text(),
                            self.arg_elements[2][1].get_text(),
                            str(self.arg_elements[3][1].get_active()),
                            str(self.arg_elements[4][1].get_active()),
                            '',
                            ))
        
        self.lstore.append((str(self.check_elements[0][1].get_active()),
                            self.check_elements[1][1].get_text(),
                            self.check_elements[2][1].get_text(),
                            self.check_elements[3][1].get_active_text(),
                            str(self.check_elements[4][1].get_active()),
                            self.check_elements[5][1].get_active_text(),                            
                            ))
        
    def edit_list_item(self, widget, row, col):
        widget = widget.get_model()
        print widget[row][0]