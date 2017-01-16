"""Draw Table Library."""

try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
except ImportError:
    show('error', 'Python GTK3.0 library not found.')
    sys.exit(1)


class Table:
    """Table class.

    Args:
        *items: List of lists of objects like ((x,y), (x,y))
    """
    def __init__(self, *items):
        self.items = items
        self.table = Gtk.Grid()

    def render(self):
        """Render the final results.

        Returns:
            Gtk table object
        """
        top = 0
        left = 0
        for row in self.items:
            for cell in row:
                self.table.attach(cell, left, top, 500, 10)
                # self.table.attach(cell,
                #                   left,
                #                   self.cols-left,
                #                   top,
                #                   self.rows-top,
                #                   Gtk.AttachOptions.SHRINK |
                #                   Gtk.AttachOptions.FILL)
                left += 1
            left = 0
            top += 10
        return self.table
