"""Windows Layout Management Library."""

import sys
from .show import show

try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk, Gdk
except ImportError:
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
    def __init__(self, name, title, size, close_btn=True, *btns):
        # Window header bar config
        self.header_bar = Gtk.HeaderBar()
        Gtk.Window.__init__(self, title="UGTrain - {}".format(title))
        self.header_bar.props.title = "UGTrain - {}".format(title)
        self.set_titlebar(self.header_bar)
        self.set_name(name)

        # Windows body size
        self.set_default_size(*size)
        self.set_border_width(10)

        # Window action buttons
        self.header_bar.set_show_close_button(close_btn)

        # Load and set CSS style (Theme)
        style = Gtk.CssProvider()
        style.load_from_data(open('css/style.css', 'rb').read())  # FIXME
        Gtk.StyleContext().add_provider_for_screen(
            Gdk.Screen.get_default(),
            style,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        # Add buttons or menus to the header bar based on their positions
        if btns:
            for obj, position in btns:
                if position == 'left':
                    self.header_bar.pack_start(obj)
                elif position == 'right':
                    self.header_bar.pack_end(obj)

        # Add Box in Window
        self.box = Gtk.Box(spacing=10)
        self.box.set_homogeneous(False)
        self.add(self.box)

        # Handle destroy signal on Window
        self.signal('delete_event', Gtk.main_quit)

    def add_item(self, item_obj, position='center'):
        """Add item inside of the main box.

        Args:
            item_obj: Gtk item object.
            position: Item position on Window Box.
        Returns:
            None
        """
        if position == 'center':
            self.box.set_center_widget(item_obj)
        elif position == 'left':
            self.box.pack_start(item_obj, True, True, 0)
        elif position == 'right':
            self.box.pack_end(item_obj, True, True, 0)

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
        """Render the final results.

        Returns:
            None
        """
        self.show_all()
        Gtk.main()
