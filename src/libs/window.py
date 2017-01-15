"""Windows Layout Management Library."""

import sys
from .show import show

try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
except:
    show('error', 'Python GTK3.0 library not found.')
    sys.exit(1)


class Window(Gtk.Window):
    """Windows layout management class.

    Args:
        title: Window title.
        size: List of Window size (x, y).
        close_btn: Show close button on the Window header bar.
        *btns: List of all buttons or menus objects which
                to be shown on the Window header bar.
    """

    def __init__(self, title, size, close_btn=True, *btns):
        # Window header bar settings
        self.header_bar = Gtk.HeaderBar()
        Gtk.Window.__init__(self, title="UGTrain - {}".format(title))
        self.header_bar.props.title = "UGTrain - {}".format(title)
        self.set_titlebar(self.header_bar)

        # Windows body size
        self.set_default_size(*size)
        self.set_border_width(10)

        # Window action buttons
        self.header_bar.set_show_close_button(close_btn)

        # Add buttons or menus to the header bar based on their positions
        if btns:
            for obj, position in btns:
                if position == 'left':
                    self.header_bar.pack_start(obj)
                elif position == 'right':
                    self.header_bar.pack_end(obj)

        # Handle destroy signal on Window
        self.signal('delete_event', Gtk.main_quit)

    def signal(self, event, action):
        """Window Signal handler.

        Args:
            event: name of event which will be happend.
            action: The function which should be run on the event.
        Returns:
            None
        """
        self.connect(event, action)

    def render(self):
        """Render final results.

        Returns:
            None
        """
        self.show_all()
        Gtk.main()
