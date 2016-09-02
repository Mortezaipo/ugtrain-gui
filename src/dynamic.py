import gtk


class Dynamic(gtk.Window):
    def __init__(self):
        super(Dynamic, self).__init__()
        
        self.set_size_request(700, 400)
        self.set_title("UGTrain - Dynamic Form")
        self.show_all()