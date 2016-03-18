import gtk


class Static(gtk.Window):
    def __init__(self):
        super(Static, self).__init__()
        
        self.set_size_request(700, 400)
        self.set_title("UGTrain - Static Form")
        self.show_all()