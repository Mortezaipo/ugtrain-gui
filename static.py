import gtk
import settings


class Static(gtk.Window):
    """Static window."""
    
    # Edit mode for editing list items.
    edit_mode = None
    
    # Final config data
    config_file_content = ""
    
    def __init__(self):
        super(Static, self).__init__()
        
        # Set window settings
        self.set_size_request(1120, 300)
        self.set_title("UGTrain - Static Form")
        self.set_border_width(settings.window_border)
        
        # Create layouts
        box = gtk.VBox(False, 5)
        self.setting_table = gtk.Table(2, 7, False)
        self.setting_table.set_col_spacings(settings.table_col_space)
        
        # Draw elements
        #self.define_elements()
        
        # Define Config elements
        self.conf_elements = (
                    ('Value name', gtk.Entry()),
                    ('Abs Address', gtk.Entry()),
                    ('Data Type', gtk.Entry()),
                    ('Check', gtk.CheckButton()),
                    ('Wish Value', gtk.Entry()),
                    ('Key Binding', gtk.Entry()),
                    ('Act State', gtk.Entry()),
        )
        
        i = 0
        for label, element in self.conf_elements:
            self.setting_table.attach(gtk.Label(label), i, i+1, 0, 1)
            self.setting_table.attach(element, i, i+1, 1, 2)
            i += 1
        
        save_btn = gtk.Button("Save static data")
        add_arg = gtk.Button("Add new args")
        fix = gtk.Fixed()
        
        # Connect element to signals
        add_arg.connect("clicked", self.data_win)
        save_btn.connect("clicked", self.save_config)
        
        # Create List Store
        scrolled_win = gtk.ScrolledWindow()
        scrolled_win.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        self.list_store = gtk.ListStore(str, str, str, str, str, str)
        self.tree = gtk.TreeView(self.list_store)
        self.tree.connect("row-activated", self.edit_data_win)
        for i in range(6):
            row = gtk.CellRendererText()
            cell = gtk.TreeViewColumn("Arg %d" % i, row, text=i)
            self.tree.append_column(cell)
        
        # Connect elements to layouts
        scrolled_win.add(self.tree)
        fix.put(save_btn, 0, 0)
        fix.put(add_arg, 120, 0)
        box.pack_start(self.setting_table, False, False, 0)
        box.pack_start(scrolled_win, True, True, 0)
        box.pack_end(fix, False, False, 0)
        self.add(box)
        self.show_all()
        
    def define_elements(self, form_data=None):
        """Declare all required elements - Config, Argument, Check elements."""
        
        # Define data
        self.data_types = ['i8', 'i16', 'i32', 'i64', 'u8', 'u16', 'u32', 'u64', 'f32', 'f64']
        self.compare_types = ['I', 'G', 'E']
        self.other_data_types = ['Futhur', 'Check']
                
        # Define Argument elements
        self.arg_elements = (
                ('a1', gtk.Label('Val name *'), gtk.Entry()),
                ('a2', gtk.Label('Abs address *'), gtk.Entry()),
                ('a3', gtk.Label('Data type *'), gtk.combo_box_new_text()),
                ('a4', gtk.Label('Check'), gtk.CheckButton()),
                ('a5', gtk.Label('Watch'), gtk.CheckButton()),
        )
        
        self.check_elements = (
                ('c1', gtk.Label('Check'), gtk.CheckButton()),
                ('c2', gtk.Label('Abs address *'), gtk.Entry()),
                ('c3', gtk.Label('Data type *'), gtk.combo_box_new_text()),
                ('c4', gtk.Label('*'), gtk.combo_box_new_text()),
                ('c5', gtk.Label('Check value'), gtk.CheckButton()),
                ('c6', gtk.Label('*'), gtk.combo_box_new_text()),
        )
        
        for i in self.data_types:
            self.arg_elements[2][2].append_text(i)
            self.check_elements[2][2].append_text(i)
        
        for i in self.compare_types:
            self.check_elements[3][2].append_text(i)
        
        for i in self.other_data_types:
            self.check_elements[5][2].append_text(i)
        
        if form_data:
            self.arg_elements[0][2].set_text(form_data[0])
            self.arg_elements[1][2].set_text(form_data[1])
            if form_data[2] != None:
                self.arg_elements[2][2].set_active(self.data_types.index(form_data[2]))
            if form_data[3] == 'True':
                self.arg_elements[3][2].set_active(1)
            if form_data[4] == 'True':
                self.arg_elements[4][2].set_active(1)
                
            if form_data[5] == 'True':
                self.check_elements[0][2].set_active(1);
            self.check_elements[1][2].set_text(form_data[6])
            if form_data[7] != None:
                self.check_elements[2][2].set_active(self.data_types.index(form_data[7]))
            if form_data[8] != None:
                self.check_elements[3][2].set_active(self.compare_types.index(form_data[8]))
            if form_data[9] == 'True':
                self.check_elements[4][2].set_active(1)
            if form_data[10] != None:
                self.check_elements[5][2].set_active(self.other_data_types.index(form_data[10]))

    def data_win(self, widget=None, form_data=None):
        """Data window to add/edit list items."""
        
        # Create window
        data_win = gtk.Window()
        data_win.set_size_request(310, 480)
        data_win.set_border_width(10)
        data_win.connect("destroy", self.close_data_win)
        
        # Create layouts
        box = gtk.VBox(False, 2)
        fix = gtk.Fixed()
        abox = gtk.HBox()
        cbox = gtk.HBox()
        self.arg_table = gtk.Table(5, 2, False)
        self.arg_table.set_row_spacings(settings.table_row_space)
        self.check_table = gtk.Table(6, 2, False)
        self.check_table.set_row_spacings(settings.table_row_space)
        arg_frame = gtk.Frame('Argument')
        chk_frame = gtk.Frame('Check')
        
        if self.edit_mode:
            save_btn = gtk.Button('Update')
            save_btn.connect("clicked", self.save_list_item)
        else:
            save_btn = gtk.Button('Add')
            save_btn.connect("clicked", self.save_list_item)
        
        if not self.edit_mode:
            self.define_elements()
        else:
            self.define_elements(form_data)
            
        i = 0
        for _, label, element in self.arg_elements:
            self.arg_table.attach(label, 0, 1, i, i+1)
            self.arg_table.attach(element, 1, 2, i, i+1)
            i += 1
        i = 0
        for _, label, element in self.check_elements:
            self.check_table.attach(label, 0, 1, i, i+1)
            self.check_table.attach(element, 1, 2, i, i+1)
            i += 1
        
        # Attach elements to layouts
        abox.pack_start(self.arg_table, padding=10)
        cbox.pack_start(self.check_table, padding=10)
        arg_frame.add(abox)
        chk_frame.add(cbox)
        fix.put(save_btn, 0, 0)
        box.pack_start(arg_frame)
        box.pack_start(chk_frame)
        box.pack_end(fix)
        data_win.add(box)
        data_win.show_all()
        
    def close_data_win(self, widget):
        self.edit_mode = None
        widget.do_destroy
        
    def save_list_item(self, widget):
        if not self.validate_fields():
            return False
        
        # New data
        if not self.edit_mode: 
            self.list_store.append((
                                self.arg_elements[0][2].get_text(),
                                self.arg_elements[1][2].get_text(),
                                self.arg_elements[2][2].get_active_text(),
                                str(self.arg_elements[3][2].get_active()),
                                str(self.arg_elements[4][2].get_active()),
                                '',
                                ))
            
            self.list_store.append((
                                str(self.check_elements[0][2].get_active()),
                                self.check_elements[1][2].get_text(),
                                self.check_elements[2][2].get_active_text(),
                                self.check_elements[3][2].get_active_text(),
                                str(self.check_elements[4][2].get_active()),
                                self.check_elements[5][2].get_active_text(),
                                ))
            return True
        
        # Update data
        if self.edit_mode[0] % 2 == 0:
            arg_row = self.edit_mode[0]
            check_row = self.edit_mode[0] + 1
        else:
            arg_row = self.edit_mode[0] - 1
            check_row = self.edit_mode[0]
        
        self.list_store[arg_row][0] = self.arg_elements[0][2].get_text()
        self.list_store[arg_row][1] = self.arg_elements[1][2].get_text()
        self.list_store[arg_row][2] = self.arg_elements[2][2].get_active_text()
        self.list_store[arg_row][3] = self.arg_elements[3][2].get_active()
        self.list_store[arg_row][4] = self.arg_elements[4][2].get_active()

        self.list_store[check_row][0] = self.check_elements[0][2].get_active()
        self.list_store[check_row][1] = self.check_elements[1][2].get_text()
        self.list_store[check_row][2] = self.check_elements[2][2].get_active_text()
        self.list_store[check_row][3] = self.check_elements[3][2].get_active_text()
        self.list_store[check_row][4] = self.check_elements[4][2].get_active()
        self.list_store[check_row][5] = self.check_elements[5][2].get_active_text()
        
    def edit_data_win(self, widget, row, col):
        widget = widget.get_model()
        self.edit_mode = row
        if row[0] % 2 == 0:
            arg_row = row[0]
            check_row = row[0] + 1
        else:
            arg_row = row[0] - 1
            check_row = row[0]

        form_data = [widget[arg_row][0], widget[arg_row][1], widget[arg_row][2], widget[arg_row][3], widget[arg_row][4]]
        form_data += [widget[check_row][0], widget[check_row][1], widget[check_row][2], widget[check_row][3], widget[check_row][4], widget[check_row][5]]
        
        self.data_win(form_data=form_data)
    
    def save_config(self, widget):
        self.config_file_content += self.conf_elements[0][1].get_text() + " " + self.conf_elements[1][1].get_text() + " "\
                                 + self.conf_elements[2][1].get_text() + " " + str(self.conf_elements[3][1].get_active()) + " "\
                                 + self.conf_elements[4][1].get_text() + " " + self.conf_elements[5][1].get_text() + " "\
                                 + self.conf_elements[6][1].get_text() + "\n"
        for record in self.list_store:
            self.config_file_content += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " " + str(record[5]) + "\n"
            
    def validate_fields(self):
        return True
        for i in range(3):
            if(self._arg_elements[i][1].get_text() == ""):
                d = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "Enter * fields data in Argument part.");
                d.run()
                d.destroy()
                return False
            
        for i in [1, 2]:
            if(self._check_elements[i][1].get_text() == ""):
                d = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "Enter * fields data in Check part.");
                d.run()
                d.destroy()
                return False
            
        for i in [3, 5]:
            if(self._check_elements[i][1].get_active_text() == ""):
                d = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "Choice * fields data in Check part.");
                d.run()
                d.destroy()
                return False
        return True