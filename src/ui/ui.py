class UI(object):
    @staticmethod
    def load_ui(type):
        if type not in ['gtk', 'qt']:
            raise NotImplementedError("There is No %s UI library!" % type)

        if type == 'gtk':
            from gtk_base import GtkBase
            return GtkBase()

        elif type == 'qt':
            from qt_base import QTBase
            return QTBase()