import gtk


class Pointer(gtk.Window):
    def __init__(self):
        super(Pointer, self).__init__()
        
        self.set_size_request(700, 400)
        self.set_title("UGTrain - Pointer Form")
        self.show_all()