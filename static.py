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
        self.draw_labels()
        savebtn = gtk.Button("Save static data")
        fbox = gtk.Fixed()
        
        # Create List Store
        swin = gtk.ScrolledWindow()
        swin.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        self.lstore = gtk.ListStore(str, str, str, str, str, str)
        tree = gtk.TreeView(self.lstore)
        for i in range(6):
            row = gtk.CellRendererText()
            cell = gtk.TreeViewColumn("Arg %d" % i, row, text=0)
            tree.append_column(cell)
        
        # Connect elements to layouts
        swin.add(tree)
        fbox.put(savebtn, 0, 0)
        box.pack_start(self.setting, False, False, 0)
        box.pack_start(swin, True, True, 0)
        box.pack_end(fbox, False, False, 0)
        self.add(box)
        
        self.show_all()
        
    def draw_labels(self):
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
        for label, obj in elements:
            self.setting.attach(gtk.Label(label), i, i+1, 0, 1)
            self.setting.attach(obj, i, i+1, 1, 2)
            i+= 1